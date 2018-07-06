# --------------------------------------------------
# ------- A DIP INTO DIFFERENT POSSIBILITIES -------
# --------------------------------------------------
# in the spirit of jumping ahead, and because you declared interest,
# here are a few other ways to solve the name formatting challenge
# using functions. we can discuss them in class (but this is a preview)


# ------- defining functions -------

# using map() and a lambda function
def format_name_args_1(*names):
    full_name = ' '.join(map(lambda x: x.title(), names))
    return full_name

# using a list comprehension
def format_name_args_2(*names):
    full_name = ' '.join([x.title() for x in names])
    return full_name

# using keyword arguments and dictionary unpacking - no return!
def format_name_kwargs_1(**kwnames):
    for name_type, name in kwnames.items():
        print(f"{name_type: <12}: {name.title()}")

# using keyword arguments and dictionary unpacking plus return
def format_name_kwargs_2(**kwnames):
    full_name = ''  # we start with an empty string
    for name_type, name in kwnames.items():
        full_name += f"{name.title()} "  # adding titlecased name + space
        print(f"{name_type: <12}: {name.title()}")
    return full_name.rstrip()  # need to get rid of that final whitespace


# ------- calling functions -------

print(format_name_args_1('joHann', 'seBasTian', 'BACH'))
print()
print(format_name_args_2('igor', 'stravinsky'))
print()
print(format_name_kwargs_1(first_name='giacomo',
                            last_name='pucini'))
print()
print(format_name_kwargs_2(first_name='wolferl',
                            middle_name='aMADEUS',
                            last_name='MozArt'))
