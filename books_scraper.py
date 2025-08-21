from bs4 import BeautifulSoup
import requests
import pandas

url = "https://books.toscrape.com"

book_links = []
prices = []
books = []
dict_of_books = {}

for a in range(1,10):
    response = requests.get(f"https://books.toscrape.com/catalogue/page-{a}.html")
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        break
    soup = BeautifulSoup(response.text, "html.parser")
    if soup is not None:
        print(a)
    ol = soup.find("ol", class_="row")

    all_prices = ol.find_all("p", class_="price_color")
    all_books = ol.find_all("h3")

    for book in all_books:
        books.append(book.find("a").get("title"))
        book_links.append(url + "/" + book.find("a").get("href"))

    for price in all_prices:
        prices.append(price.text[1:])


dict_of_books = {"Book": books,
                 "Link": book_links,
                 "Price": prices, }

df = pandas.DataFrame(dict_of_books)
df.to_csv("books.csv", mode="w",index=False,header=True)

