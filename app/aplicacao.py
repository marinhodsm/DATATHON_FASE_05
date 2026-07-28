# APLICACAO STREAMLIT - DASHBOARD + PREDICAO DE AUMENTO NA DEFASAGEM

# ==================================================
# BIBLIOTECAS E CONFIGURACOES
# ==================================================
import joblib
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

diretorio_projeto = 'C:/Users/diego/Desktop/RM368720_DATATHON_FASE_05'
# ==================================================
# CONFIGURACAO DA PAGINA
# ==================================================
st.set_page_config(
    page_title='Painel de Apoio à Identificação de Alunos em Risco de Defasagem',
    page_icon=f'{diretorio_projeto}/assets/icone.png',
    layout='wide'
)

col1, col2 = st.columns([1, 8])

with col1:
    st.image(f'{diretorio_projeto}/assets/logotipo.png', width=180)

with col2:

    st.markdown(
        '''
        <div style='
            height:120px;
            display:flex;
            align-items:center;
        '>
            <h1 style='
                font-family: Verdana;
                margin:0;
                font-size:30px;
                color: #1a365d;
            '>
            PAINEL DE APOIO À IDENTIFICAÇÃO DE RISCO DE DEFASAGEM
            </h1>
        </div>
        ''',
        unsafe_allow_html=True
    )

st.markdown('---')

# ==================================================
# CARREGAMENTO DO MODELO TREINADO
# ==================================================
modelo = joblib.load(f'{diretorio_projeto}/models/modelo_previsao_defasagem.pkl')

# ==================================================
# ABAS PARA NAVEGAÇÃO DE PÁGINA
# ==================================================
st.markdown('**NAVEGAÇÃO DE PÁGINAS**')

tab1, tab2, tab3 = st.tabs([
    '🏠 Visão Geral',
    '⭐ Principais Indicadores',
    '🎯 Predição do Aluno'
])

# ==================================================
# VISÃO GERAL
# ==================================================
with tab1:

    st.markdown(
        '''
        Este painel foi desenvolvido para apoiar a identificação de fatores associados
        ao aumento da defasagem escolar e auxiliar ações de prevenção e intervenção pedagógica.

        A ferramenta utiliza técnicas de Ciência de Dados e Machine Learning para analisar
        indicadores acadêmicos, psicossociais e psicopedagógicos relacionados ao risco de queda no desempenho dos alunos.
        '''
    )

    st.subheader('📋 Funcionalidades')

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            '''
            📊 **ANÁLISE DE FATORES ASSOCIADOS À DEFASAGEM ACADÊMICA**

            Identificação das variáveis mais relevantes para compreender
            os fatores que contribuem para a defasagem escolar ou queda no desempenho.
            '''
        )

        st.info(
            '''
            📊 **ANÁLISE DE FATORES ASSOCIADOS À DEFASAGEM ACADÊMICA**

            Identificação das variáveis mais relevantes para compreender
            os fatores que contribuem para a defasagem escolar ou queda no desempenho.
            '''
        )

    with col2:

        st.info(
            '''
            📊 **ANÁLISE DE FATORES ASSOCIADOS À DEFASAGEM ACADÊMICA**

            Identificação das variáveis mais relevantes para compreender
            os fatores que contribuem para a defasagem escolar ou queda no desempenho.
            '''
        )

        st.info(
            '''
            📊 **ANÁLISE DE FATORES ASSOCIADOS À DEFASAGEM ACADÊMICA**

            Identificação das variáveis mais relevantes para compreender
            os fatores que contribuem para a defasagem escolar ou queda no desempenho.
            '''
        )

    st.subheader('🔎 Principais Achados')

    st.success(
        '''
        📍 INSIRA SEU TEXTO AQUI.

        📍 INSIRA SEU TEXTO AQUI.

        📍 INSIRA SEU TEXTO AQUI.

        📍 INSIRA SEU TEXTO AQUI.
        '''
    )

    st.markdown('---')
    
    st.caption(
        '''
        Esta ferramenta oferece suporte à tomada de decisão,
        complementando — e nunca substituindo — a avaliação
        pedagógica realizada pela equipe escolar.
        '''
    )

