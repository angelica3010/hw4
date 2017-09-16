#check the ranges for a number

from sys import argv
script = argv
n = int (argv[1])

print(n)

if (6 <= n <= 12):
    print ("The number is in the range of 6 to 12")

elif (121 <= n <= 151):
    print ("The number is in the range of 121 to 151")

else:
    print ("The number is not in any of these ranges")
