read -p "Digite o mês (ex: 01): " MES
read -p "Digite o ano (ex: 2017): " ANO

mywget() {
    wget -O ../dados/html/remuneracao$3$2_$1 "http://www.senado.gov.br/transparencia/rh/servidores/remuneracao.asp?fcodigo=$1&fvinculo=&mes=01/$2/$3" --load-cookies=../dados/cookies.txt;
}


export -f mywget
parallel mywget :::: ../dados/codigos.txt ::: ${MES} ::: ${ANO}
