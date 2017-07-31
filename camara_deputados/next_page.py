from bs4 import BeautifulSoup
import sys


raw_content = "".join(sys.stdin.readlines())
soup = BeautifulSoup(raw_content, 'html.parser')

if soup.find('ul', class_='pagination') is None or soup.find('ul', class_='pagination').find('li', class_='next') is None:
    exit()

print(soup.find('ul', class_='pagination').find('li', class_='next').find('a')['href'])
