from bs4 import BeautifulSoup as bs
import requests # switching to requests pckg

url = 'https://president.yale.edu/speeches-writings/notes-woodbridge-hall'
x = requests.get(url)
html_page = x.text
soup = bs(html_page,'html.parser')
text = soup.find_all('a', {'class':'views-more-link'})
links = []
for link in text:
    links.append((link['href']))
fixed_links = []
for x in links:
    fixed_links.append('https://president.yale.edu' + x)
print(fixed_links)
counter = 0
urls = fixed_links
clean_ptags = []
for url in urls:
    x = requests.get(url)
    html_page = x.text
    soup = bs(html_page,'html.parser')
    ptags = soup.find_all('p')
    for paragraph in ptags:
        clean_ptags.append(paragraph.text)
    counter += 1

    all_text = ''
    for p in clean_ptags:
        all_text += p

    # all_text = ''.join(clean_ptags)

    with open(f'pres_speech_number_{counter}fix.txt', 'w') as fo:
        fo.write(all_text)
