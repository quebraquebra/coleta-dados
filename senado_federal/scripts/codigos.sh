#!/usr/bin/env bash

curl -s "http://www.senado.gov.br/transparencia/rh/servidores/nova_consulta.asp?fnome=&fvinculo=&fsituacao=&flotacao=&fcategoria=&fcargo=0&fsimbolo=&ffuncao=0&fadini=&fadfim=&fconsulta=ok&btnsubmit=Pesquisar" | python getCodigoSenado.py