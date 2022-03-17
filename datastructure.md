{% include navigation.html %}

# Data Structures 

## [GitHub](https://github.com/PunarvasuS/DataStructures/)
## [Replit](https://replit.com/@DerrickHuang2)

### Code

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

