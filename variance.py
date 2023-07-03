# Get the variance of the colors
from bs4 import BeautifulSoup
import statistics


# Define a dictionary to map colors to integer values
color_map = {
    'arsh': 0,
    'brown': 1,
    'green': 2,
    'blue': 3,
    'blew': 4,
    'pink': 5,
    'yellow': 6,
    'red': 7,
    'white': 8,
    'black': 9,
    'cream': 10,
    'orange': 11
}


html = '''
<table>
	<thead>
		<th>DAY</th><th>COLOURS</th>
	</thead>
	<tbody>
	<tr>
		<td>MONDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>TUESDAY</td>
		<td>ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE</td>
	</tr>
	<tr>
		<td>WEDNESDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE</td>
	</tr>
	<tr>
		<td>THURSDAY</td>
		<td>BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>FRIDAY</td>
		<td>GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE</td>
	</tr>
	</tbody>
</table>
'''



# Parse the HTML table
soup = BeautifulSoup(html, "html.parser")

# Extract the table
table = soup.find('table')
rows = table.find_all('tr')[1:]  


# create an empty list to store the colors data
colors_data = []

# loop through each row of the table and extract the colors data
for row in rows:
    data = row.find_all("td")[1].text.split(", ")
    colors_data.extend(data)

# convert the list of colors data to lowercase
colors_data = [color.lower() for color in colors_data]

# Define the array of colors
colors = ['arsh', 'brown', 'green', 'brown', 'blue', 'blue', 'blew', 'pink', 'pink', 'orange', 'orange', 'red', 'white', 'blue', 'white', 'white', 'blue', 'blue', 'blue', 'green', 'yellow', 'green', 'brown', 'blue', 'pink', 'red', 'yellow', 'orange', 'red', 'orange', 'red', 'blue', 'blue', 'white', 'blue', 'blue', 'white', 'white', 'blue', 'blue', 'green', 'white', 'blue', 'brown', 'pink', 'yellow', 'orange', 'cream', 'orange', 'red', 'white', 'blue', 'white', 'blue', 'blue', 'blue', 'green', 'green', 'white', 'green', 'brown', 'blue', 'blue', 'black', 'white', 'orange', 'red', 'red', 'red', 'white', 'blue', 'white', 'blue', 'blue', 'blue', 'white']

# Convert the array of colors to an array of integers
color_values = [color_map[color] for color in colors_data]


# calculate the variance of the colors
variance = statistics.variance(color_values)

# print the variance of the colors
print("Variance of the colors:", variance)