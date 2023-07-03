# Write a recursive searching algorithm to search for a number entered by user in a list of numbers.

def recursive_search(num, lst, index=0):
    """
    A recursive function to search for a number in a list and return its index.
    If the number is not found, returns None.
    """
    if index == len(lst):  # base case: end of list
        return None
    elif lst[index] == num:  # base case: number found
        return index
    else:  # recursive case: search next index
        return recursive_search(num, lst, index+1)
    

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_to_search = int(input("Enter a number to search for: "))

index = recursive_search(num_to_search, numbers)

if index is not None:
    print(f"{num_to_search} found at index {index}")
else:
    print(f"{num_to_search} not found in list")