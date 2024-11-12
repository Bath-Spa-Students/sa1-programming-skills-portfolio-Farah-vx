#correct password
password=12345
#setting up max password attempts
max_attempts=5
attempts=0 #this is to track the no. of attempts

#asking for the password until there are no attempts left
while attempts < max_attempts:
    user=int(input("enter password:"))

    if user == password:
        print("access granted!")
        break
    else:
        attempts += 1 # attempts counter
        attempts_remaining = max_attempts-attempts
        if attempts_remaining > 0:
            print(f"Incorrect password. Remaining Attempts {attempts_remaining}.")
        else:
            print("incorrect password. authorities have been alerted!.".upper())