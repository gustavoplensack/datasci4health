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

* **IBGE**:
    * [PNAD](https://www.ibge.gov.br/estatisticas/sociais/educacao/9127-pesquisa-nacional-por-amostra-de-domicilios.html?=&t=o-que-e):compreende informações como ocupação, desemprego, informalidade, taxa de circulação;
    * [Indicadores econômicos](https://www.ibge.gov.br/estatisticas/economicas/precos-e-custos/9256-indice-nacional-de-precos-ao-consumidor-amplo.html?=&t=resultados): IPCA, INPC, variação do PIB e PIB per capita;
* **Ministério da Economia - Secretaria do Trabalho**:
    * [CAGED](https://www.gov.br/trabalho/pt-br/assuntos/empregador/caged): acesso geral ao cadastro de empregados e desempregados;
    * [Estatísticas do Seguro Desemprego](http://pdet.mte.gov.br/images/Seguro-Desemprego/202103/1-Apresenta%C3%A7%C3%A3o_Dados%20SD_mensal_Mar%C3%A7o_2021.pdf);
* [**Organização Mundial do Trabalho**](https://ilostat.ilo.org/): Dados gerais sobre o trabalho no mundo e definições sobre termos técnicos da área;
* **Dados sobre isolamento social**:
    * [City Analytics](https://www.enelx.com/br/pt/para-cidades/dashboard-covid-19): mapa de mobilidade;
    * [Painel InLoco](https://mapabrasileirodacovid.inloco.com.br/pt/): dados foram descontinuados (uma possibilidade, dado que esta plataforma foi descontinuada é investigar se os dados de SP e ES servem como proxy para estimar os dados foram descontinuados);
* [**Dados sobre COVID-19 no Brasil**](https://covid.saude.gov.br/): casos, recuperados e óbitos;
 

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
