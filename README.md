# Coleta-Dados
Repositório responsável pela coleta de dados.

## Crawler e scrapping dos dados da camara de deputados

Entrando na pasta `camara_deputados` você vai encontrar diferentes programas para acessar os dados da Câmara de Deputados.

### lotacoes.sh

Gera um arquivo data/lotacoes.txt que tem todas as lotações (departamentos) da Câmara.

### outro_servidores.sh

Gera um arquivo data/outros_servidores.txt com a lista de nomes de todos os servidores (não deputados) que trabalham na Câmara de deputados.

### remuneracao_deputados_ano.sh

Gera arquivos SQL com comandos INSERT INTO data/deputados_inserts_${ANO}${MES}.sql que contem todas as remunerações de todos os deputados durante um ano.

### remuneracao_funcionario.sh

Gera comandos SQL INSERT INTO das remunerações para um deputado num periodo especifico (YYYYMM).

### remuneracao_outros_servidores_ano.sh

Gera arquivos SQL com comandos INSERT INTO data/outros_inserts_${ANO}${MES} que contem todas as remunerações de todos os servidores (não deputados) durante um ano.

### servidores_lotacao.sh

Gera uma lista de nomes de servidores que trabalham numa especifica lotação da câmara.

### sqls_txt.py

Converte todos os dados baixados para um txt, que será usado na análise dos dados da câmara.

OBS: para gerar só os arquivos necessários na análise, basta executar `remuneracao_deputados_ano.sh` (remuneracao deputados) e `remuneracao_outros_servidores_ano.sh` (para outros servidores da camara). Além do `sqls_txt.py` para conseguir todos os dados unidos.

## Crawler e scrapping dos dados do senado federal

Entrado na pasta `senado_federal/scripts` você vai encontrar diferentes programas para acessar os dados do Senado Federal.

### codigo.sh

Gera um arquivo dados/codigos.txt contendo uma lista dos códigos de todos os servidores do Senado.

### remuneracao_servidores_senado_mes_ano.sh

Gera os htmls dos remunerações com base em um certo mês e ano.

Para tanto é preciso que o usuário faça o download do `dados/cookies.txt` daquele mês e ano específico na página do senado: 

* Adicionar a extensão de baixar cookies no [Mozilla](https://addons.mozilla.org/pt-BR/firefox/addon/export-cookies/?src=api) . Ou use esta extensão no [Google Chrome](https://chrome.google.com/webstore/detail/cookiestxt/njabckikapfpffapmjgojcnbfjonfjfg?utm_source=chrome-app-launcher-info-dialog)

* Entrar no site do [Senado](http://www.senado.gov.br/transparencia/rh/servidores/nova_consulta.asp)

* Selecionar um servidor qualquer

* Escolher a data para a qual quer obter os dados

* Colocar o captcha e clicar em mais informações

* Vá em Ferramentas, na barra superior do Mozilla, e clique em baixar cookies 
OBS: As informaçes que serão baixadas serão apenas do mês e ano do cookie que você baixou, ou seja, para baixar informaçes de outro mês e ano, você precisará baixar um novo cookie

* Após salvar o cookie na pasta dados, execute o remuneracao_servidores_senado_mes_ano.sh

### convert_dir_to_csv.py

Esse script converte um arquivo com dados de remuneração de um servidor no formato .html em arquivo .csv. Caso haja alguma falha na conversão, então, a ID do servidor é salva em um arquivo de log.

### convert_html_to_csv.py

* convert_dir_to_csv.py: Caso tenha diversos html's para diversos servidores para serem convertidos, então, pode-se utilizar esse script para realizar essa conversão em todos html's contidos em um diretório. Os arquivos que tiverem a conversão realizada com sucesso, terão as suas informações salvas em um arquio .csv. Os arquivos que apresentaram algum erro na conversão, terão os seus ID's salvo em um arquivo de log.

### crawler-senado-folha.php

* Script PHP para gerar scripts SQL para os inserts no banco de dados. Os arquivos gerados são separados por ano/mês.

> Para sua correta execução, os arquivos CSV que serão utilizados pelo script PHP deve estar em um diretório chamado **csv**. Crie também um diretório chamada **sql** que irá receber os scripts SQL. Ambos os diretórios devem ser criados no mesmo nível do script PHP.
