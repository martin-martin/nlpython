# part 1 function definition
# with optional arguments - as discussed together
def format_name(first_name, last_name, middle_name=None):
    if middle_name:
        full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        full_name = f"{first_name.title()} {last_name.title()}"
    return full_name

# part 2 here is our 'database' - inconsistent formatting (e.g. web scraped)
classic_names = [
    {'First Name': 'JOHANN', 'Middle Name': 'Sebastian', 'Last Name': 'bach'},
    {'First Name': 'Wolfgang', 'Middle Name': 'Amadeus', 'Last Name': 'Mozart'},
    {'First Name': 'Ludwig', 'Middle Name': 'van', 'Last Name': 'Beethoven'},
    {'First Name': 'Giuseppe', 'Last Name': 'VERDI'},
    {'First Name': 'pyotr', 'Middle Name': 'Ilyich', 'Last Name': 'Tchaikovsky'},
    {'First Name': 'Frederic', 'Last Name': 'CHOPIN'},
    {'First Name': 'ANTONIO', 'Last Name': 'Vivaldi'},
    {'First Name': 'Giacomo', 'Last Name': 'Puccini'},
    {'First Name': 'George', 'Middle Name': 'Frideric', 'Last Name': 'handel'},
    {'First Name': 'igor', 'Last Name': 'Stravinsky'},
]

# # part 3 A - executing code logic from user input - we did this
# f_name = input("tell me your first name: ")
# l_name = input("tell me your last name: ")
# print(format_name(f_name, l_name))
# print()

# -------------------------------------------
# ---------------- YOUR TASK ----------------
# -------------------------------------------

# part 3 B - executing code logic from different input (same function)

'''
USING THE SAME FUNCTION THAT WE DEFINED ABOVE (which is also the same
one that we used to format names that we received from user input):
- write a loop that prints out all the names of the composers neatly
formatted.

'''
