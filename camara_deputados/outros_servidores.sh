#!/usr/bin/env bash


cat data/lotacoes.txt | parallel -j 16 "./servidores_lotacao.sh {} > data/outros_servidores_lotacao_{}.txt"
cat data/outros_servidores_lotacao_{}.txt | sort | uniq > data/outros_servidores.txt
