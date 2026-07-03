from flask import Flask, render_template

from scraper import get_amazon_data, get_hackernews_data, get_collegedunia_data, get_dav_faculty_data, get_flipkart_data
from scraper1 import get_amazon_data as get_dynamic_amazon_data, get_youtube_data, get_myntra_data, get_indeed_data, get_github_data
from scraper2 import get_gyan_setu_courses, get_products_api_data, get_currency_data, get_countries_api_data, get_jsonplaceholder_data
app = Flask(__name__)

# ---------------- HOME PAGES ----------------
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/learn-more")
def learn_more():
    return render_template("learnmore.html")


@app.route("/web-scraping")
def scraping():
    return render_template("scraping.html")


# ---------------- STATIC SCRAPING ----------------
@app.route("/static-scraping")
def static_scraping():
    return render_template("static.html")


@app.route("/amazon")
def amazon():
    data = get_amazon_data()
    return render_template("amazon.html", products=data)


@app.route("/hackernews")
def hackernews():
    data = get_hackernews_data()
    return render_template("hackernews.html", news=data)


@app.route("/collegedunia")
def collegedunia():
    data = get_collegedunia_data()
    return render_template("collegedunia.html", data=data)


# ✅ FIXED (removed confusion: use hyphen everywhere)
@app.route("/dav-faculty")
def dav_faculty():
    data = get_dav_faculty_data()
    return render_template("davfaculty.html", data=data)


@app.route("/flipkart")
def flipkart():
    data = get_flipkart_data()
    return render_template("flipkart.html", data=data)


# ---------------- DYNAMIC SCRAPING ----------------
@app.route("/dynamic-scraping")
def dynamic_sources():
    return render_template("dynamic.html")


@app.route("/amazon1")
def amazon1():
    data = get_dynamic_amazon_data()
    return render_template("amazon1.html", products=data)


@app.route("/youtube")
def youtube():
    data = get_youtube_data()
    return render_template("youtube.html", videos=data)


@app.route("/myntra")
def myntra():
    data = get_myntra_data()
    return render_template("myntra.html", products=data)


@app.route("/indeed")
def indeed():
    data = get_indeed_data()
    return render_template("indeed.html", jobs=data)


@app.route("/github")
def github():
    data = get_github_data()
    return render_template("github.html", repos=data)


# ---------------- 🔥 API SECTION (IMPORTANT FIX) ----------------

@app.route("/api")
def api_page():
    return render_template("api.html")


@app.route("/gyan-setu")
def gyan_setu_page():
    data = get_gyan_setu_courses()
    return render_template("gyansetu.html", data=data)

@app.route("/products-api")
def products_api():
    products = get_products_api_data()
    return render_template("products_api.html", products=products)

@app.route("/currency-api")
def currency_api():
    data = get_currency_data()
    return render_template("currency.html", data=data)

@app.route("/countries-api")
def countries_api():
    countries = get_countries_api_data()
    return render_template("countries_api.html", countries=countries)


@app.route("/jsonplaceholder-api")
def jsonplaceholder_api():
    posts = get_jsonplaceholder_data()
    return render_template("jsonplaceholder_api.html", posts=posts)

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)