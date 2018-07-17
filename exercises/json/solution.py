'''
1) import the JSON file as a list of dictionaries (hint: use a package)

2) inspect the data
* how many quotes are there?
* how many quotes are by an Unknown author?

3) fetch a quote from Sigmund Freud. How many are there? Which one do you
    like best?

4) write your favorite quote to a text file:
    - title the file with the author's name
    - the rest should be pure text content constituted by the quote
    + wrap it in quotation marks and add the author in a new line below
'''

# ---- 1 ---- #
import json

# opening the file and getting the content into python
with open('quotes.json', 'r') as f:
    quotes = json.load(f)

print(type(quotes))  # it's a list!


# ---- 2 ---- #
# a) how many quotes?
print(len(quotes))  # 1640

# b) getting Unknown authors (using a listcomp)
unknown = [q for q in quotes if q['quoteAuthor'] == 'Unknown']
print(len(unknown))  # 97


# ---- 3 ---- #
freud = [q for q in quotes if q['quoteAuthor'] == 'Sigmund Freud']
for q in freud:
    print(q['quoteText'])

favorite = freud[0]['quoteText']
print(favorite)


# ---- 4 ---- #
filename = freud[0]['quoteAuthor'].split()[1]

with open(f"{filename}.txt", 'w') as f:
    f.write(f"{favorite}\n({freud[0]['quoteAuthor']})")
