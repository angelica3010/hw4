#Step 1: Define your variables
people = 30
cars = 40
trucks = 15

#Step2: Write your if/else statements

if cars > people:
    print("We should take the cars.")

elif cars < people:
    print("We shold not take the cars.")
else:
    print("We cant't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
