#this one is like your scripts with arg
# you tell python to make  a
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes no arguments
def print_none():
    print("I got nothin'.")

#you call the functions here vs in the past we would
#call the argv by doing from sys import argv and wait for
#someone to do an input
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

#this is snake case
#print_two
#this is camel case
#printTwoThree

#syntax for naming function
#def name ()

#return lets you save the result and use it later for something else like a
#global variable
