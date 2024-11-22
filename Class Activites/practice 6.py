#decision structures
sales = int(input("type sales:"))
bonus = 0
if sales > 6000:
     bonus = 300
else:
     bonus = 0
print ("your bonus is "+str(bonus))