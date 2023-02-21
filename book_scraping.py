import csv
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Send an HTTP request to the URL of the webpage you want to access
response = requests.get('https://books.toscrape.com/')

# Parse the content of the request with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the book titles and prices on the page
books = soup.find_all('article', class_='product_pod')
titles = [book.h3.a.attrs['title'] for book in books]
prices = [float(book.select('.price_color')[0].get_text()[1:]) for book in books]

# Write the data to a CSV file
with open('books.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Title', 'Price'])
    for i in range(len(titles)):
        writer.writerow([titles[i], prices[i]])

print('Data successfully written to CSV file.')

# Create a bar chart of the book prices
# plt.bar(titles, prices)
# plt.xticks(rotation=90)
# plt.xlabel('Book Titles')
# plt.ylabel('Price ($)')
# plt.title('Book Prices')
# plt.show()
