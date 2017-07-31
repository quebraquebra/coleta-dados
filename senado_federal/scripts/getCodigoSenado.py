from bs4 import BeautifulSoup
import sys

def getCodigo(href):
	return href.split('detalhe.asp?fcodigo=')[1]

raw_content = "".join(sys.stdin.readlines())
soup = BeautifulSoup(raw_content, 'html.parser')


with open('../dados/codigos.txt', 'w') as codigos:
	tbody = soup.find('tbody')
	for a in tbody.find_all('a', href=True):
		codigos.write(getCodigo(a['href']))
		codigos.write('\n')

codigos.close()
