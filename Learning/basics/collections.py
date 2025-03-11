# Creating a list, which is an ordered and mutable collection of items
fruits = ["apple", "banana", "cherry"]

# Adding an item to the list using the append() method
fruits.append("date")

# Printing the list after modification
print(fruits)  # This will output ['apple', 'banana', 'cherry', 'date']

# Creating a tuple, which is an ordered but immutable collection of items
coordinates = (10, 20)

# Accessing an element of the tuple by index (indexing starts at 0)
print(coordinates[0])  # This will output 10

# Creating a dictionary, which is a collection of key-value pairs
person = {"name": "Alice", "age": 25}

# Accessing a value using the key
print(person["name"])  # This will output 'Alice'

# Creating a set, which is an unordered collection of unique elements
numbers = {1, 2, 3, 3}  # The duplicate 3 will be automatically removed

# Printing the set (it will only show unique values)
print(numbers)  # This will output {1, 2, 3}
