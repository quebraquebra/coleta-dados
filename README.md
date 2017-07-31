# quebra-quebra-coleta
Repositório responsável pela coleta de dados.

## Tipos
* convert_html_to_csv.py: Esse script converte um arquivo com dados de remuneração de um servidor no formato .html em arquivo .csv. Caso haja alguma falha na conversão, então, a ID do servidor é salva em um arquivo de log;
* convert_dir_to_csv.py: Caso tenha diversos html's para diversos servidores, então, pode-se utilizar esse script para realizar essa conversão em todos html's contidos em um diretório. Os arquivos que tiverem a conversão realizada com sucesso, terão as suas informações salvas em um arquio .csv. As que apresentaram algum erro, terão os seus ID's salvo em um arquivo de log;
