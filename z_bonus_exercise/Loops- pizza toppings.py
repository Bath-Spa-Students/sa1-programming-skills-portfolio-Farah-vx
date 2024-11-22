#creating a loop so the user can enter a series of pizza toppings until they enter 'quit'
while True:
    pizza_topping = input("enter pizza topping (or enter 'quit' to finish): ")

#using 'if' statement ti check if the user wants to quit
    if pizza_topping.lower() == 'quit':
       break
    else:
       print(f"I'll add {pizza_topping} to your pizza.")