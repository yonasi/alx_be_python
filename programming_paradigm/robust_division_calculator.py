def safe_divide(numerator, denominator):
    try:
        
         float(numerator) / float(denominator)
         print(f"The result of the divisionis {int(numerator) / int(denominator)}")
        
    except ZeroDivisionError:
        message = "Error: Cannot divide by zero."
        return message
    except ValueError:
        message = "Error: Please enter numeric values only."
        return message
