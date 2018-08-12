#######################################################################
# Interactive Tutorial 2: Python Basics
#######################################################################
# Comments beginning with "TODO" contain the tasks that you must
# complete in this interactive tutorial. Write your answers under each
# TODO. Use Find (Ctrl/Cmd + F) to keep track of them.
# 
# This is a Python file, not the interactive interpreter, so code won't
# run immediately when you write it. You also WON'T need the triple
# greater-than symbols (>>>) at the beginning of each line.
# 
# Just focus on writing Python to the best of your abilities! Once
# you're done, you'll have the chance to check your work in the next
# tutorial section, Running Python Code: https://bit.ly/2w3PbCX
#######################################################################

#######################################################################
# Don't touch this! This is for checking your code.
#######################################################################
from Python_Tests.save_prints import start, stop
from Python_Tests.tutorial_2 import check_all_todos

start()
#######################################################################

# TODO 1: Print Monroe's favorite food. Hint: rice and beans

print('Rice and beans')

# TODO 2: Calculate the volume of a 7 x 7 x 5 cube, then print the
# result.

volume = 7 ** 2 * 5
print(volume)

# TODO 3: Lists
# TODO 4: Dicts

# TODO 5: Write a conditional statement with 3 conditions: when x is 10, when x is 1, and when x is anything other than 1 or 10. For each condition, have your code print what the value is or isn't.

# TODO 6: Write a `for` loop that takes a variable with an initial value of 0, and adds the current index to the previous value of that variable (i.e. you variable should grow in size every iteration). Perform the iteration 20 times, and have the final value be printed at the end.

# TODO 7: Functions 

#######################################################################
# Don't touch this! This is for checking your code.
#######################################################################
printed_lines = stop()
check_all_todos(printed_lines)
#######################################################################