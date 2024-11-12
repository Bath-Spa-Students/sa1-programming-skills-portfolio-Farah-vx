#month num and days in the month using dictionary (advance)
month_days={"1":"31",#january
            "2":"28",#february  
            "3":"31",#march
            "4":"30",#april
            "5":"31",#may
            "6":"30",#june
            "7":"31",#july
            "8":"31",#august
            "9":"30",#september
            "10":"31",#october
            "11":"30",#november
            "12":"31"}#december

#requesting input of month num
month = int(input("enter month number(1-12): "))
#validating month number
if 1 <= month <= 12:
    month_str = str(month) #altering month num to string

#checking if the month is a leap year
    if month_str == "2":
       #asking user if its a leap year
        leap_year = input("is it a leap year?(yes/no): ").lower()
        if leap_year == "yes":
            print(f"there are 29 days in {month_str}")
        else:
            print(f"there are 28 days in {month_str}") 
    else:
        print(f"there are {month_days[month_str]}  days in {month_str}")
else:
    print("invalid month number")  
    