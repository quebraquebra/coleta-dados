#!/usr/bin/env bash

ANO=$1

cat data/outros_servidores.txt | python url_encode.py | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}01 {} > data/outros_inserts_${ANO}01.sql
cat data/outros_servidores.txt | python url_encode.py | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}02 {} > data/outros_inserts_${ANO}02.sql
cat data/outros_servidores.txt | python url_encode.py | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}03 {} > data/outros_inserts_${ANO}03.sql
cat data/outros_servidores.txt | python url_encode.py | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}04 {} > data/outros_inserts_${ANO}04.sql
cat data/outros_servidores.txt | python url_encode.py | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}05 {} > data/outros_inserts_${ANO}05.sql
cat data/outros_servidores.txt | python url_encode.py | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}06 {} > data/outros_inserts_${ANO}06.sql
cat data/outros_servidores.txt | python url_encode.py | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}07 {} > data/outros_inserts_${ANO}07.sql
cat data/outros_servidores.txt | python url_encode.py | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}08 {} > data/outros_inserts_${ANO}08.sql
cat data/outros_servidores.txt | python url_encode.py | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}09 {} > data/outros_inserts_${ANO}09.sql
cat data/outros_servidores.txt | python url_encode.py | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}10 {} > data/outros_inserts_${ANO}10.sql
cat data/outros_servidores.txt | python url_encode.py | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}11 {} > data/outros_inserts_${ANO}11.sql
cat data/outros_servidores.txt | python url_encode.py | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}12 {} > data/outros_inserts_${ANO}12.sql
