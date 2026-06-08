import datetime

def is_valid_date(date_str, date_format="%Y-%m-%d"):
    """
    Check if the input date is valid based on the specified date format.
    :param date_str: date string
    :param date_format: date format string
    :return: true if the date string matches the specified format, false otherwise
    """
    try:
        datetime.datetime.strptime(date_str, date_format) # Parse the date string
        return True # Return True if the date string matches the format

    except (ValueError, TypeError): # Return False if the date string is not in the expected format
        return False

while True:
    date = input("Which year do you want to travel to? (YYYY-MM-DD): ")
    if is_valid_date(date): # Check if the input is a valid date
        print(f"You will travel to {date}!")
        break

    print("Invalid date. Please enter a valid date in the format YYYY-MM-DD.")