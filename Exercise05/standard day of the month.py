#days of the month using dictionary;- month nums and days
month_days={1:31,
            2:28,
            3:31,
            4:30,
            5:31,
            6:30,
            7:31,
            8:31,
            9:30,
            10:31,
            11:30,
            12:31}
#askimg user to input month num
month = int(input("enter month number(1-12): "))
    
#validating the input
if month in range (1,13):
    print(f"the no. of days in {month} is {month_days[month]}.")
else:
    print("invalid")
