from sys import argv
script = argv
n = int (argv[1])



print(n)

if (n >= 0):
    print("The number is positive")

elif (n<0):
    print("the number is negative")

else:
    print("that entry isn't valid")
