import requests
from bs4 import BeautifulSoup
import re

def get_gyan_setu_courses():
    url = "https://www.gyansetu.in/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=20)
    soup = BeautifulSoup(response.text, "html.parser")

    courses = []
    seen = set()

    # poore homepage ka text le lo
    text = soup.get_text("\n", strip=True)
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    i = 0
    while i < len(lines):
        line = lines[i]

        # course blocks usually aise mil rahe hain:
        # Course Name
        # 9269 reviews
        # Next Batch - 11 Jul, 2026
        # 6 months
        # Online/ Offline
        # View Details

        # line ko course name maan lo agar ye normal text hai aur next lines me reviews/batch/months ho
        if (
            i + 4 < len(lines)
            and "reviews" in lines[i + 1].lower()
            and "next batch" in lines[i + 2].lower()
        ):
            course_name = line
            duration = "-"
            mode = "-"

            # next 5-6 lines scan karo
            block = lines[i:i+7]

            for item in block:
                item_low = item.lower()

                # duration like 3 months / 4 months / 6 months
                if "month" in item_low:
                    duration = item.strip()

                # mode
                if "online" in item_low or "offline" in item_low:
                    mode = item.strip()

            key = (course_name, duration, mode)
            if course_name not in seen:
                seen.add(course_name)
                courses.append({
                    "course_name": course_name,
                    "mode": mode,
                    "duration": duration,
                    
                })

            i += 6
        else:
            i += 1

    # agar duplicates ya weird rows aaye hon to clean करो
    cleaned = []
    used = set()

    for c in courses:
        name = c["course_name"].strip()

        # random headings skip karo
        bad_words = [
            "popular courses", "view all", "why choose", "our impact",
            "explore courses", "full stack development courses",
            "data analytics 360° courses", "data science 360° courses"
        ]

        if len(name) < 3:
            continue
        if any(bad in name.lower() for bad in bad_words):
            continue
        if name in used:
            continue

        used.add(name)
        cleaned.append(c)

    return {
        "title": "Gyan Setu Courses",
        "courses": cleaned
    }

#------------product api--------------#

import requests

def get_products_api_data():
    url = "https://dummyjson.com/products"
    response = requests.get(url, timeout=20)
    data = response.json()

    products = []

    for item in data["products"]:
        products.append({
            "title": item.get("title", ""),
            "price": item.get("price", ""),
            "category": item.get("category", ""),
            "brand": item.get("brand", ""),
            "rating": item.get("rating", "")
        })

    return products

#---------currency api--------#

def get_currency_data():
    return [
        {"currency": "USD", "rate": 1.00},
        {"currency": "INR", "rate": 83.50},
        {"currency": "EUR", "rate": 0.92},
        {"currency": "GBP", "rate": 0.78},
        {"currency": "JPY", "rate": 160.25},
        {"currency": "AUD", "rate": 1.52},
        {"currency": "CAD", "rate": 1.36},
        {"currency": "CHF", "rate": 0.89},
        {"currency": "CNY", "rate": 7.25},
        {"currency": "SGD", "rate": 1.34},
        {"currency": "AED", "rate": 3.67},
        {"currency": "SAR", "rate": 3.75},
        {"currency": "NZD", "rate": 1.65},
        {"currency": "KRW", "rate": 1380.45},
        {"currency": "RUB", "rate": 88.20},
        {"currency": "ZAR", "rate": 18.45},
        {"currency": "BRL", "rate": 5.42},
        {"currency": "MXN", "rate": 17.95},
        {"currency": "THB", "rate": 36.10},
        {"currency": "HKD", "rate": 7.81}
    ]
    
#------------rest countries  api-------------#
def get_countries_api_data():
    return [
        {
            "name": "India",
            "capital": "New Delhi",
            "region": "Asia",
            "population": 1400000000,
            "flag": "https://flagcdn.com/w320/in.png"
        },
        {
            "name": "Japan",
            "capital": "Tokyo",
            "region": "Asia",
            "population": 125000000,
            "flag": "https://flagcdn.com/w320/jp.png"
        },
        {
            "name": "United States",
            "capital": "Washington, D.C.",
            "region": "North America",
            "population": 331000000,
            "flag": "https://flagcdn.com/w320/us.png"
        },
        {
            "name": "Canada",
            "capital": "Ottawa",
            "region": "North America",
            "population": 38000000,
            "flag": "https://flagcdn.com/w320/ca.png"
        },
        {
            "name": "Australia",
            "capital": "Canberra",
            "region": "Oceania",
            "population": 26000000,
            "flag": "https://flagcdn.com/w320/au.png"
        },
        {
            "name": "Germany",
            "capital": "Berlin",
            "region": "Europe",
            "population": 83000000,
            "flag": "https://flagcdn.com/w320/de.png"
        },
        {
            "name": "France",
            "capital": "Paris",
            "region": "Europe",
            "population": 67000000,
            "flag": "https://flagcdn.com/w320/fr.png"
        },
        {
            "name": "Italy",
            "capital": "Rome",
            "region": "Europe",
            "population": 59000000,
            "flag": "https://flagcdn.com/w320/it.png"
        },
        {
            "name": "Brazil",
            "capital": "Brasília",
            "region": "South America",
            "population": 214000000,
            "flag": "https://flagcdn.com/w320/br.png"
        },
        {
            "name": "Argentina",
            "capital": "Buenos Aires",
            "region": "South America",
            "population": 46000000,
            "flag": "https://flagcdn.com/w320/ar.png"
        },
        {
            "name": "China",
            "capital": "Beijing",
            "region": "Asia",
            "population": 1410000000,
            "flag": "https://flagcdn.com/w320/cn.png"
        },
        {
            "name": "Russia",
            "capital": "Moscow",
            "region": "Europe/Asia",
            "population": 144000000,
            "flag": "https://flagcdn.com/w320/ru.png"
        },
        {
            "name": "South Africa",
            "capital": "Pretoria",
            "region": "Africa",
            "population": 60000000,
            "flag": "https://flagcdn.com/w320/za.png"
        },
        {
            "name": "Mexico",
            "capital": "Mexico City",
            "region": "North America",
            "population": 126000000,
            "flag": "https://flagcdn.com/w320/mx.png"
        },
        {
            "name": "South Korea",
            "capital": "Seoul",
            "region": "Asia",
            "population": 52000000,
            "flag": "https://flagcdn.com/w320/kr.png"
        }
    ]

#-----Json Placeholder API----------#
import requests

def get_jsonplaceholder_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        posts = []
        for item in data[:15]:
            posts.append({
                "id": item.get("id"),
                "title": item.get("title"),
                "body": item.get("body")
            })

        return posts

    except Exception as e:
        print("JSONPlaceholder API Error:", e)
        return []