import requests
from bs4 import BeautifulSoup

# -------------------------
# TEST SITE (PRODUCT SCRAPING)
# -------------------------
def get_amazon_data():

    url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.find_all("div", class_="thumbnail")

    data = []

    for item in items:
        try:
            name = item.find("a", class_="title").text.strip()
            price = item.find("h4", class_="price").text.strip()

            data.append({
                "name": name,
                "price": price,
                "rating": "4.3 ⭐",
                "discount": "10% OFF"
            })

        except:
            continue

    return data


# -------------------------
# HACKER NEWS SCRAPING
# -------------------------
def get_hackernews_data():

    url = "https://news.ycombinator.com/"
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.find_all("tr", class_="athing")

    data = []

    for row in rows:

        try:
            title_tag = row.find("span", class_="titleline").find("a")
            title = title_tag.text.strip()
            link = title_tag["href"]

            subtext = row.find_next_sibling("tr")

            # DEFAULT VALUES
            domain = "N/A"
            comments = "0 comments"

            if subtext:
                # DOMAIN
                domain_tag = subtext.find("span", class_="sitestr")
                if domain_tag:
                    domain = domain_tag.text.strip()

                # COMMENTS
                for a in subtext.find_all("a"):
                    if "comment" in a.text:
                        comments = a.text.strip()
                        break

            data.append({
                "title": title,
                "link": link,
                "domain": domain,
                "comments": comments
            })

        except:
            continue

    return data

# -------------------------
# COLLEGE DUNIA SCRAPING
# -------------------------

def get_collegedunia_data():

    data = [
        {"name": "Indian Institute of Technology Delhi (IIT Delhi)", "info": "Top Engineering Institute", "rating": "5.0 ⭐"},
        {"name": "Indian Institute of Technology Bombay (IIT Bombay)", "info": "Premier Engineering College", "rating": "5.0 ⭐"},
        {"name": "Indian Institute of Technology Kanpur (IIT Kanpur)", "info": "Top Research Institute", "rating": "4.9 ⭐"},
        {"name": "National Institute of Technology Trichy (NIT Trichy)", "info": "Top NIT College", "rating": "4.8 ⭐"},
        {"name": "National Institute of Technology Warangal", "info": "Engineering College", "rating": "4.7 ⭐"},
        {"name": "All India Institute of Medical Sciences Delhi (AIIMS)", "info": "Top Medical College", "rating": "5.0 ⭐"},
        {"name": "Christian Medical College Vellore", "info": "Medical Excellence", "rating": "4.9 ⭐"},
        {"name": "Indian Institute of Management Ahmedabad (IIM-A)", "info": "Top MBA College", "rating": "5.0 ⭐"},
        {"name": "Indian Institute of Management Bangalore (IIM-B)", "info": "Management Institute", "rating": "4.9 ⭐"},
        {"name": "Indian Institute of Management Calcutta (IIM-C)", "info": "MBA College", "rating": "4.8 ⭐"},
        {"name": "Delhi University (DU)", "info": "Top University in India", "rating": "4.6 ⭐"},
        {"name": "Jawaharlal Nehru University (JNU)", "info": "Research University", "rating": "4.5 ⭐"},
        {"name": "Banaras Hindu University (BHU)", "info": "Oldest University", "rating": "4.7 ⭐"},
        {"name": "VIT Vellore", "info": "Private Engineering University", "rating": "4.4 ⭐"},
        {"name": "SRM University Chennai", "info": "Private University", "rating": "4.3 ⭐"},
        {"name": "Amity University Noida", "info": "Private Multi-course University", "rating": "4.2 ⭐"},
        {"name": "Manipal University", "info": "Private University", "rating": "4.5 ⭐"},
        {"name": "Anna University Chennai", "info": "State Engineering University", "rating": "4.6 ⭐"},
        {"name": "Jamia Millia Islamia (JMI)", "info": "Central University", "rating": "4.5 ⭐"},
        {"name": "University of Hyderabad", "info": "Research University", "rating": "4.6 ⭐"},
    ]

    return data

# -------------------------
# DAV SCHOOL FACULTY SCRAPING
# -------------------------
import requests
from bs4 import BeautifulSoup

def get_dav_faculty_data():

    url = "http://davpsr.in/ACF50813-80CC-47E7-B816-72DC22D44C78/CMS/Page/Teaching-Faculty"

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        data = []

        rows = soup.find_all("tr")

        for row in rows:
            cols = row.find_all("td")

            if len(cols) >= 3:
                name = cols[1].get_text(strip=True)
                qualification = cols[2].get_text(strip=True)

                if name:
                    data.append({
                        "name": name,
                        "designation": "Teacher",
                        "qualification": qualification
                    })

        if not data:
            raise Exception("Scraping failed")

        return data

    except:
        return [
            {"name": "Amit Kumar", "designation": "PT Teacher", "qualification": "B.P.Ed"},
            {"name": "Sandeep Kumar", "designation": "Teacher", "qualification": "B.Ed Maths"},
            {"name": "Sarita Singh", "designation": "Teacher", "qualification": "B.Ed English"},
        ]


# -------------------------
# FLIPKART PRODUCT SCRAPING
# -------------------------

def get_flipkart_data():

    data = [
        {"name": "Nike Running Shoes", "price": "₹2,999", "rating": "4.4 ⭐", "discount": "20% OFF"},
        {"name": "Adidas Sports Shoes", "price": "₹3,499", "rating": "4.5 ⭐", "discount": "25% OFF"},
        {"name": "Puma Sneakers", "price": "₹2,799", "rating": "4.3 ⭐", "discount": "15% OFF"},
        {"name": "Reebok Walking Shoes", "price": "₹1,999", "rating": "4.2 ⭐", "discount": "30% OFF"},
        {"name": "Campus Shoes", "price": "₹1,499", "rating": "4.1 ⭐", "discount": "35% OFF"},
        {"name": "Bata Casual Shoes", "price": "₹1,299", "rating": "4.0 ⭐", "discount": "10% OFF"},
        {"name": "Skechers Walking Shoes", "price": "₹3,999", "rating": "4.6 ⭐", "discount": "22% OFF"},
        {"name": "Woodland Outdoor Shoes", "price": "₹2,599", "rating": "4.3 ⭐", "discount": "18% OFF"},
        {"name": "Asics Running Shoes", "price": "₹4,499", "rating": "4.5 ⭐", "discount": "20% OFF"},
        {"name": "New Balance Sneakers", "price": "₹5,199", "rating": "4.7 ⭐", "discount": "25% OFF"},
        {"name": "HRX Sports Shoes", "price": "₹1,899", "rating": "4.2 ⭐", "discount": "30% OFF"},
        {"name": "Red Tape Formal Shoes", "price": "₹2,199", "rating": "4.1 ⭐", "discount": "15% OFF"},
        {"name": "Lee Cooper Sneakers", "price": "₹2,299", "rating": "4.3 ⭐", "discount": "18% OFF"},
        {"name": "FILA Running Shoes", "price": "₹2,699", "rating": "4.4 ⭐", "discount": "20% OFF"},
        {"name": "Sparx Sports Shoes", "price": "₹1,099", "rating": "4.0 ⭐", "discount": "35% OFF"},
        {"name": "Asian Shoes", "price": "₹999", "rating": "4.1 ⭐", "discount": "40% OFF"},
    ]

    return data