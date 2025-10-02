try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print("Division successful:", x)
finally:
    print("End of program")
