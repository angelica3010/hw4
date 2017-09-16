#Write a function that takes 2 arguments and if argument 1
#is greater than argument 2, divide the 1st argument by 2nd
# if argument 2 is greater than argument 1, mulitply argument 1,
#by 10 call function 3 times with different values

from sys import argv
script = argv
#n = int (argv[1])

#print(n)

def here (arg1, arg2):
    if (arg1 > arg2):
        return (arg1 / arg2)

    elif  (arg1 < arg2):
        return (arg1 * 10)
    else:
        print ("the number is the same")

result1 = here (1,2)
print (result1,  "here is the result")


result2 = here (4, 5)
print (result2,  "here is the result")

result3 = here (20, 10)
print (result3,  "here is the result")
