#!/usr/bin/env bash

PERIODO=$1
DEPUTADO=$2

FOLHA_URL=`curl -s "http://fagnerlima.pro.br/quebra-quebra/dep-links.php?periodoFolha=${PERIODO}&nome=${DEPUTADO}"`
curl -s $FOLHA_URL | python remuneracao_funcionario_sql_insert.py
