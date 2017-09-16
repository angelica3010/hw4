#write a function that
def print_one():
    print("this is a call to function print_one")

def print_two():
    print("this is a call to print_two")

def activity (a, b):
    if (a > b):
        print (a / b)
        print_one()

    elif (b > a):
        c = a * 10
        print_two()
    else:
        print("both are the same")

activity(8,9)
activity(8,8)
activity(9,10)
