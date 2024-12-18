def my_function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero!" 

result = my_function(10, 0)
print(result) # Output: Division by zero!