# ==================================================
# PRINCIPAIS INDICADORES
# ==================================================
with tab2:

    st.markdown(
        '''
        Dentre vários indicadores monitorados, alguns se destacam
        pela forte contribuição preditiva e pelo impacto direto
        na análise realizada pela ferramenta.
        
        Esses indicadores representam dimensões essenciais do
        desenvolvimento acadêmico, comportamental e socioemocional
        dos estudantes, sendo os que mais influenciam o modelo na
        estimativa de risco de aumento da defasagem escolar.

        Eles funcionam como um conjunto de métricas-chave que sintetizam
        aspectos críticos da trajetória do aluno, permitindo ao sistema
        identificar padrões, antecipar possíveis quedas de desempenho e
        apoiar decisões pedagógicas com maior precisão.

        A seguir, estão os principais indicadores utilizados pelo modelo:
        '''
    )

    col1, col2 = st.columns(2)
    
    with col1:

        st.info(
            '''
            **📍INDE — Índice de Desenvolvimento Educacional**
            \nReflete o nível geral de desenvolvimento do estudante, considerando aspectos acadêmicos, comportamentais e socioemocionais.
            É um indicador sintético que ajuda a visualizar, de forma ampla, o estágio atual do aluno em sua trajetória escolar.
            '''
        )

        st.info(
            '''
            **📍IDA — Indicador de Desempenho Acadêmico**
            \nMede o desempenho do estudante nas principais áreas avaliadas pela instituição.
            É calculado a partir da média das notas de Matemática, Português e Inglês, oferecendo uma visão objetiva da performance acadêmica.
            '''
        )

        st.info(
            '''
            **📍IAA — Indicador de Autoavaliação**
            \nRepresenta a percepção do próprio aluno sobre seu desempenho, comportamento e evolução.
            Baseia-se na média das respostas de autoavaliação, pontuadas de 0 a 10, permitindo identificar como o estudante enxerga sua própria trajetória.
            '''
        )

        st.info(
            '''
            **📍IEG — Indicador de Engajamento**
            \nAvalia o nível de participação do aluno em atividades acadêmicas, tarefas, projetos e ações complementares.
            É calculado pela média das pontuações das tarefas realizadas, refletindo o comprometimento do estudante com o processo de aprendizagem.
            '''
        )

    with col2:
    
        st.info(
            '''
            **📍IPS — Indicador Psicossocial**
            \nMede aspectos emocionais, sociais e comportamentais do estudante, com base em avaliações realizadas por psicólogos.
            Ajuda a identificar fatores que podem influenciar o desempenho escolar e o bem-estar geral.
            '''
        )

        st.info(
            '''
            **📍IPP — Indicador Psicopedagógico**
            \nAvalia dimensões pedagógicas observadas por profissionais psicopedagógicos, como organização, autonomia, compreensão de conteúdos e estratégias de estudo.
            É calculado pela média das avaliações registradas.
            '''
        )

        st.info(
            '''
            **📍IPV — Indicador do Ponto de Virada**
            \nAnalisa a evolução longitudinal do aluno, considerando progresso acadêmico, engajamento e desenvolvimento emocional ao longo do tempo.
            É utilizado para identificar mudanças significativas — positivas ou negativas — na trajetória escolar.
            '''
        )

        st.info(
            '''
            **📍Defasagem Atual**
            \nIndica o nível atual de defasagem do estudante, considerando sua fase ideal e sua fase efetiva.
            Valores negativos representam atraso escolar, enquanto valores positivos indicam alinhamento ou avanço.
            Esse indicador é fundamental para estimar o risco de piora na próxima avaliação.
            '''
        )

    st.markdown('---')
        
    st.caption(
        '''
        Esta ferramenta oferece suporte à tomada de decisão,
        complementando — e nunca substituindo — a avaliação
        pedagógica realizada pela equipe escolar.
        '''
    )
