#write comments

#step1: make the function by defining it and passing in arugmetns

def cheese_and_crackers(cheese_count, boxes_of_crackers):

#step 2: Write the print results of the arguments
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Man that's enough for a party!")
    print(f"Get a blanket. \n")

#step3: pass in arguments and print the result
print("We just give the function numbers directly:")
cheese_and_crackers(20,30)

#step4: define the variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

#step5: call the function this time with the variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#step6: print out the result
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
