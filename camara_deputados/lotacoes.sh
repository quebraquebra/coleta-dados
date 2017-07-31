#!/usr/bin/env bash

curl -s http://www2.camara.leg.br/transparencia/recursos-humanos/servidores/lotacao/consulta-servidores/layouts_transpar_quadroremuner_consultaServidores | python lotacoes.py > data/lotacoes.txt
