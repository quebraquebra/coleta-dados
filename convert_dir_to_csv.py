#coding=utf-8
import os
import sys
		
'''
#################################################################################
# Funcao 'main'
# Esse script recebe um diretório contendo diversos htmls com informações de
# remuneração de diversos servidores e processa cada um deles, armazenando as
# informações de remuneração em um arquivo no formato .csv, para aqueles servidores
# que obteve sucesso na coleta de dados. Caso haja algum erro, a ID do usuário será
# salva em um arquivo de log 
#################################################################################
'''
if __name__ == '__main__':
	############################################################
	#O usuário deverá chamar este script fornecendo os seguintes parâmetros:
	#	* diretorio_de_htmls: Diretório contendo diversos html para
	# diferentes servidores 
	#	* nome_arquivo_saida: Nome do arquivo onde serão salvas as informações
	# de remuneração dos servidores que estão no diretorio_de_htmls, esse arquivo
	# terá formato .csv
	#	# arquivo_de_log_id: Nesse arquivo serão salvas as ID dos usuários que
	# por alguma razão apresentou falha na conversão do html em csv
	############################################################
	if len(sys.argv) == 4:
		diretorio_de_htmls = sys.argv[1]
		nome_arquivo_saida = sys.argv[2]
		arquivo_de_log_id = sys.argv[3]
	else:
		print("Você deve chamar: %s [diretorio_entrada] [csv_saida] [log_id]" % (sys.argv[0]))
		sys.exit()

	todos_arquivos = os.listdir(diretorio_de_htmls)
	print diretorio_de_htmls
	
	for nome_arquivo in todos_arquivos:
		nome_do_arquivo = str("%s/%s" % (diretorio_de_htmls, nome_arquivo))
		command = ("python convert_html_to_csv.py \"%s\" %s %s" % (nome_do_arquivo, nome_arquivo_saida, arquivo_de_log_id))
		os.system(command)
	
	sys.exit()
