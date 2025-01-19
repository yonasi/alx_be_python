def safe_divide(numerator, denominator):
    try:
        
         float(numerator) / float(denominator)
         message = f"The result of the division is {int(numerator) / int(denominator)}"
         return message
    except ZeroDivisionError:
        message = "Error: Cannot divide by zero."
        return message
    except ValueError:
        message = "Error: Please enter numeric values only."
        return message
