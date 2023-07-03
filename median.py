#  Which color is the median? 

import re
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


# extract colors from table
colors = []
pattern = re.compile('[a-zA-Z]+')
for row in rows:
    cells = row.find_all('td')
    colors += pattern.findall(cells[1].text)

# sort colors
colors.sort()

# find median color
if len(colors) % 2 == 0:
    middle = int(len(colors) / 2)
    median = (colors[middle - 1], colors[middle])
else:
    middle = int(len(colors) / 2)
    median = colors[middle]

print(f"The median color is {median}")