#Functions - Mini Scripts Inside .Py scripts
#you name a function, just like you our script takes
#an arguments
#inside a function is a code that does something just
#like the code inside the script
#function- a block of code that does a specific thing

name = 'Saroosh'
location = 'Bronx'

##function definition
def print_variables(name, location):
    print(f"Name is {name} \nLocation is {location}")

##function call
#a function needs to be called just like a .py scripts
print_variables(name, location)
print_variables('John', 'Manhattan')
