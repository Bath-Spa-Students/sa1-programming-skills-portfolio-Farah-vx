#searching specific string within the list
name = ["jake","zac","ian","ron","sam","dave"]
index = name.index("sam")
print(index)

#allowing the user to input the search
name = ["jake","zac","ian","ron","sam","dave"]
user = (input("enter the name your looking for: "))
if user in name:
    print(f"{user} is in the list!")
else:
    print(f"Oops {user} isnt in the list ;(. ")