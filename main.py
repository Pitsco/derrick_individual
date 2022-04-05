# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
import math
from week0 import Animation
from week1 import infoDb
from week2 import factorial

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
week0_list = [
    ["Swap", "week0/Swap.py"],
    ["Matrix", "week0/Matrix.py"], 
    ["Tree", "week0/Tree.py"],
    ["Animation", Animation.ship],
]

week1_list = [

  ["InfoDb Loops", infoDb.InfoDb_loops],
  ["Factorial", infoDb.factorial],
  ["Fibonacci", infoDb.output_fibonacci]
]

week2_list = [
    ["Factorial OOP", factorial.OOP],
    ["Square", "week2/square.py"], 
    ["Palindrome", "week2/palindrome.py"],
    ["Triangular", "week2/triangular.py"]
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
  print()
  title = "Function Menu" + banner
  menu_list = main_menu.copy()
  menu_list.append(["Static", week0_func])
  menu_list.append(["Lists", week1_func])
  menu_list.append(["Math", week2_func])
  buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()

def week0_func():
  title = "Week 0" + banner
  buildMenu(title, week0_list)
  
def week1_func():
  title = "Week 1" + banner
  buildMenu(title, week1_list)

def week2_func():
  title = "Week 2" + banner
  buildMenu(title, week2_list)


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

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Not callable {action}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()