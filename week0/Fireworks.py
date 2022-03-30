import time, os, random

#colors - i only used some
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"

def clear():
  os.system('clear')

color_list=[red,green,yellow,magenta,cyan,bright_blue,bright_cyan,bright_green,bright_magenta,bright_red,bright_yellow] #a list of the colors


clear()#clears the console, just in case.

while True:#goes on forever
			for i in range(9): # a for loop, does the following below colon 9 times
				f_color = random.choice(color_list)# chooses a random color every sec. (i think its every sec)
				clear()#clears
				for line in range(len(open("frames/frame" + str(i + 1) ).readlines())):#this opens up your files, line in range, opens up everyline and the str(i + 1) is switching the frame to an animation. Remember, the print is when the animation happens, this is just telling it to prepare. The .readlines() is taking your file into an input and every line becomes an element. This is kinda hard to explain tbh. lol
					print(f_color+open("frames/frame" + str(i + 1) ).readlines()[line],end="")# This prints the animation, adding the colors and doing the animation. The .readlines() shows up again, and the [line] does the animation. Also, the ,end="" makes the animation NOT look funky. Without that, the animation indentation and everything will look wierd.
				time.sleep(0.1)#sleeps for 0.1 seconds
			time.sleep(0.5)#sleeps for 0.5 seconds
			clear()#clears the console.