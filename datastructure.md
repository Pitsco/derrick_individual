{% include navigation.html %}

# Data Structures 

## [GitHub](https://github.com/PunarvasuS/DataStructures/)
## [Replit](https://replit.com/@DerrickHuang2)

### Code TT0

Main.py

```
import animation

# Creates Title 
border = "=" * 40
banner = f"\n{border}\nWhat do you want to do with the list\n{border}"

def menu():
  print(banner)
  options = [
    ["tree", "tree.py"],
    ["animation", animation.ship],
  ]

  functions = {}
  functions[0] = ["Exit"] 
  for op in options:
    index = len(functions)
    functions[index] = op

  for key, value in functions.items():
    print(key, '->', value[0])

#  number = 1 
#  for thing in functions: 
#    print( str(number) + " " + str(thing)
#    number = int(number) + 1  

  choice = input("What function would you like: ")

  try: #try converting to integer
    #convert to number
    choice = int(choice)
    if choice == 0: #exit choice, stop loop
      return        #return means leave function
    try:  #try to run as playground function
      action = functions.get(choice)[1]
      exec(open(action).read())
    except:
      try:  #try to run as function
        action()
      except:
        print(f"Bad action: {action}")
      #end function try
    #end playground try
  except ValueError: #not a number error
    print(f"Not a number: {choice}")
  except: #traps all other errors
    print(f"Invalid choice: {choice}")

menu()
```

tree.py

```
def tree(x):
    print("\n".join([f"{'*'*(2* n + 1):^{2*x+1}}" for n in range(x)]))
def trunk(n):
      for i in range(n):
        for j in range(n-1):
            print('      ', end=' ')
        print('***')
tree(15)
trunk(3)
```

animation.ship

```
import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u""
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def ocean_print():
    # print ocean
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
    print(OCEAN_COLOR + "  " * 35)

# print ship with colors and leading spaces
def ship_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + " ░░░░░███████ ]▄▄▄▄▄▄▄▄ ")
    print(sp + "  ▂▄▅█████████▅▄▃▂   ")
    print(sp + " Il███████████████████]. ")
    print(sp + "  @@@@@@@@@@@@@@@@@@@ ")
    print(RESET_COLOR)

# ship function, iterface into this file
def ship():
  ocean_print()
  # loop control variables
  start = 0  # start at zero
  distance = 50  # how many times to repeat
  step = 2  # count by 2

  # loop purpose is to animate ship sailing
  for position in range(start, distance, step):
      ship_print(position)  # call to function with parameter
      time.sleep(.1)
```

matrix.py

```
matrix = ([1,2,3], [4,5,6], [7,8,9], [" ", 0, " "])

for x in matrix:
  for y in x:
    print(y, end = ' ')
  print()
```

### Code TT1

List Elements with embedded Dictionary
```
sub_menu = [
    ["Factors", None],
    ["GCD", None],
    ["LCM", None],
    ["Primes", None],
]

random_sub_menu = [
    ["Random1", None],
    ["Random2", None],
    ["Random3", None],
]
Lists_sub_menu = [
    ["Tester", tester],
    ["Factorial", tester2],
    ["Fibonacci", fibtester],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", submenu])
    menu_list.append(["Random", Random_submenu])
    menu_list.append(["Lists", Lists_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)
def Random_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, random_sub_menu)
def Lists_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, Lists_sub_menu)
def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

```

Recursion
```
def for_loop():
  for n in range(len(InfoDb)):
      print_data(n)

    
  # hack 2b: def while_loop(0)
# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
  while n < len(InfoDb):
      print_data(n)
      n += 1
  return

  # hack 2c : def recursive_loop(0)
# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
  if n < len(InfoDb):
      print_data(n)
      recursive_loop(n + 1)
  return # exit condition

def InfoDb_loops():
  print()
  print("For loop:")
  for_loop()
  print("While loop:")
  while_loop(0)  # requires initial index to start while
  print("Recursive loop:")
  recursive_loop(0)  # requires initial index to start recursion
  
# Factorial of a number using recursion
def recur_factorial(n):
  if n == 1 or n == 0:
    return 1
  else:
    num = n * recur_factorial(n-1)
    return num

# this is test driver or code that plays when executed directly, versus import which will not run these statements
def factorial():
  num = int(input("Enter a number for factorial: "))
  # check if the number is negative
  if num < 0:
      print("Sorry, factorial does not exist for negative numbers.")
  else:
      print("The factorial of", num, "is", recur_factorial(num))

# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input
```
Fibonacci
```
def fibonacci(n):  
  if n < 0:
    print("Please enter a positive integer")
  elif n == 0:
    return 0
  elif n == 1 or n == 2:
    return 1
  elif n > 20:
    print("That's too many numbers, don't input over 20")
  else:  
    return(fibonacci(n-1) + fibonacci(n-2))  

def output_fibonacci():
  # take input from the user  
  nterms = int(input("How many terms would you like? "))  
  # check if the number of terms is valid  
  if nterms <= 0:  
     print("The Fibonacci sequence does not exist for negative numbers.")  
  else:  
     print("Your sequence:")
     for i in range(nterms):
         print(fibonacci(i), end=" ")
  print()
```

### Code TT1

Factorial
```
class Factorial: 
  def __init__(self):
    self.factSeq = [0, 1]
    
  def __call__(self, n):
    if n < len(self.factSeq):
      return self.factSeq[n]
    else:
      num = n * self(n-1)
      return num

def OOP():
  num_input = int(input("Enter a number for factorial: "))
  factorial_of = Factorial()
  if num_input < 0:
      print("Sorry, factorial does not exist for negative numbers.")
  else:
      print("The factorial of", num_input, "is", factorial_of(num_input))
```
Square
```
num = float(input("Enter a number: "))
square = math.pow(num, 2.0)
# determines the square of given value
print("The square of a given number {0} = {1}".format(num, square))
# prints the square
```
