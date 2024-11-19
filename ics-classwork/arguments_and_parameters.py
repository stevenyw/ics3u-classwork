def num_chairs(tables, chairs_per_table):
    chairs = tables * chairs_per_table
    print(f"You will need {chairs} chairs.")


num_chairs(4, 5)
# There's two arguments, 4 and 5.
# The name of the parameters are "tables" and "chairs_per_table"
# The output is 20
# If u add or remove one it breaks the code

def print_integer(n):
    print(n)
    
print_integer(5)

# Create a function that takes two integer arguments and prints out their difference. 
def difference(a, b):
    result = (a-b)
    print(result)
    
difference(5, 3)

# List the two things wrong with the following code and how to fix it.
def subtract(a, b):
    print(a - b)
  # There's only one parameter for a
  # The word "function" will not work, you need to use def

subtract(5, 7)

# How would you call the following function? Give two examples.
def activate_thrusters(percent_power):
    print(percent_power)

activate_thrusters(45)

def activate_thrusters(percent_power):
    print(percent_power)

a = int(input("give"))
activate_thrusters(a)

def person_apples(a, b):
    print(f"{a} will eat {b} apples.")
    
poop = input("Name")
cas = int(input("Apples amount"))
person_apples(poop, cas)
    
    
