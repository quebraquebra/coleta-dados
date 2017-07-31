from bs4 import BeautifulSoup
import decimal
import sys
from unidecode import unidecode

def fix_decimal(s):
    s = s.replace('-', '').replace('(', '').replace(')', '').strip()
    virgula = s.rfind(',')
    ponto = s.rfind('.')
    decimal_part = 0
    integer_part = 0
    if (virgula > ponto):
        decimal_part = s.split(',')[-1]
        integer_part = s.split(',')[0].replace('.', '')
    else:
        decimal_part = s.split('.')[-1]
        integer_part = s.split('.')[0].replace(',', '')
    return decimal.Decimal("%s.%s" % (integer_part, decimal_part))


raw_content = "".join(sys.stdin.readlines())
soup = BeautifulSoup(raw_content.replace('<tr">', '<tr>'), 'html.parser')

if soup.find('table') is None:
    exit()

vinculo = soup.find('table').find_all('td')[0].text.strip().split(':')[1]
vinculo = unidecode(vinculo)
vinculo = vinculo.encode("ascii")
cargo = soup.find('table').find_all('td')[2].text.strip().split(':')[1]
cargo = unidecode(cargo)
cargo = cargo.encode("ascii")

meses = {'Jan': 1, 'Fev': 2, 'Mar': 3, 'Abr': 4, 'Mai': '5', 'Jun': 6, 'Jul': 7, 'Ago': 8, 'Set': 9, 'Out': 10, 'Nov': 11, 'Dez': 12}
mes = meses[soup.find_all('legend')[0].find('span').text.split('-')[0].strip().split('/')[0]]
ano = soup.find_all('legend')[0].find('span').text.split('-')[0].strip().split('/')[1]
nome = soup.find('h3').text
nome = unidecode(nome)
nome = nome.encode("ascii")

(
    remuneracao_fixa,
    vantagens_pessoal,
    funcao_ou_cargo,
    gratificao_natalina,
    ferias,
    outras_remuneracoes,
    abono_permanencia,
    redutor_constitucional,
    contribucao_previdencia,
    imposto_renda,
    remuneracao_apos_descontos,
    outros_diarias,
    outros_auxilios,
    outros_vantagens
) = [fix_decimal(x.text) for x in soup.find_all('table')[1].find_all('td', class_='numerico')]

atributos = {
    'mes': mes,
    'ano': ano,
    'cargo': cargo,
    'vinculo': vinculo,
    'nome': nome,
    'remuneracao_fixa': remuneracao_fixa,
    'vantagens_pessoal': vantagens_pessoal,
    'remuneracao_eventual': funcao_ou_cargo + gratificao_natalina + ferias + outras_remuneracoes,
    'abono_permanencia': abono_permanencia,
    'descontos': redutor_constitucional + contribucao_previdencia + imposto_renda,
    'outros_diarias': outros_diarias,
    'outros_auxilios': outros_auxilios,
    'outros_vantagens': outros_vantagens
}

print("INSERT INTO folha_camara (mes, ano, cargo, vinculo, nome, remuneracao_fixa, vantagens_pessoais, remuneracao_eventual, abono_permanencia, descontos, outros_diarias, outros_auxilios, outros_vantagens) VALUES (%(mes)s, %(ano)s, \"%(cargo)s\", \"%(vinculo)s\", \"%(nome)s\", %(remuneracao_fixa)s, %(vantagens_pessoal)s, %(remuneracao_eventual)s, %(abono_permanencia)s, %(descontos)s, %(outros_diarias)s, %(outros_auxilios)s, %(outros_vantagens)s);" % atributos)