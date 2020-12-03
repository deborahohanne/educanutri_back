# Algoritmo Genético para elaboração de Cardápio Nutricionais para Alimentação Escolar - EDUCANUTRI 

<p align="center"> Status do Projeto: Em desenvolvimento.
<div align="center">   
   <img width="200" alt="logo" src="https://user-images.githubusercontent.com/48803004/99796555-78219200-2b0c-11eb-9f90-fa303c4499fa.png">
</div>

## DESCRIÇÃO DO PROJETO

<p align="justify"> A finalidade da aplicação é minimizar o erro nutricional e facilitar o trabalho dos nutricionistas no gerenciamento dos cardápios nutricionais para alimentação escolar, o EDUCANUTRI fornecerá pratos que buscam a melhor combinação para a elaboração do cardápio. </p>

<p align="justify"> O EDUCANUTRI visa resolver problemas na elaboração de cardápios nutricionais com uma proposta de solução do sistema para fornecer aos usuários gerais um formulário de solicitação de um cardápio nutricional baseado em uma faixa etária, características dos alimentos como a cor, consistência e variedade, e simultaneamente um baixo custo financeiro. </p>

<p align="justify">Para mais informações leia o <b><a href="">Artigo<a></b>.  </p>
   
## FERRAMENTAS

<ul>
   <li><b>Linguagem:</b> Python</li>
   <li><b>FastAPI</b></li> 
   <li><b>Docker</b></li> 
</ul>   

## COMO RODAR A APLICAÇÃO 
<p align="justify"> Para abrir uma das amostras do projeto, comece fazendo checkout de uma da ramificações(Branch) pricipal(master) e abra o diretório raiz em qualquer editor de texto.</p>

## Prerequisites

- [Python 3.8](https://www.python.org/)


### CLONANDO O PROJETO

1. Clone o repositório:

```
git clone https://github.com/deborahohanne/educanutri_back.git
```

2. Esta etapa garante que você esteja na ramificação principal. 

```
git checkout master
```

<b>Nota:</b> Se você desejar alterar para uma ramificação(Branch) diferente, substitua "master" pelo nome da ramificação(Branch) que deseja visualizar.

3. Por fim, abra o diretório educanutri_back/ no editor.

### Docker

No projeto, a raiz cria o Dockerfile

```bash
# docker image build -t <IMAGE_NAME> <DOCKERFILE_DIRECTORY>
docker image build -t <IMAGE_NAME> .
```

Execute o contêiner usando a imagem gerada
```bash
#  docker run <IMAGE_NAME>
docker run <IMAGE_NAME>
```

### Docker Compose

Na raiz do projeto execute
```
docker-compose up
```
ou
```
docker-compose up --build
```
   
## REPOSITÓRIO FRONT-END

<p align="justify"><a href="https://github.com/MilenaNobre/educanutri_frontend"> EDUCANUTRI - FRONT-END </a> </p>
  
## DESENVOLVEDORES
<p align="justify"> :octocat: <a href="https://github.com/deborahohanne"> Deborah Ohanne </a> </p>
<p align="justify"> :octocat: <a href="https://github.com/MilenaNobre"> Milena Nobre </a> </p>
<p align="justify"> :octocat: <a href="https://github.com/jjorge98"> Jorge Júnior </a> </p>
