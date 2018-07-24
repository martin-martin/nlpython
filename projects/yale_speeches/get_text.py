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

    div_list = soup.find_all('div', {'class': ['list-item', 'even']})
    time = div_list[0].text
    text_list = div_list[1].find_all('p')

    raw_text_list = [p.text for p in text_list]
    text = '\n'.join(raw_text_list)

    with open(f'texts/{f[:-4]}.txt', 'w') as fout:
        fout.write(f'{time}\n\n')
        fout.write(text)
