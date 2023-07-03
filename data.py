#  Save the colours and their frequencies in postgresql database

from bs4 import BeautifulSoup
from collections import Counter
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
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
data = []
for row in rows:
    day, colors = row.find_all("td")
    colors = colors.text.strip().split(", ")
    data.extend(colors)

# Count the frequencies of each color
counter = Counter(data)
colors = list(counter.keys())
frequencies = list(counter.values())

# Create a connection to the PostgreSQL database using SQLAlchemy
engine = create_engine("postgresql://postgres:R3L8IvBKVSXQ0Zfd2BFw@containers-us-west-136.railway.app:6912/railway")
metadata = MetaData()

# Define a table to store the colors and their frequencies
table = Table(
    "colors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("color", String),
    Column("frequency", Integer)
)

# Create the table if it doesn't exist
metadata.create_all(engine)

# Insert the colors and their frequencies into the database
with engine.connect() as conn:
    for i in range(len(colors)):
        color = colors[i]
        frequency = frequencies[i]
        conn.execute(table.insert().values(color=color, frequency=frequency))
