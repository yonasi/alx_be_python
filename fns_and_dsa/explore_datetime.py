from datetime import datetime
from datetime import timedelta
def display_current_datetime():
    current_date = datetime.now()
    now =current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {now}")

def calculate_future_date():
    coming_day = int(input("Enter the number of days to add to the current date:"))
    future_date = datetime.now() + timedelta(days=coming_day)
    result = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future date: {result}")
display_current_datetime()
calculate_future_date()
