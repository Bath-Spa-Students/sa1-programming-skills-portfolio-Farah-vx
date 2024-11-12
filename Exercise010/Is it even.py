#creating a program to test if a value is odd or even

#checking if its odd or even
def odd_even(num):

    if num % 2 == 0:
      return f"{num} is an even number."

    else:
        return f"{num} is an odd number."
    
#asking user for a number
def main():
    user = int(input("enter a number: "))

    result = odd_even(user)
    print(result)

if __name__ == "__main__":
    main()