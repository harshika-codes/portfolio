from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# ---------------- COMMON DRIVER ----------------
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver


# ---------------- AMAZON DYNAMIC ----------------
def get_amazon_data():
    driver = get_driver()
    products = []

    try:
        driver.get("https://www.amazon.in/s?k=mobiles")
        time.sleep(5)

        items = driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")

        for item in items[:10]:
            try:
                title = item.find_element(By.CSS_SELECTOR, "h2 span").text.strip()
            except:
                title = "N/A"

            try:
                price = item.find_element(By.CSS_SELECTOR, "span.a-price-whole").text.strip()
            except:
                price = "N/A"

            rating = "No Rating"
            try:
                rating = item.find_element(By.CSS_SELECTOR, "span.a-icon-alt").get_attribute("textContent").strip()
            except:
                pass

            if rating != "No Rating":
                rating = rating.split(" ")[0]

            products.append({
                "title": title,
                "price": price,
                "rating": rating
            })

    finally:
        driver.quit()

    return products


# ---------------- YOUTUBE DYNAMIC ----------------
def get_youtube_data():
    driver = get_driver()
    videos = []

    try:
        driver.get("https://www.youtube.com/results?search_query=triggered+insaan")

        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, '//ytd-video-renderer'))
        )
        time.sleep(3)

        items = driver.find_elements(By.XPATH, '//ytd-video-renderer')[:15]

        for item in items:
            try:
                title_el = item.find_element(By.ID, "video-title")
                title = title_el.get_attribute("title") or title_el.text.strip()
                link = title_el.get_attribute("href")
            except:
                continue

            views = "N/A"
            upload_time = "N/A"

            try:
                meta = item.find_elements(By.XPATH, './/*[@id="metadata-line"]/span')
                if len(meta) > 0:
                    views = meta[0].text.strip()
                if len(meta) > 1:
                    upload_time = meta[1].text.strip()
            except:
                pass

            videos.append({
                "title": title,
                "views": views,
                "time": upload_time,
                "link": link
            })

    finally:
        driver.quit()

    return videos


# ---------------- MYNTRA DYNAMIC ----------------
def get_myntra_data():
    driver = get_driver()
    products = []

    try:
        driver.get("https://www.myntra.com/men-tshirts")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "li.product-base"))
        )
        time.sleep(3)

        items = driver.find_elements(By.CSS_SELECTOR, "li.product-base")

        for item in items[:20]:
            try:
                brand = item.find_element(By.CSS_SELECTOR, "h3.product-brand").text.strip()
            except:
                brand = "N/A"

            try:
                title = item.find_element(By.CSS_SELECTOR, "h4.product-product").text.strip()
            except:
                title = "N/A"

            price = "N/A"
            try:
                price = item.find_element(By.CSS_SELECTOR, "span.product-discountedPrice").text.strip()
            except:
                try:
                    price = item.find_element(By.CSS_SELECTOR, "span.product-price").text.strip()
                except:
                    pass

            try:
                original_price = item.find_element(By.CSS_SELECTOR, "span.product-strike").text.strip()
            except:
                original_price = "N/A"

            try:
                discount = item.find_element(By.CSS_SELECTOR, "span.product-discountPercentage").text.strip()
            except:
                discount = "N/A"

            products.append({
                "brand": brand,
                "title": title,
                "price": price,
                "original_price": original_price,
                "discount": discount
            })

    finally:
        driver.quit()

    return products


# ---------------- INDEED DYNAMIC ----------------
def get_indeed_data():
    driver = get_driver()
    jobs = []

    try:
        driver.get("https://in.indeed.com/jobs?q=python+developer&l=India")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        time.sleep(5)

        items = driver.find_elements(By.CSS_SELECTOR, "div.job_seen_beacon")
        if not items:
            items = driver.find_elements(By.CSS_SELECTOR, "div.slider_container")

        for item in items[:15]:
            title = "N/A"
            company = "N/A"
            location = "N/A"

            try:
                title = item.find_element(By.CSS_SELECTOR, "h2.jobTitle").text.strip()
            except:
                try:
                    title = item.find_element(By.CSS_SELECTOR, "a.jcs-JobTitle span").text.strip()
                except:
                    pass

            try:
                company = item.find_element(By.CSS_SELECTOR, "[data-testid='company-name']").text.strip()
            except:
                try:
                    company = item.find_element(By.CSS_SELECTOR, "span.companyName").text.strip()
                except:
                    pass

            try:
                location = item.find_element(By.CSS_SELECTOR, "[data-testid='text-location']").text.strip()
            except:
                try:
                    location = item.find_element(By.CSS_SELECTOR, "div.companyLocation").text.strip()
                except:
                    pass

            jobs.append({
                "title": title,
                "company": company,
                "location": location
            })

    finally:
        driver.quit()

    return jobs


# ---------------- GITHUB DYNAMIC ----------------
def get_github_data():
    driver = get_driver()
    repos = []

    try:
        driver.get("https://github.com/trending")

        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.Box-row"))
        )
        time.sleep(3)

        items = driver.find_elements(By.CSS_SELECTOR, "article.Box-row")

        for item in items[:15]:
            name = "N/A"
            description = "N/A"
            language = "N/A"
            stars = "N/A"
            link = "N/A"

            try:
                repo_tag = item.find_element(By.CSS_SELECTOR, "h2 a")
                name = repo_tag.text.strip().replace("\n", "").replace(" ", "")
                link = repo_tag.get_attribute("href")
            except:
                pass

            try:
                description = item.find_element(By.CSS_SELECTOR, "p").text.strip()
            except:
                pass

            try:
                language = item.find_element(By.CSS_SELECTOR, "span[itemprop='programmingLanguage']").text.strip()
            except:
                pass

            try:
                star_links = item.find_elements(By.CSS_SELECTOR, "a.Link--muted")
                if len(star_links) > 0:
                    stars = star_links[0].text.strip()
            except:
                pass

            repos.append({
                "name": name,
                "description": description,
                "language": language,
                "stars": stars,
                "link": link
            })

    finally:
        driver.quit()

    return repos