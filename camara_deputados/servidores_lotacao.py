from bs4 import BeautifulSoup
import sys
from unidecode import unidecode


raw_content = "".join(sys.stdin.readlines())
soup = BeautifulSoup(raw_content, 'html.parser')

if soup.find(text='Nenhum resultado encontrado.'):
    exit()

for name in [tr.find_all('td')[1].text for tr in soup.find('table').find_all('tr')[1:]]:
    t=unidecode(name.strip())
    t.encode("ascii")
    print(t)