# ==================================================
# PREDICAO DO ALUNO
# ==================================================
with tab3:

    st.markdown(
        '''
        Informe os indicadores atuais do aluno para estimar a probabilidade de ocorrência de piora em sua defasagem na próxima avaliação.
        \nComo premissa, o risco não está associado apenas a alunos já em situação de elevada defasagem, mas a qualquer piora em sua trajetória acadêmica.
        ''')

    with st.form('form_predicao'):

        st.subheader('Formulário do Aluno')

        col1, col2 = st.columns(2)

        with col1:

            inde = st.number_input(
                'INDE (índice de desenvolvimento educacional)',
                min_value=0.0,
                max_value=10.0,
                value=7.0,
                step=0.1,
                format='%.1f'
            )

            ida = st.number_input(
                'IDA (indicador de desempenho acadêmico)',
                min_value=0.0,
                max_value=10.0,
                value=7.0,
                step=0.1,
                format='%.1f'
            )

            iaa = st.number_input(
                'IAA (indicador de autoavaliação)',
                min_value=0.0,
                max_value=10.0,
                value=7.0,
                step=0.1,
                format='%.1f'
            )

            ieg = st.number_input(
                'IEG (indicador de engajamento)',
                min_value=0.0,
                max_value=10.0,
                value=7.0,
                step=0.1,
                format='%.1f'
            )

        with col2:

            ips = st.number_input(
                'IPS (indicador psicossocial)',
                min_value=0.0,
                max_value=10.0,
                value=7.0,
                step=0.1,
                format='%.1f'
            )

            ipp = st.number_input(
                'IPP (indicador psicopedagógico)',
                min_value=0.0,
                max_value=10.0,
                value=7.0,
                step=0.1,
                format='%.1f'
            )

            ipv = st.number_input(
                'IPV (indicador do ponto de virada)',
                min_value=0.0,
                max_value=10.0,
                value=7.0,
                step=0.1,
                format='%.1f'
            )

            defasagem = st.slider(
                'Defasagem Atual (quanto mais positivo, melhor)',
                min_value=-5,
                max_value=3
            )

        submit = st.form_submit_button(
            'Realizar Predição',
            type='primary'
        )

    # ==================================================
    # RESULTADO DA PREDIÇÃO
    # ==================================================
    if submit:

        dados = pd.DataFrame({
            'INDE': [inde],
            'IDA': [ida],
            'IAA': [iaa],
            'IEG': [ieg],
            'IPS': [ips],
            'IPP': [ipp],
            'IPV': [ipv],
            'Defasagem': [defasagem]
        })

        probabilidade = modelo.predict_proba(dados)[0][1]
        previsao = modelo.predict(dados)[0]

        st.markdown('---')

        st.subheader('Resultado da Predição')

        st.metric(
            label='Probabilidade estimada de risco',
            value=f'{probabilidade * 100:.1f}%'
        )

        if probabilidade < 0.30:

            st.success(
                '🟢 **Baixo risco de aumento da Defasagem**'
            )

            st.info(
                '''
                O modelo estima baixa probabilidade de piora na defasagem
                na próxima avaliação. Recomenda-se manter o acompanhamento
                pedagógico e monitorar periodicamente os indicadores do
                aluno.
                '''
            )

        elif probabilidade < 0.60:

            st.warning(
                '🟡 **Risco moderado de aumento da defasagem**'
            )

            st.info(
                '''
                O modelo indica atenção para possível piora da defasagem.
                Recomenda-se acompanhar a evolução do aluno e avaliar
                intervenções pedagógicas preventivas.
                '''
            )

        else:

            st.error(
                '🔴 **Alto risco de aumento da defasagem**'
            )

            st.info(
                '''
                O modelo estima elevada probabilidade de aumento da
                defasagem na próxima avaliação. Recomenda-se priorizar
                o acompanhamento pedagógico e adotar estratégias de
                intervenção para reduzir o risco de queda no desempenho.
                '''
            )

        st.markdown('---')

        st.caption(
            '''
            Esta ferramenta oferece suporte à tomada de decisão,
            complementando — e nunca substituindo — a avaliação
            pedagógica realizada pela equipe escolar.
            '''
        )