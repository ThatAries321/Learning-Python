# Defining a function that takes one parameter 'name' and prints a greeting message
def greet(name):
    print(f"Hello, {name}!")  # The f-string formats the output to include the value of 'name'

# Calling the function and passing an argument ('Alice') to it
greet("Alice")

# Defining a function that takes two parameters and returns their sum
def add(x, y):
    return x + y  # Returns the result of x + y

# Calling the function and storing the result in a variable 'result'
result = add(5, 3)

# Printing the result
print(result)  # This will output 8, as 5 + 3 equals 8
