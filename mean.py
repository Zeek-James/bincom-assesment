# Which color of shirt is the mean color?

import statistics

from bs4 import BeautifulSoup
import requests

url = "http://127.0.0.1:5500/index.html"

# Get the HTML content of the page
response = requests.get(url)
html_content = response.content

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the table
table = soup.find('table')
rows = table.find_all('tr')[1:]  
# Extract the colors from the table
colors = []
for row in rows:
    cells = row.find_all('td')
    color_string = cells[1].text
    color_list = color_string.split(', ')
    colors += color_list

# Calculate the mean color
mean_color = statistics.mode(colors)
print('The mean color is:', mean_color)
