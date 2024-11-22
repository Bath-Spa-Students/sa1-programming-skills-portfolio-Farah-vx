#creating function
def greet ():
    print ('hello')
#calling the function
greet()

#local variable
def greet ():
    result = "hello"
    print(result)

#calling the function
greet()

#different functions with same local variable
def greet ():
    result='hello'
    print (result)

def greet_2():
    result="bye"
    print (result)

greet()
greet_2()

#passing argument variable

def greet_2(result):
    print(result)

text='wake up'
greet_2(text)

#ex parameter x store value and get double 
def main():
    value= 10
    double(value)

def double(x):
    print(x*4)

main()
