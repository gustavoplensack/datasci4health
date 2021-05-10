# Projeto _"Um estudo sobre a relação entre isolamento social e indicadores sócio-econômicos durante o período da pandemia da COVID-19 no Brasil."_

# Project _"A study on the relationship between social isolation and socio-economic indicators during the pandemic period of COVID-19 in Brazil."_

# Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação [Ciência e Visualização de Dados em Saúde](https://github.com/datasci4health/home), oferecida no primeiro semestre de 2021, na Unicamp.

## Integrantes

|              Nome             	|   RA   	|                        Especialização                        	|
|:-----------------------------:	|:------:	|:------------------------------------------------------------:	|
| Aline Liz de Faria            	| 226606 	| Nutricionista aluna especial                                 	|
| Carolina Neves Freiria        	| 101825 	| Nutricionista - Doutoranda em gerontologia FCM               	|
| Flavia Noeli de Souza Infante 	| 100061 	| Nutricionista - Doutoranda Saúde da Criança e do adolescente 	|
| Gustavo G. Plensack           	| 155662 	| Engenharia Elétrica - Aluno especial                         	|

# Descrição Resumida do Projeto
A pandemia do COVID-19 é um acontecimento sem precedentes na história recente da humanidade e seus impactos chegaram a todos os setores da sociedade. Como forma de mitigar a crise sanitária, uma das medidas mais eficazes se mostrou ser o distanciamento social.

No entanto, é fato que esta prática traz impactos grandes sobre a economia, em especial em países emergentes como o Brasil. Este estudo se propõe a investigar as relações entre o isolamento social praticado no estado de São Paulo e indicadores econômicos como desemprego, informalidade e inflação. 

