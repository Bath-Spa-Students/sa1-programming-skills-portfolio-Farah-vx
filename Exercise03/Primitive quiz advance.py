#recording capitals of 10 European countries.
capitals = {"Italy": "Rome",
"Spain": "Madrid",
"Switzerland": "Bern",
"France": "Paris",
"Germany": "Berlin",
"Greece": "Athens",
"Austria": "Vienna",
"Russia": "Moscow" ,
"united Kingdom": "London",
"Finland": "Helsinki"}
for country, capital in capitals.items():
    answer = input (f"what is the capital of {country}?: ")
#Ensuring whether or not the answer is correct
    if answer.lower()==capital.lower():
        print("the answer is correct")
    else:
        print("the answer is incorrect")

    