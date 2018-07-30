from bs4 import BeautifulSoup
import requests

# fetching the links from the output files
sources = ['yalescrape/output/statements-links.tsv',
            'yalescrape/output/speeches-links.tsv']

link_list =[]  # making a container for the data
for page in sources:
    with open(page, 'r') as f:
        for line in f.readlines():
            # they are TSV files (tab-separated) to avoid conflicts
            # with titles that contain commas!
            # so we gotta split on the tab character \t
            line = line.rstrip().split('\t')
            # adding lists of ['<link_title>', '<http_link>'] to the master list
            link_list.append(line)

# now we'll work with those links to fetch the HTML pages from the web
for link in link_list:
    title = link[0]
    # the actual link is in position [1] of each list, so that's what
    # we call the requests.get() method on
    # this creates a Requests object that you can work with in bs4
    req = requests.get(link[1])
    with open(f"pages/{title}.html", 'w') as f:
        f.write(req.text)  # saving the page to file (not necessary) (but you can run it for fun ;)

        # ----------- HERE COMES THE PARSING ------------

        # create and parse a BeautifulSoup() object
        # in order to extract only the text data of the article
