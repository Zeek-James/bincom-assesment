#  If a colour is chosen at random, what is the probability that the color is red?

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
    color_list = row.find_all("td")[1].text.strip().split(", ")
    colors.extend(color_list)

# count the occurrences of red
num_red = colors.count("RED")

# calculate the probability of choosing red
probability_red = num_red / len(colors)

print(f"The probability of choosing red at random is {probability_red:.2f}")