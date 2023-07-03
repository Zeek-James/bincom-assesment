#  Which color is mostly worn throughout the week?

import re

# Define a function to count occurrences of each color in the week
def count_colors(colors):
    # Create a dictionary to store the count of each color
    color_counts = {}
    # Split the colors string into a list of individual colors
    color_list = re.findall(r'\w+', colors)
    # Loop through the list and count the occurrences of each color
    for color in color_list:
        if color not in color_counts:
            color_counts[color] = 1
        else:
            color_counts[color] += 1
    return color_counts

# Define a function to find the color with the highest count
def most_worn_color(colors):
    # Count the occurrences of each color in the week
    color_counts = count_colors(colors)
    # Find the color with the highest count
    most_worn = max(color_counts, key=color_counts.get)
    return most_worn

# Example usage
monday_colors = "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN"
tuesday_colors = "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE"
wednesday_colors = "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE"
thursday_colors = "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN"
friday_colors = "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"

all_colors = monday_colors + tuesday_colors + wednesday_colors + thursday_colors + friday_colors

most_worn = most_worn_color(all_colors)
print("The color mostly worn throughout the week is:", most_worn)