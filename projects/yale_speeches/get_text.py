import os
from bs4 import BeautifulSoup


files = os.listdir('./pages')
# need to replace the "right single quote" character u2019 with a char
# that my terminal can handle to print!
# files = [f.replace('’', "'") for f in files]

# exercise file
# f = "Yale's Response to the DACA Announcement.html"

for f in files:
    with open(f"./pages/{f}", 'r') as fin:
        soup = BeautifulSoup(fin)

    # targeting the text part of the HTML document
    # this gives two items - one containing the date, and one the text
    div_list = soup.find_all('div', {'class': ['list-item', 'even']})
    # getting the date as a string
    time = div_list[0].text
    # getting the text as a list of p elements
    text_list = div_list[1].find_all('p')
    # fetching only the text from those p elements
    raw_text_list = [p.text for p in text_list]
    # creating a coherent string of all paragraphs, preserving the
    # paragraphs as newline characters
    text = '\n'.join(raw_text_list)

    # and then, writing it all to a new txt file
    with open(f'texts/{f[:-4]}.txt', 'w') as fout:
        fout.write(f'{time}\n\n')
        fout.write(text)
