import xml.etree.ElementTree as etree
import sys
import urllib.parse
from unidecode import unidecode


raw_content = "".join(sys.stdin.readlines())
tree = etree.parse(raw_content)
root = tree.getroot()

for nome in [deputado.find('nome').text for deputado in root]:
    t=unidecode(nome.strip())
    t.encode("ascii")
    print(t)
