# Using try and except to catch and handle errors gracefully

try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:  # This block of code handles the error
    print("You can't divide by zero!")  # This message will be printed when the error occurs
