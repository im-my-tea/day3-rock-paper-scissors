import random

#coin = [ "Head", "Tail" ]
#print(random.choice(coin))

names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
pay = random.randint(0, len(names) - 1)
print(names[pay] + " is going to buy the meal today!")