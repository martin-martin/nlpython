'''
Create a function called 'americanize' that takes a string as argument,
transforms it into ALL CAPS, and then prints it as a subliminal part
of the american flag. E.g.:

|* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|
| * * * * * * * * *  OOOOOOOOOOOOOOOOOOOOOOOOO|
|* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|
| * * * * * * * * *  OOOOOOOOOOOOOOOOOOOOOOOOO|
|* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|
| * * * * * * * * *  OOOOOOOOOOOOOOOOOOOOOOOOO|
|* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|
|GOD SAVE THE QUEENOOOOOOOOOOOOOOOOOOOOOOOOOOO|
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|

The function should always return the name of your favorite US president.

'''

def americanize(text):
    # a length check to keep it good-looking.
    if len(text) > 45:
        print("please be concise. big is beautiful, but below 45 chars is top.")
        return
    # and now, addressing the flag design and IMPORTANT SPEECH
    patriot_text = text.upper()
    print(f"""|* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|
| * * * * * * * * *  OOOOOOOOOOOOOOOOOOOOOOOOO|
|* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|
| * * * * * * * * *  OOOOOOOOOOOOOOOOOOOOOOOOO|
|* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|
| * * * * * * * * *  OOOOOOOOOOOOOOOOOOOOOOOOO|
|* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|
|{patriot_text:O<45}|
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|
"""
)
    return "Barack Obama"

print(americanize("happy 4th of july all you americans!"))


