from bs4 import BeautifulSoup
import sys
import io

def getCodigo(href):
	return href.split('detalhe.asp?fcodigo=')[1]

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

raw_content = "".join(input_stream)
soup = BeautifulSoup(raw_content, 'html.parser')


with open('../dados/codigos.txt', 'w', encoding="utf8") as codigos:
	tbody = soup.find('tbody')
	for a in tbody.find_all('a', href=True):
		codigos.write(getCodigo(a['href']))
		codigos.write('\n')

codigos.close()
