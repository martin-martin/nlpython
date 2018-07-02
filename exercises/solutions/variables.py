# ------------------------------------------
# ------------ PYTHON VARIABLES ------------
# ------------------------------------------

# define a valid variable in python, then print() it out
hello = "hello"
print(hello)

# define three variables that are *not allowed* by the naming conventions
# 1 = 1
# 1var = 1
# r33l* = 2

# try defining a variable called 'try' - why does it not work?
# try = 42

# check all reseved keywords that can't be used as var names
import keyword
print(keyword.kwlist)

Var = 1  # this throws no error - why not? why not use it?

# define two variables in one line
# when is this useful? why should it be otherwise avoided?
one, two = 1, 2
# Note the difference to:
three = 1, 2
print(type(one), type(three), len(three))  # len(one) throws error

# reassign a variable - assign 'hello' to a different value
hello = "byebye"
print(hello)


# use input() to ask for user input - - assign it to a variable
fahrenheit = input("enter a temperature in fahrenheit: ")
celsius = (fahrenheit - 32) / 1.8
print(celsius)

# CHALLENGE: convert the above code into a function


# LINK: how to use markdown
# https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
# more resources: https://gist.github.com/JosefJezek/5917040
