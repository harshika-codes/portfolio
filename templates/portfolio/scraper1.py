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

    # local + render dono ke liye
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")

    # user-agent add karo taaki site bot less detect kare
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.set_page_load_timeout(60)
    return driver


# ---------------- HELPER: SCROLL PAGE ----------------
def scroll_page(driver, times=3, pause=2):
    for _ in range(times):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause)


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
                rating = rating.split(" ")[0]
            except:
                pass

            if title != "N/A":
                products.append({
                    "title": title,
                    "price": price,
                    "rating": rating
                })

    except Exception as e:
        print("Amazon Error:", e)

    finally:
        driver.quit()

    return products


# ---------------- YOUTUBE DYNAMIC ----------------
def get_youtube_data():
    driver = get_driver()
    videos = []

    try:
        driver.get("https://www.youtube.com/results?search_query=triggered+insaan")
        time.sleep(5)

        WebDriverWait(driver, 25).until(
            EC.presence_of_all_elements_located((By.XPATH, '//ytd-video-renderer'))
        )

        scroll_page(driver, times=2, pause=2)

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

    except Exception as e:
        print("YouTube Error:", e)

    finally:
        driver.quit()

    return videos


# ---------------- MYNTRA DYNAMIC ----------------
def get_myntra_data():
    driver = get_driver()
    products = []

    try:
        driver.get("https://www.myntra.com/men-tshirts")
        time.sleep(8)

        # thoda scroll karo taaki products load ho jaye
        scroll_page(driver, times=3, pause=2)

        WebDriverWait(driver, 25).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.product-base"))
        )

        items = driver.find_elements(By.CSS_SELECTOR, "li.product-base")

        print("Myntra items found:", len(items))

        for item in items[:20]:
            brand = "N/A"
            title = "N/A"
            price = "N/A"
            original_price = "N/A"
            discount = "N/A"

            # BRAND
            try:
                brand = item.find_element(By.CSS_SELECTOR, "h3.product-brand").text.strip()
            except:
                pass

            # TITLE
            try:
                title = item.find_element(By.CSS_SELECTOR, "h4.product-product").text.strip()
            except:
                pass

            # PRICE
            try:
                price = item.find_element(By.CSS_SELECTOR, "span.product-discountedPrice").text.strip()
            except:
                try:
                    price = item.find_element(By.CSS_SELECTOR, "span.product-price").text.strip()
                except:
                    try:
                        price = item.find_element(By.CSS_SELECTOR, "div.product-price span").text.strip()
                    except:
                        pass

            # ORIGINAL PRICE
            try:
                original_price = item.find_element(By.CSS_SELECTOR, "span.product-strike").text.strip()
            except:
                pass

            # DISCOUNT
            try:
                discount = item.find_element(By.CSS_SELECTOR, "span.product-discountPercentage").text.strip()
            except:
                pass

            # useful rows hi add karo
            if brand != "N/A" or title != "N/A":
                products.append({
                    "brand": brand,
                    "title": title,
                    "price": price,
                    "original_price": original_price,
                    "discount": discount
                })

    except Exception as e:
        print("Myntra Error:", e)

    finally:
        driver.quit()

    return products


# ---------------- INDEED DYNAMIC ----------------
def get_indeed_data():
    driver = get_driver()
    jobs = []

    try:
        driver.get("https://in.indeed.com/jobs?q=python+developer&l=India")
        time.sleep(8)

        scroll_page(driver, times=2, pause=2)

        WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        items = []

        # multiple selectors try karo
        selectors = [
            "div.job_seen_beacon",
            "div.cardOutline",
            "div.slider_container",
            "div.jobsearch-SerpJobCard"
        ]

        for sel in selectors:
            items = driver.find_elements(By.CSS_SELECTOR, sel)
            if items:
                print("Indeed selector working:", sel, "Count:", len(items))
                break

        for item in items[:15]:
            title = "N/A"
            company = "N/A"
            location = "N/A"

            # TITLE
            try:
                title = item.find_element(By.CSS_SELECTOR, "h2.jobTitle span").text.strip()
            except:
                try:
                    title = item.find_element(By.CSS_SELECTOR, "a.jcs-JobTitle span").text.strip()
                except:
                    try:
                        title = item.find_element(By.CSS_SELECTOR, "h2 a").text.strip()
                    except:
                        pass

            # COMPANY
            try:
                company = item.find_element(By.CSS_SELECTOR, "[data-testid='company-name']").text.strip()
            except:
                try:
                    company = item.find_element(By.CSS_SELECTOR, "span.companyName").text.strip()
                except:
                    pass

            # LOCATION
            try:
                location = item.find_element(By.CSS_SELECTOR, "[data-testid='text-location']").text.strip()
            except:
                try:
                    location = item.find_element(By.CSS_SELECTOR, "div.companyLocation").text.strip()
                except:
                    pass

            if title != "N/A" or company != "N/A":
                jobs.append({
                    "title": title,
                    "company": company,
                    "location": location
                })

    except Exception as e:
        print("Indeed Error:", e)

    finally:
        driver.quit()

    return jobs


# ---------------- GITHUB DYNAMIC ----------------
def get_github_data():
    driver = get_driver()
    repos = []

    try:
        driver.get("https://github.com/trending")

        WebDriverWait(driver, 25).until(
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

            if name != "N/A":
                repos.append({
                    "name": name,
                    "description": description,
                    "language": language,
                    "stars": stars,
                    "link": link
                })

    except Exception as e:
        print("GitHub Error:", e)

    finally:
        driver.quit()

    return repos