🎥 [Apresentação do Projeto](https://drive.google.com/file/d/1r17x60hF7Gx_e8v6M-6V-O7QfEi8iRQL/view?usp=sharing)

# Perguntas de Pesquisa
Qual a relação entre isolamento social e indicadores sócio-econômicos durante a pandemia da COVID-19 no estado de São Paulo?

## Hipóteses (10/04/2021):
**H1:** Num primeiro momento, o isolamento social leva ao aumento do desemprego;

**H2:** Num segundo momento, o aumento do desemprego leva à diminuição do isolamento social;

**H3:** Fatores como o aumento da Inflação, redução do PIB per Capita levam à redução do isolamento social;

**H4:** Políticas públicas, como o auxílio emergencial favorecem o isolamento social.

# Bases de Dados e Evolução

## Bases de Estudadas mas Não Adotadas

### Mapa brasileiro da COVID-19 - InLoco

|             Base de Dados            |                 Endereço na Web                 |                                      Resumo descritivo                                     |
|:------------------------------------:|:-----------------------------------------------:|:------------------------------------------------------------------------------------------:|
| Mapa brasileiro da COVID-19 - InLoco | https://mapabrasileirodacovid.inloco.com.br/pt/ | Dados de abrangência nacional sobre isolamento social coletado através de apps de celular. |

A Inloco é uma startup de Recife especialista em geolocalização (atuante desde 2011). Para criar o “Índice de isolamento social” a Inloco utilizou dados celulares de 60 milhões de usuários. Por meio da API (Application Programming Interface) de aproximadamente 600 aplicativos (desde aplicativos de bancos até lojas de varejo) parceiros da empresa que anonimiza e agrega os dados e então repassa aos estados parceiros. A Inloco coletava, até então, estes dados de geolocalização para fins de publicidade e prevenção de fraudes. Durante a pandemia estes dados foram utilizados para avaliar o isolamento social. 

A empresa calcula a taxa de isolamento a partir de um espaço que é dividido em polígonos de 450 metros de raio. A taxa de isolamento mede, do total de aparelhos que estavam no polígono durante a noite, quantos não mudaram de polígono ao longo do dia. A taxa de precisão é de 3 metros.

Para essa análise ser estatisticamente relevante, são disponibilizados os dados de isolamento apenas no caso de haver um número mínimo de 20 usuários observados dentro das microrregiões. Se um município não tiver nenhuma microrregião que atenda a esse filtro, ele é desconsiderado e será eliminado  na composição do Índice de Isolamento do Estado.

Durante o segundo semestre de 2020, a empresa Inloco foi vendida para a rede Magazine Luiza e a coleta de dados foi descontinuada no início de 2021. Os dados coletados durante o ano de 2020 e início de 2021 ficarão disponíveis Tableau Public. Foram coletados dados durante o período de fevereiro de 2020 até março de 2021. 

Após a reunião com a professora Thaís na E1 o grupo acatou a sugestão de trabalhar com dados em menores proporções e limitamos o trabalho ao estado de São Paulo o que nos permitiu descartar este conjunto de dados. Outros motivos para não escolhermos os dados do Inloco foi a descontinuidade da coleta a partir do final de março de 2021 e fato de terem sido coletados por meio de apps específicos

## Bases Estudadas e Adotadas

### Dados de Isolamento Social do Estado de São Paulo - IPT

|                      Base de Dados                      |                    Endereço na Web                    |                                  Resumo descritivo                                 |
|:-------------------------------------------------------:|:-----------------------------------------------------:|:----------------------------------------------------------------------------------:|
| Dados de Isolamento Social do Estado de São Paulo - IPT | https://www.saopaulo.sp.gov.br/coronavirus/isolamento | Dados sobre o isolamento social em cidades paulistas com mais de 50 mil habitantes |

O IPT juntamente com o SIMI-SP (Sistema de Informações e Monitoramento Inteligente do Governo do Estado de São Paulo) divulga, diariamente, dados sobre o isolamento social nas cidades do estado de São Paulo. Os dados sobre isolamento social são coletados a partir de empresas prestadores de serviços de telecomunicação (telefonia celular – VIVO, TIM, CLARO, OI). Tais dados são obtidos a partir de uma plataforma chamada Big Data que é gerida pela Associação Brasileira de Recursos em Telecomunicações (ABR Telecom).

O índice de isolamento social é baseado na localização obtida pelas antenas de celulares, usando como local de referência a localização onde o celular permaneceu dentre 22h00 e 2h00. Um celular que tenha se afastado desta referência, mais que 200m, é considerado fora do isolamento. 

Os dados são repassados de forma anônima e agregada índices, gráficos e mapas estaduais agregados por municípios, não existindo a possibilidade de acesso a qualquer dado individualizado por parte do IPT ou do Governo do Estado.

No início da coleta dos dados (início da pandemia) eram repassados apenas dados de municípios que possuíam mais de 70.000 habitantes, no entanto, a partir de janeiro de 2021 foram incluídos municípios com mais de 50.000 habitantes. Os índices são disponibilizados de maneira pública no [site do estado](http://saopaulo.sp.gov.br/coronavirus/isolamento) e são atualizados diariamente.

O esquema do banco é uma série temporal com o isolamento naquele dia para um dado município. Também são encontrados alguns metadados como a população em 2020 e código do IBGE.

Explorando os dados, observamos dados faltantes nas primeiras 15 amostras da série e alguns poucos no meio da série. Diante disso, removemos os 15 primeiros dias de coleta e interpolamos linearmente os demais dias.

Uma análise inicial sobre estes dados permitiu notar que para as 20 cidades mais populosas do estado a série de isolamento apresenta uma alta correlação. Ao longo de todo o período, o isolamento ficou entre 30% e 50% sendo um pouco maior nos finais de semana. Detalhes, gráficos e código podem ser verificados em `notebooks/Estudo_IPT_E2.ipynb`

### PNAD contínua - Macrodados

|          Base de Dados          |                                                                      Endereço na Web                                                                      |                                                       Resumo descritivo                                                      |
|:-------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| Macrodados PNAD Contínua - IBGE | https://www.ibge.gov.br/estatisticas/sociais/trabalho/9173-pesquisa-nacional-por-amostra-de-domicilios-continua-trimestral.html?edicao=30227&t=resultados | Acompanhamento do desenvolvimento socioeconômico do país, apresentando dados referente a força de trabalho formal e informal |

A Pesquisa Nacional por Amostras de Domicílios (PNAD) em sua forma contínua teve início em 2012 com a junção da PNAD antiga e a Pesquisa Mensal de Emprego (PME) sendo realizada pelo Instituto Brasileiro de Geografia e Estatística (IBGE). A pesquisa tem abrangência nacional possibilitando inferências sobre o país, grandes regiões, unidades da federação e de algumas regiões metropolitanas dos municípios das capitais (SULIANO, 2017; IBGE, s/da).

O grande foco da PNAD é o acompanhamento do desenvolvimento socioeconômico do país, apresentando dados referente a força de trabalho tanto formal como informal de forma mensal (país) e trimestral (demais subdivisões), contemplando outras informações relevantes de forma anual, sendo para tanto considerada uma das principais pesquisas sobre o mercado de trabalho do Brasil (SULIANO, 2017; IBGE, s/da; CONSEUIL, et al., 2019). 

A pesquisa é realizada em 3.500 municípios do Brasil, acompanhando em média 211.344 domicílios particulares permanentes, na qual, cada um dos domicílios é visitado por 5 trimestres consecutivos. Durante o período da pandemia pelo coronavírus as entrevistas estão sendo realizadas via telefone (início na terceira semana de referência do mês de março de 2020) (SULIANO, 2017; IBGE, s/da; IPEA, 2019).

O acesso ao banco de dados é aberto e fica localizado no próprio site do IBGE. No site é possível o acesso rápido às informações mensais do país e aos dados trimestrais das regiões e unidades da federação. Para as análises referentes às regiões metropolitanas dos municípios das capitais é necessário o acesso aos microdados da pesquisa (IBGE, s/da).

Durante a pandemia também foi lançada a PNAD COVID-19 que acompanhou 193,6 mil domicílios em 3.364 municípios do país com o objetivo de avaliar os impactos da pandemia no mercado de trabalho. Teve seu início em maio de 2020 e foi descontinuada em setembro do mesmo ano. Por este motivo, visando atender aos objetivos estabelecidos neste projeto de pesquisa, optou-se pela análise apenas da PNAD contínua que abrange um período maior de estudo. Além disso, a PNAD covid-19, segundo o próprio IBGE, pode fornecer estatísticas experimentais na quais as inferências realizadas a partir dos dados devem ser realizadas com maior cautela (IBGE, s/db). 
 
**Sobre os dados utilizados da PNAD contínua**

Após a primeira arguição de nosso projeto com a professora Thaís, optou-se por focar apenas no banco de dados referente ao estado de São Paulo. Pelo site do IBGE foi possível baixar o banco de dados brutos do estado, com 112 tabelas contendo informações sobre a população geral, força de trabalho e  rendimentos obtidos entre o período de janeiro de 2012 a dezembro de 2020. 

Inicialmente foi realizado um recorte temporal do banco, considerando o último trimestre pré-pandemia (outubro/dezembro 2019) e o período referente a pandemia de covid-19 no país (considerando os trimestres de janeiro/março a outubro/dezembro de 2020). Após, foram coletadas as informações referentes a população total; população com mais de 14 anos de idade; pessoas de 14 anos ou mais de idade ocupadas; pessoas de 14 anos ou mais de idade desocupadas e pessoas de 14 anos ou mais de idade fora da força de trabalho. A seleção destas informações foi realizada para o estabelecimento de um panorama acerca da situação de pessoas empregadas, desempregadas e que estavam fora da força de trabalho (não estavam em busca de emprego) durante o período da pandemia.

**Análise descritiva dos dados**

Durante o período selecionado a pesquisa contou com uma média de população total de 46 mil pessoas, sendo que destas, aproximadamente 38,5 mil apresentavam 14 anos ou mais de idade. O gráfico abaixo contém as informações sobre a população de pessoas de 14 anos ou mais de idade ocupadas, desocupadas e fora da força de trabalho no estado de São Paulo entre o período analisado.

![ Evolução do número de pessoas desocupadas, ocupadas e fora da força de trabalho no estado de São Paulo de outubro de 2019 a dezembro de 2020.](./assets/PNAD.png)

Gráfico 1 - Evolução do número de pessoas desocupadas, ocupadas e fora da força de trabalho no estado de São Paulo de outubro de 2019 a dezembro de 2020. 


Podemos perceber pelo gráfico que entre o primeiro e segundo trimestre houve uma leve redução no número de pessoas ocupadas no estado, sendo a queda mais acentuada observada entre o segundo e terceiro trimestre, esboçando uma recuperação apenas entre o quarto e quinto trimestre. Em contraste, o nível de desocupados apresentou-se de maneira inversa: com grande aumento entre o segundo e terceiro trimestre, um aumento menos acentuado entre o terceiro  e quarto trimestre e uma leve queda entre o quarto e último trimestre.

Por fim, o nível de pessoas fora da força de trabalho manteve-se estável ao longo do período acompanhado, apresentando um leve aumento durante os três últimos trimestres, o que poderia ser um reflexo da diminuição de pessoas procurando emprego com receio da pandemia. 

Não foi necessário lidar com dados faltantes.

# Metodologia
O projeto de pesquisa usará o modelo _KDDM_ seguindo a metodologia de [1] dividida em 9 passos:

1. Desenvolvimento do projeto e entendimento do problema; 
2. Criação de conjunto de dados alvo;
3. Limpeza dos dados e Pré-processamento;
4. Redução dos dados e Projeções;
5. Escolha da tarefa de mineração de dados;
6. Escolha do algoritmo para análise dos dados;
7. Mineração dos dados;
8. Interpretação dos dados;
9. Consolidação do conhecimento;

Para execução desta metodologia, esperamos empregar as seguintes técnicas de mineração de dados: análises estatísticas, análise de redes, técnicas de regressão e classificação.

# Ferramentas

As ferramentas que serão utilizadas dentro deste projeto serão:
* Python 3.6.9
    * [Pandas](https://pandas.pydata.org/);
    * [Numpy](https://numpy.org/);
    * [Scikit-learn](https://scikit-learn.org/stable/);
    * [Statsmodels](https://www.statsmodels.org/stable/index.html);
    * [Seaborn](https://seaborn.pydata.org/);
    * [Matplotlib](https://matplotlib.org/stable/users/installing.html);
    * [Pillow](https://pillow.readthedocs.io/en/stable/)
* Gerenciamento de planilhas:
    * MS Excel e Google Sheets;
* Armazenagem e Computação em Nuvem:
    * Google Drive;
    * Google Colab;

# Cronograma
|                           -                           	|  Abril 	||  Maio  	||  Junho 	||  Julho 	|
|:-----------------------------------------------------:	|:------:	|:------:	|:------:	|:------:	|:------:	|:------:	|:------:	|
|                       Atividade                       	| 1 qui. 	| 2 qui. 	| 1 qui. 	| 2 qui. 	| 1 qui. 	| 2 qui. 	| 1 qui. 	|
| Plano de projeto                                      	|    X   	|        	|        	|        	|        	|        	|        	|
| Desenvolvimento do projeto e entendimento do problema 	|    X   	|    X   	|    X   	|        	|        	|        	|        	|
| Criação de conjunto de dados alvo                     	|    X   	|    X   	|    X   	|        	|        	|        	|        	|
| Limpeza dos dados e Pré-processamento                 	|    X   	|    X   	|    X   	|        	|        	|        	|        	|
| Base de Dados de Trabalho                             	|        	|        	|    X   	|        	|        	|        	|        	|
| Escolha da tarefa de mineração de dados               	|        	|        	|    X   	|    X   	|    X   	|        	|        	|
| Escolha do algoritmo para análise dos dados           	|        	|        	|    X   	|    X   	|    X   	|        	|        	|
| Mineração dos dados                                   	|        	|        	|    X   	|    X   	|    X   	|        	|        	|
| Interpretação dos dados                               	|        	|        	|        	|        	|    X   	|    X   	|        	|
| Consolidação do conhecimento                          	|        	|        	|        	|        	|        	|    X   	|        	|
| Entrega Final                                         	|        	|        	|        	|        	|        	|    X   	|        	|
| Apresentações                                         	|        	|        	|        	|        	|        	|    X   	|    X   	|

# Referências Acadêmicas
[1] Fayyad, U., Piatetsky-Shapiro, G., & Smyth, P. (1996). From Data Mining to Knowledge Discovery in Databases. AI Magazine, 17(3), 37. https://doi.org/10.1609/aimag.v17i3.1230

----
<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
