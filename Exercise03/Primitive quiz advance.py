#recording capitals of 10 European countries.
capitals = {"Canada": "Ottawa",
"china": "Beijing",
"Egypt": "Cairo",
"France": "Paris",
"Germany": "Berlin",
"India": "New Delhi",
"New Zealand": "Wellington",
"Russia": "Moscow" ,
"united Kingdom": "London",
"United States of America": "Washington"}
for country, capital in capitals.items():
    answer = input (f"what is the capital of {country}?: ")
#Ensuring whether or not the answer is correct
    if answer.lower()==capital.lower():
        print("the answer is correct")
    else:
        print("the answer is incorrect")

    