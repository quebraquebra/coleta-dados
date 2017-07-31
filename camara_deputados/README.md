# Crawler e scrapping dos dados da camera de deputados

## lotacoes.sh

Gera um arquivo `data/lotacoes.txt` que tem todas as locatacoes (departamentos) da camera.

## outro_servidores.sh

Gera um arquivo `data/outros_servidores.txt` com a lista de nomes de todos os servidores (não deputados) que trabalham na camera de deputados.

## remuneracao_deputados_ano.sh

Gera arquivos SQL com comandos INSERT INTO `data/deputados_inserts_${ANO}${MES}.sql` que contem todas as remunerações de todos os deputados durante um ano.

## remuneracao_funcionario.sh

Gera comandos SQL INSERT INTO das remunerações para um deputado num periodo especifico (YYYYMM).

## remuneracao_outros_servidores_ano.sh

Gera arquivos SQL com comandos INSERT INTO `data/outros_inserts_${ANO}${MES}` que contem todas as remunerações de todos os servidores (não deputados) durante um ano.

## servidores_lotacao.sh

Gera uma lista de nomes de servidores que trabalham numa especifica lotação da camera.
