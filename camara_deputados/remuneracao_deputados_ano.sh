#!/usr/bin/env bash

ANO=$1

cat data/deputados.txt | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}01 {} > data/deputados_inserts_${ANO}01.sql
cat data/deputados.txt | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}02 {} > data/deputados_inserts_${ANO}02.sql
cat data/deputados.txt | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}03 {} > data/deputados_inserts_${ANO}03.sql
cat data/deputados.txt | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}04 {} > data/deputados_inserts_${ANO}04.sql
cat data/deputados.txt | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}05 {} > data/deputados_inserts_${ANO}05.sql
cat data/deputados.txt | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}06 {} > data/deputados_inserts_${ANO}06.sql
cat data/deputados.txt | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}07 {} > data/deputados_inserts_${ANO}07.sql
cat data/deputados.txt | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}08 {} > data/deputados_inserts_${ANO}08.sql
cat data/deputados.txt | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}09 {} > data/deputados_inserts_${ANO}09.sql
cat data/deputados.txt | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}10 {} > data/deputados_inserts_${ANO}10.sql
cat data/deputados.txt | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}11 {} > data/deputados_inserts_${ANO}11.sql
cat data/deputados.txt | parallel -j 16 ./remuneracao_funcionario.sh ${ANO}12 {} > data/deputados_inserts_${ANO}12.sql
