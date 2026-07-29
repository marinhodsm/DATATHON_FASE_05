# 🎓 Painel Inteligente de Apoio à Identificação de Alunos em Risco de Defasagem Escolar

## 📌 Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de aplicar técnicas de Ciência de Dados e Machine Learning para identificar, de forma antecipada, estudantes com maior probabilidade de apresentar aumento na defasagem escolar.

A solução foi construída a partir de uma base histórica contendo indicadores acadêmicos, comportamentais, psicossociais e psicopedagógicos dos alunos, permitindo identificar padrões associados à piora do desempenho ao longo do tempo.

Além da etapa analítica desenvolvida em Jupyter Notebook, o projeto disponibiliza uma aplicação web desenvolvida em Streamlit, permitindo que gestores e equipes pedagógicas realizem simulações individuais de risco por meio do preenchimento dos indicadores atuais do estudante.

---

## 🎯 Objetivos

* Identificar padrões associados ao aumento da defasagem escolar;
* Antecipar alunos com maior probabilidade de piora em avaliações futuras;
* Comparar diferentes algoritmos de Machine Learning;
* Avaliar a contribuição dos indicadores educacionais na previsão do risco;
* Disponibilizar uma aplicação interativa para apoio à tomada de decisão pedagógica.

---

## 📊 Estratégia de Modelagem

Como o objetivo do desafio consistia em prever a ocorrência de aumento da defasagem antes que ela acontecesse, foi necessária a construção de uma variável alvo baseada na evolução temporal de cada estudante.

Foram adotadas as seguintes premissas:

* Cada aluno foi ordenado cronologicamente por ano de avaliação;
* Apenas avaliações consecutivas foram consideradas (2022→2023 e 2023→2024);
* Registros sem avaliação imediatamente posterior foram descartados;
* Foi considerada situação de risco qualquer redução no indicador de defasagem entre duas avaliações consecutivas, independentemente do nível inicial do aluno.

Dessa forma, o modelo aprende a identificar sinais de piora antes que ela ocorra.

---

## 🤖 Modelos Avaliados

Foram comparados dois algoritmos de classificação:

* Regressão Logística
* Random Forest

Após a comparação dos resultados, o modelo Random Forest apresentou melhor desempenho geral e foi selecionado para implantação na aplicação final.

---

## 📈 Principais Resultados

O modelo Random Forest apresentou desempenho superior em praticamente todas as métricas avaliadas.

Principais resultados obtidos:

* Melhor modelo: Random Forest
* Accuracy: aproximadamente 80%
* ROC-AUC: aproximadamente 0,80
* Validação cruzada utilizando GroupKFold por aluno
* Geração de probabilidade individual de risco para cada estudante

Além da avaliação do desempenho dos modelos, também foi realizada análise da importância das variáveis, identificando quais indicadores exercem maior influência na previsão do aumento da defasagem.

Entre os indicadores mais relevantes destacam-se:

* Defasagem Atual
* IPV — Indicador do Ponto de Virada
* IPP — Indicador Psicopedagógico
* IDA — Indicador de Desempenho Acadêmico

---

## 🖥 Aplicação Web

Foi desenvolvida uma aplicação utilizando Streamlit para demonstrar o funcionamento do modelo preditivo.

A aplicação é composta por quatro páginas principais:

* 🏠 Visão Geral
* 📊 Dashboard Executivo
* ⭐ Principais Indicadores
* 🎯 Predição Individual do Aluno

Na página de predição, o usuário informa os indicadores atuais do estudante e o sistema retorna:

* Probabilidade estimada de aumento da defasagem;
* Classificação do risco (baixo, moderado ou alto);
* Recomendações de acompanhamento pedagógico.

---

## 🛠 Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* Scikit-Learn
* Random Forest
* Matplotlib
* Plotly
* Streamlit
* Joblib

---

## 📁 Estrutura de Arquivos

- **BASE DE DADOS PEDE 2024 - DATATHON.xlsx**: base de dados utilizada para análise exploratória, engenharia de atributos e treinamento dos modelos.

- **notebook.ipynb**: notebook contendo todas as etapas do projeto, incluindo análise exploratória dos dados (EDA), feature engineering, criação da variável target, treinamento, avaliação e comparação dos modelos de Machine Learning.

- **modelo_previsao_defasagem.pkl**: arquivo contendo o modelo Random Forest treinado e utilizado pela aplicação para realizar as predições individuais.

- **aplicacao.py**: aplicação desenvolvida em Streamlit, responsável pela interface gráfica, dashboard executivo, visualização dos indicadores e realização das predições.

- **requirements.txt**: arquivo contendo todas as dependências necessárias para execução local do projeto e implantação da aplicação.

- **video_apresentacao.mp4**: vídeo demonstrando o desenvolvimento do projeto, os principais resultados obtidos e o funcionamento da aplicação.