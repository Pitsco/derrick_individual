import math

try:
  layers = int(input("How many layers of the pyramid (enter an integer): "))
except:
    print("That\'s not an integer! Please run again.")
    exit()
star = "* "
x = 1
spaceNum = layers

print("Here's your tree")

while x <= layers:
  print((spaceNum * " ") + star)
  star += "* "
  spaceNum -= 1
  x += 1

print(" " * math.floor(layers/1.11) + "***")