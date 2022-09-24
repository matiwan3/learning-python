import datetime
from calendar import month
from datetime import datetime

def ask_for_birthdate():
    year = int(input("Please enter the year of birth: "))
    month = int(input("Please enter the month of birth: "))
    day = int(input("Please enter the day of birth: "))
    birthdate = datetime(year,month,day)
    return birthdate

def calculate_days(birth_date):
    today = datetime.today()
    number_of_days = today - birth_date
    return number_of_days.days

def main():
    birthdate = ask_for_birthdate()
    number_of_days = calculate_days(birthdate)
    print(f'\n You are living {number_of_days} days!')

if __name__ =="__main__":
    main()
    
