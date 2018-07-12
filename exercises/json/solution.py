import json


# opening the file and getting the content into python
with open('quotes.json', 'r') as f:
    quotes = json.load(f)

print(type(quotes))
print(len(quotes))  # how many quotes?

# getting Unknown authors
unknown = []
for q in quotes:
    if q['quoteAuthor'] == 'Unknown':
        unknown.append(q)

print(len(unknown))

freud = [q for q in quotes if q['quoteAuthor'] == 'Sigmund Freud']
for q in quotes:
    if q['quoteAuthor'] == 'Sigmund Freud':
        print(q)

print(freud)
filename = freud[0]['quoteAuthor'].split()[1]
quote = freud[0]['quoteText']

with open(f"{filename}.txt", 'w') as f:
    f.write(f"{quote}\n({freud[0]['quoteAuthor']})")
