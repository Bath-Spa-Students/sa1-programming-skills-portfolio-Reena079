#store days in a month
def days_in_month():
    month_days = {
        1: 31,  # January
        2: 28,  # February (default, may change in leap year)
        3: 31,  # March
        4: 30,  # April
        5: 31,  # May
        6: 30,  # June
        7: 31,  # July
        8: 31,  # August
        9: 30,  # September
        10: 31, # October
        11: 30, # November
        12: 31  # December
    }

    try:
        # Ask the user to enter a month number
        month_number = int(input("Enter a month number of your choice from 1 to 12: "))
        
        # Check if the number is within the valid range
        if 1 <= month_number <= 12:
            if month_number == 2:
                # make a condition that will operate if it is a leap year
                leap_year = input("Is it a leap year? (yes/no): ").strip().lower()
                print("Days in the month:", 29 if leap_year == "yes" else 28)
            else:
                print("Days in the month:", month_days[month_number])
        else:
            print("That is an invalid month number. Please enter a number from 1 to 12.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Call the function
days_in_month()