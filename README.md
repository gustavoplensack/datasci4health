# Projeto `Um estudo sobre a relação entre isolamento social e indicadores sócio-econômicos durante o período da pandemia da COVID-19 no Brasil.`

# Project `A study on the relationship between social isolation and socio-economic indicators during the pandemic period of COVID-19 in Brazil.`

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

No entanto, é fato que esta prática traz impactos grandes sobre a economia, em especial em países emergentes como o Brasil. Este estudo se propõe a investigar as relações entre o isolamento social praticado no país e indicadores econômicos como desemprego, informalidade e inflação. 

# Perguntas de Pesquisa
Qual a relação entre isolamento social e indicadores sócio-econômicos durante a pandemia da COVID-19 no Brasil?

## Hipóteses (10/04/2021):
**H1:** Num primeiro momento, o isolamento social leva ao aumento do desemprego;

**H2:** Num segundo momento, o aumento do desemprego leva à diminuição do isolamento social;

**H3:** Fatores como o aumento da Inflação, redução do PIB per Capita levam à redução do isolamento social;

**H4:** Políticas públicas, como o auxílio emergencial favorecem o isolamento social.

# Bases de Dados

* **IBGE**:
    * [PNAD](https://www.ibge.gov.br/estatisticas/sociais/educacao/9127-pesquisa-nacional-por-amostra-de-domicilios.html?=&t=o-que-e):compreende informações como ocupação, desemprego, informalidade, taxa de circulação;
    * [Indicadores econômicos](https://www.ibge.gov.br/estatisticas/economicas/precos-e-custos/9256-indice-nacional-de-precos-ao-consumidor-amplo.html?=&t=resultados): IPCA, INPC, variação do PIB e PIB per capita;
* **Ministério da Economia - Secretaria do Trabalho**:
    * [CAGED](https://www.gov.br/trabalho/pt-br/assuntos/empregador/caged): acesso geral ao cadastro de empregados e desempregados;
    * [Estatísticas do Seguro Desemprego](http://pdet.mte.gov.br/images/Seguro-Desemprego/202103/1-Apresenta%C3%A7%C3%A3o_Dados%20SD_mensal_Mar%C3%A7o_2021.pdf);
* [**Organização Mundial do Trabalho**](https://ilostat.ilo.org/): Dados gerais sobre o trabalho no mundo e definições sobre termos técnicos da área;
* **Dados sobre isolamento social**:
    * [City Analytics](https://www.enelx.com/br/pt/para-cidades/dashboard-covid-19): mapa de mobilidade;
    * [Painel InLoco](https://mapabrasileirodacovid.inloco.com.br/pt/): dados foram descontinuados (uma possibilidade, dado que esta plataforma foi descontinuada é investigar se os dados de SP e ES servem como proxy para estimar os dados foram descontinuados)

 

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
* Python
    * Dados:
        * Pandas;
        * Numpy;
        * Scikit-learn;
        * Statsmodels;
    * Web scraping(?):
        * Selenium;
        * Requests;
        * Beautiful Soup;
* Javascript/Typescript:
    * Web scraping(?):
        * Puppeteer;
* Armazenagem e Computação em Nuvem:
    * AWS - S3 (?);
    * Google Drive;
    * Google Colab;

**NOTA:** as ferramentas marcadas com (?) são as menos prováveis de usarmos ao longo do projeto, mas que podem vir a ser necessárias. Elas serão removidas desta lista à medida que o desenvolvimento do projeto avançar e sua necessidade ficar mais clara.

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
