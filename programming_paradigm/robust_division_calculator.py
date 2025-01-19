def safe_divide(numerator, denominator):
    try:
        
         float(numerator) / float(denominator)
         print(f"The result of the divisionis {int(numerator) / int(denominator)}")
        
    except ZeroDivisionError:
        print("error: Can not divide by zero.")
    except ValueError:
        print("error: Please enter numeric value only.")
