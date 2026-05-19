import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# WEB SCRAPING
# ==========================================

headers = {
    "User-Agent": "Mozilla/5.0"
}

all_books = []

# Scrape 5 pages
for page in range(1, 6):

    print(f"Scraping Page {page}...")

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        # Book Name
        name = book.h3.a["title"]

        # Price
        price = book.find(
            "p",
            class_="price_color"
        ).text

        # Rating
        rating = book.p["class"][1]

        # Availability
        availability = book.find(
            "p",
            class_="instock availability"
        ).text.strip()

        # Product Link
        link = book.h3.a["href"]

        full_link = (
            "https://books.toscrape.com/catalogue/" + link
        )

        # Image URL
        image = book.find("img")["src"]

        image_url = (
            "https://books.toscrape.com/" +
            image.replace("../", "")
        )

        # Store Data
        all_books.append({
            "Book Name": name,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Product Link": full_link,
            "Image URL": image_url
        })

# ==========================================
# CREATE DATAFRAME
# ==========================================

df = pd.DataFrame(all_books)

# ==========================================
# DATA CLEANING
# ==========================================

# Remove unwanted symbols
df["Price"] = (
    df["Price"]
    .str.replace("Â", "", regex=False)
    .str.replace("£", "", regex=False)
)

# Convert to numeric
df["Price"] = pd.to_numeric(
    df["Price"],
    errors="coerce"
)

# Remove missing values
df = df.dropna(subset=["Price"])

# ==========================================
# SAVE CSV
# ==========================================

df.to_csv("books_data.csv", index=False)

print("\nCSV File Saved Successfully!")

# ==========================================
# DISPLAY DATA
# ==========================================

print("\nFirst 5 Records:")
print(df.head())

# ==========================================
# DATA ANALYSIS
# ==========================================

# Top 10 Highest Priced Books
highest_books = df.sort_values(
    by="Price",
    ascending=False
).head(10)

print("\nTop 10 Highest Priced Books:")
print(highest_books[["Book Name", "Price"]])

# Average Price
average_price = df["Price"].mean()

print("\nAverage Book Price:")
print(round(average_price, 2))

# Rating Distribution
rating_distribution = df["Rating"].value_counts()

print("\nRating Distribution:")
print(rating_distribution)

# Most Common Rating
most_common_rating = df["Rating"].mode()[0]

print("\nMost Common Rating:")
print(most_common_rating)

# ==========================================
# VISUALIZATION 1 - BAR CHART
# ==========================================

plt.figure(figsize=(8,5))

rating_distribution.plot(kind="bar")

plt.title("Book Rating Distribution")
plt.xlabel("Ratings")
plt.ylabel("Count")

plt.show()

# ==========================================
# VISUALIZATION 2 - HISTOGRAM
# ==========================================

plt.figure(figsize=(8,5))

plt.hist(df["Price"], bins=10)

plt.title("Book Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.show()

# ==========================================
# VISUALIZATION 3 - PIE CHART
# ==========================================

plt.figure(figsize=(7,7))

rating_distribution.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Ratings Percentage Distribution")
plt.ylabel("")

plt.show()
