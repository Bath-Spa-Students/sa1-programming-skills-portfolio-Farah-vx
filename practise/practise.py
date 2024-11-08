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

#slicing by omiting the starting index
grocery=["flour","bread","milk","napkin","rice"]
print(grocery[:3])
print(grocery[:5])