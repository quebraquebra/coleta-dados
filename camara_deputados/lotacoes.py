from bs4 import BeautifulSoup
import sys


raw_content = "".join(sys.stdin.readlines())
soup = BeautifulSoup(raw_content, 'html.parser')

for value in list(filter(None, [x['value'] for x in soup.find('select', id='lotacao').find_all('option')])):
    print(value)
