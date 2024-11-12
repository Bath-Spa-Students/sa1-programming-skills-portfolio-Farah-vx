#correct password
password=12345

#asking the user to enter password
user=int(input("enter password:"))

#using while loop so it repeatedly asks for the password until the user enter the correct one .
while user!=password:
    print("incorrect password. try again.")
    user=int(input("enter the password:").strip())
    
if user==password:
    print("access granted!")
      