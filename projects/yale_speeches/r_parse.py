from requests_html import HTMLSession


session = HTMLSession()

r = session.get('https://www.udacity.com')

print(r.html.text)
