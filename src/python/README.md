# Código fonte do projeto "Um estudo sobre a relação entre isolamento social e empregabilidade durante o período da pandemia da COVID-19 no Estado de São Paulo."

## Tecnologias usadas

A de algumas partes deste projeto foram feitas se baseando em majoritariamente em `Python 3.6.9`.

Caso você tenha que gerenciar as versões do Pyhton na sua máquina, recomendamos usar o [pyenv](https://github.com/pyenv/pyenv).

Nota: usar um virtualenv pode ser interessante para isolar as dependências.

## Instalação
Para instalar as bibliotecas usadas, basta usar:

```sh
pip install -r requirements.txt
```

## Principais scripts

### `src/data/`
Possui os scripts para processar os dados processados partindo dos dados brutos contidos em `<repo_root>/data/external/`. Basta executar o script `generate.py`. 

### `src/visualization/`
Possui os scripts para gerar as visualizações usadas neste projeto. Para gerar as visualizações, basta executar o script `visualize.py`.
