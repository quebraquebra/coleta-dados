## Sobre

Não é segredo que a folha de pagamento da Câmara de Deputados e Senado do Brasil está entre as mais caras do mundo. As duas casas juntas tem orçamento previsto de R$ 10,2 bilhões para 2017 o que equivale a R$ 28 milhões por dia! Além de salários e benefícios generosos, nossos parlamentares também contam com um número generoso de assessores e funcionários. A Câmara, por exemplo, além de seus 513 deputados, possui cerca de 16 mil funcionários efetivos e comissionados que representam 81% do orçamento.

O problema é que se quisermos acessar informações sobre a remuneração de servidores dessas duas casas esbarraremos em diversas dificuldades. No site do Senado, por exemplo, precisamos primeiro passar os nomes específicos dos servidores, um a um, e depois digitar um captcha bem difícil de decifrar para que a consulta seja realizada. Além disso, não temos como ver ou baixar os dados da folha referentes a um dado período ou cargo, por exemplo.

Entendendo que o cidadão tem direito constitucional a essas informações, garantido pela Lei de Acesso à Informação, decidimos tornar mais fácil o acesso a esses dados. Desenvolvemos programas coletores para baixar os dados da folha de pagamento da Câmara e Senado de 2012 à 2017. Esses dados agora estão facilmente disponíveis por meio da API de acesso que desenvolvemos. Além disso, desenvolvemos uma interface de consulta de remunerações dessas duas casas que resolve os problemas atuais de acesso acima mencionados. Por último, criamos um blog com várias análises de dados das folhas da Câmara e Senado. Esse blog poderá no futuro ser alimentado por outras pessoas interessadas que queiram contribuir com a promoção da transparência desses dados.

É essencial termos todas as remunerações abertas (e não uma a uma) para uma análise mais aprofundada da estrutura de cargos e salários para eventuais correções. Os cidadãos, que pagam os salários, têm o direito de saber quanto ganham os seus empregados.

Os dados estão disponíveis no [GitHub do projeto](https://github.com/quebraquebra).

## Repositórios

Os repositórios mais importantes para instalação e uso da nossa aplicação são:

1. coleta-dados: Repositório contendo scripts para coleta dos dados da folha da Câmara/Senado.
2. ap: Repositório contendo o código da api que desenvolvemos para acesso dos dados da Câmara e Senado.
3. webapp: Repositório contendo o código do site principal da aplicação.
4. blog: Repositório com as análises realizadas em cima dos dados coletados. Note que esse blog é independente do site principal. Sendo assim, não há dependência entre eles.

## Sustentabilidade

Há basicamente dois gatilhos que precisam ser acionados de tempos em tempos para garantir a sustentabilidade do projeto: a atualização dos dados e a inclusão de novas análises sobre esses dados. Para a atualização dos dados basta que os scripts criados neste projeto sejam executados mensalmente (assumindo que a estrutura atual dos sites da [Câmara](http://www2.camara.leg.br/transpnet/consulta) e [Senado](http://www.senado.gov.br/transparencia/rh/servidores/nova_consulta.asp) de onde coletamos os dados não mude). Em relação às análises, nós criamos um blog com várias análises já postadas pela equipe. A ideia é que qualquer pessoa interessada possa fazer um fork no projeto e fazer pull requests com suas próprias análises para serem incluídas no blog. Estaremos com certeza bastante receptivos a isso. 

## Inovação e Criativadade

O mecanismo criado para ultrapassar as barreiras impostas pela Câmara e Senado para o acesso à informação envolveu engenharia e criatividade. Além disso, as análises realizadas são inéditas trazendo informaçes também inéditas, dada a, até então, dificuldade em obter esses dados de forma irrestrita e consolidada. Perguntas como: quem são os servidores/cargos mais caros ou quanto custa os assessores de um senador estão finalmente sendo respondidas.

## Potencial de Impacto

A partir do momento que podemos aumentar a transparência sobre os salários de nossos representantes, empoderamos a população para que esta ajude não só na fiscalização, mas mais imporrante, na cobrança por uma redução da desigualdade entre os salários dos servidores da Câmara/Senado e o restante do Brasil. 
