from bs4 import BeautifulSoup
import requests
url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive"
}

response = session.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.select_one('table.wikitable')

temp_list = []
final_list = []

for row in table.select('tr'):
    td = row.select_one('td')
    if td:
        c = row.td.select_one('a') #country
        p = td.find_next_sibling('td').string #population
        if c:
            temp_list.append(
                (
                    int(p.replace(',','')),
                    c['title'],
                )
            )

temp_list = sorted(temp_list,reverse=True)
final_list = [{"rank":rank,"country":c,"population":p} for rank,(p,c) in enumerate(temp_list, start=1) if p>50000000]
print('\nTop 10 Countires ranked by population:\n\n',final_list[:10],'\n\n')


"""
#This is sample exercise 1 HackerNews

url = "https://news.ycombinator.com/"

session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive"
}

response = session.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

Exercise 6: Extract top 30 titles
for tag in soup.select('span.titleline'):
    print(tag.a.string)

Exercise 7: Extract title + score
titles = {}
for tag in soup.find_all('tr',class_="athing"):
    title = tag.select_one('span.titleline').a.string
    subtext = tag.find_next_sibling('tr')
    point = subtext.select_one('span.score')
    if not point:
        point = "None"
    else:
        point = point.getText()
    titles[title] = point
print(titles)

Exercise 8: Find highest voted post
titles = {}
for tag in soup.find_all('tr',class_="athing"):
    title = tag.select_one('span.titleline').a.string
    subtext = tag.find_next_sibling('tr')
    point = subtext.select_one('span.score')
    if not point:
        point = "None"
    else:
        point = point.getText()
    titles[title] = point

max = 0
highest_post = {}

for t,point in titles.items():
    p = point.split()[0]
    if p == 'None':
        pass
    else:
        p = int(p)
        if p > max:
            max = p
            highest_post={t:max}
print(highest_post)

Exercise 9: Build a ranked list
titles = {}
for tag in soup.find_all('tr',class_="athing"):

    title = tag.select_one('span.titleline').a.string
    subtext = tag.find_next_sibling('tr')
    point = subtext.select_one('span.score')
    if point != None:
        titles[title] = int(point.getText().split()[0])
    else:
        titles[title] = "None"
    
clean = []
for t,p in titles.items():
    if p != "None":
        if p >=100 :
            clean.append((p,t))

temp_list_with_points = sorted(clean,reverse=True)
final_sorted_list = [{"title":t,"points":p} for p,t in temp_list_with_points]

print(final_sorted_list)

"""



"""
#This is sample exercise 2. BooksToScrape

url = "https://books.toscrape.com/"

session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive"
}

response = session.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

#Extract all book titles as a list
books = []
for titles in soup.find_all("h3"):
    books.append(titles.find("a")['title'])
# print(books)

#Extract title + price
books_with_price = []
for books in soup.find_all("article",class_="product_pod"):
    book_title = books.h3.find("a")['title']
    book_price = books.find("p",class_="price_color").string.replace('Â','')
    books_with_price.append((book_title,book_price))
# print(books_with_price)

# Extract book ratings and convert to number
book_ratings = []
star_rating_str = {'One':1,'Two':2,'Three':3,'Four':4,'Five':5}
for books in soup.find_all("article",class_="product_pod"):
    book_title = books.h3.find("a")['title']
    book_price = books.find("p",class_="price_color").string.replace('Â','')
    books_with_price.append((book_title,book_price))
    tag = books.find("p",class_="star-rating")
    rating_class = tag.get("class")[1]
    rating_num = star_rating_str[rating_class]
    book_ratings.append({
        "title": book_title,
        "rating": rating_num
    })
# print(book_ratings)

#Pagination using while loop
def pagination():
    base_url = "https://books.toscrape.com/catalogue/"
    curr_page = "page-1.html"
    while True:
        response = session.get(base_url+curr_page, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        try:
            # if soup.find("li",class_="next").a.string == "next":
            curr_page = soup.find("li",class_="next").a['href']
        except:
            break
        print(curr_page)

# Extract books with rating >= 4
book_ratings = []
star_rating_str = {'One':1,'Two':2,'Three':3,'Four':4,'Five':5}
for books in soup.find_all("article",class_="product_pod"):
    book_title = books.h3.find("a")['title']
    book_price = books.find("p",class_="price_color").string.replace('Â','')
    books_with_price.append((book_title,book_price))
    tag = books.find("p",class_="star-rating")
    rating_class = tag.get('class')[1]
    rating_num = star_rating_str[rating_class]
    if rating_num >= 4:
        book_ratings.append({"title":book_title,"rating":rating_num})
# print(book_ratings)
"""