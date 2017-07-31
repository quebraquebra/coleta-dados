#!/usr/bin/env bash

lotacao=$1
count=1

while :
do
  index=$((($count - 1) * 20))
  html=`curl -s -X GET "http://www2.camara.leg.br/transparencia/recursos-humanos/servidores/lotacao/consulta-servidores/layouts_transpar_quadroremuner_consultaServidores?form.button.pesquisar=Pesquisar&letra=&b_start:int=${index}&lotacao=${lotacao}"`
  echo $html | python servidores_lotacao.py

  next_page=`echo $html | python next_page.py`
  if [ -z $next_page ]
  then
    break
  fi

  (( count++ ))
done
