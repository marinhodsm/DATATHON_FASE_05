# 🏥 Painel Inteligente de Apoio à Prevenção da Obesidade

## 📌 Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de aplicar técnicas de Ciência de Dados e Machine Learning na predição dos níveis de obesidade, contribuindo para a identificação de fatores associados ao excesso de peso e apoiando ações de prevenção em saúde.

A solução foi construída a partir de um conjunto de dados contendo informações comportamentais, hábitos alimentares, estilo de vida e características corporais dos indivíduos.

Além da etapa analítica realizada em Jupyter Notebook, o projeto também disponibiliza uma aplicação interativa desenvolvida em Streamlit, permitindo que usuários preencham um formulário e obtenham uma predição personalizada do nível de obesidade.

---

## 🎯 Objetivos

* Investigar a capacidade de modelos de Machine Learning em prever níveis de obesidade;
* Comparar o desempenho de modelos treinados em diferentes cenários;
* Avaliar a influência de hábitos e comportamentos na predição;
* Identificar os fatores mais relevantes associados à obesidade;
* Disponibilizar uma aplicação interativa para demonstração prática do modelo desenvolvido.

---

## 📊 Cenários Avaliados

Foram comparados dois cenários distintos:

### Cenário 01 – Variáveis Comportamentais

Utiliza apenas informações relacionadas a hábitos e estilo de vida, como:

* Consumo de vegetais;
* Consumo de água;
* Frequência de atividade física;
* Tempo de uso de dispositivos eletrônicos;
* Consumo de álcool;
* Hábitos alimentares.

### Cenário 02 – Variáveis Comportamentais + Medidas Corporais

Além das informações comportamentais, incorpora:

* Idade;
* Altura;
* Peso.

Este cenário apresentou os melhores resultados preditivos e foi utilizado na aplicação final.

---

## 🤖 Modelos Avaliados

Os seguintes algoritmos foram testados:

* Random Forest
* XGBoost

Após a comparação dos resultados, o modelo XGBoost apresentou o melhor desempenho e foi selecionado para implantação.

---

## 📈 Principais Resultados

* Melhor modelo: XGBoost
* Melhor cenário: Variáveis comportamentais + medidas corporais
* Predição de 7 níveis distintos de classificação relacionados ao peso corporal

Além da avaliação de desempenho, foi realizada análise de importância das variáveis, permitindo identificar os principais fatores associados aos diferentes níveis de obesidade.

---

## 🖥 Aplicação Web

A aplicação foi desenvolvida utilizando Streamlit e possui:

* Painel executivo com informações sobre obesidade;
* Página de fatores de risco;
* Página de hábitos preventivos;
* Formulário para predição individual.

Link de acesso:
https://marinhodsm-tech-challenge-fase04.streamlit.app/

---

## 🛠 Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Matplotlib
* Seaborn
* Streamlit
* Joblib

## 📁 Estrutura de Arquivos

- **obesity.csv**: conjunto de dados utilizado para análise exploratória, engenharia de atributos e treinamento dos modelos.

- **notebook.ipynb**: notebook contendo todas as etapas do projeto, incluindo análise exploratória dos dados (EDA), preparação dos dados, treinamento, avaliação e comparação dos modelos de Machine Learning.

- **modelo_obesidade.pkl**: arquivo contendo o modelo XGBoost treinado e utilizado pela aplicação para realizar as predições.

- **aplicacao.py**: aplicação desenvolvida em Streamlit, responsável pela interface interativa, visualização dos insights e realização das predições individuais.

- **requirements.txt**: arquivo contendo as dependências necessárias para execução do projeto e implantação da aplicação.

- **video_apresentacao.mp4**: vídeo demonstrando o desenvolvimento do projeto, os principais resultados obtidos e o funcionamento da aplicação.