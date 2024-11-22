#define the number of interations
for i in range (10):
#statement that gets repeated  
     print ("Hello")
 #creating nos in sequence
for i in range (10):
     print (i)
     #using any variable instead of i
for num in range (10):
     print (num)

#while loop
seat = 100 #initial no. of seats 
while seat > 0 : #seat still available?
     print("sell ticket")#tickets sold
     seat = seat - 1 #no. of seats updated

#loop practise
for i in range (3):
     print("First")
     print("Second")

#Comparison operators
print (5==5)#is 5 equal to 5?
print(5==7)#is 5 equal to 7?
print (5!=5)#is 5 different from 5?
print (5!=7)#is 5 different from 7?
print (5<=5)#is 5 less than or equal to 5?
print (5>=5)#is 5 greater than or eual to 5?

#if else statement practise
password = input ("enter password")
if password == "654321":
    print ("access grandted")
else:
    print ("access denied")

#mutable lists (changing their values after being created)
num = [4,8,9]
num[0] = 1
num[1] = 2
num[2] = 3
print (num)

#list using values in variables
name = "farah"
country = "uae"
age = "18"
info = [name,country,age]
print(info[0])
print(info[1])
print(info[2])

#lists using string indexing
pets = "cat"
print  (pets[0])
print  (pets[1])
print  (pets[2])

#practice slicing of list
animals=["cat","dog","bird","cow"]
print(animals[1:3])
print(animals[0:1])
print(animals[1:2])
print(animals[0:4])

#slicing by omitting the starting index
grocery=["flour","bread","milk","napkin","rice"]
print(grocery[:3])
print(grocery[:5])

#slicing by omitting the stopping index
grocery=["flour","bread","milk","napkin","rice"]
print(grocery[1:])
print(grocery[4:])

#negative indexing
grocery=["flour","bread","milk","napkin","rice"]
print(grocery[-2])
print(grocery[-4])
print(grocery[-1])#last element
print(grocery[-4:])
print(grocery[-4:-1])
print(grocery[:-4])

#multiple arguments using print () function
print("your seat:",4)
print("name:","farah")
print("online:", True)#boolean
print(2,"apples")
print(5*8)
print(True and False)

#printing mixed characters to specific upper or lower case characters & capitalizaton
print("WElCome To bAtHSpA".lower())
print("WElCome To bAtHSpA".upper())
print("WElCome To bAtHSpA".capitalize())

#find() function practise
print("bee". find("e"))

#no. of item in the list
movies=["avatar","titanic","avanger"]
print(len(movies))

#adding item to end of list 
movies=["avatar","titanic","avangers"]
movies.append("barbie")
print(movies)

#adding an element to specific pocition
movies=["avatar","titanic","avangers"]
movies.insert(1,"barbie")
print(movies)
print(movies[1])

#removing an item from the list 
movies=["avatar","titanic","avangers"]
movies.pop(1)
print(movies)
print(movies[1])

#using own function
def personal_greet():
  print("hello",name)
  print("have a great day")

personal_greet=("sarah")
personal_greet=("henry")

def greet(name="guest"):
  print("hello",name) 
  print("welcome")

greet()
greet("john")

#creating a program to test if a value is odd or even
#asking the user to input a number within (1-20)
user = int(input("enter a number from (1-20)"))

#checking if its odd or even
def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 != 0
    
if is_even(user):
     print(f"{user} is an even number:")

elif is_odd(user):
     print(f"{user} is an odd number:")

else:
     print("invalid input. Please enter a number between 1 to 20")


