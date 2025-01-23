def my_function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None  # Or handle the error in another suitable way

result = my_function(10, 0)
result2 = my_function(10,2) 
print(result2) 