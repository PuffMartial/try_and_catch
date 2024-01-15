try:
    # Code that might raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Code to handle the ZeroDivisionError
    print("Cannot divide by zero!")
except Exception as e:
    # Code to handle other types of exceptions
    print(f"An error occurred: {e}")
else:
    # Code to be executed if no exception occurred
    print("Division successful!")
finally:
    # Code that will be executed no matter what
    print("This will always be executed.")
