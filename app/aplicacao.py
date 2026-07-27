# Aplicação Streamlit — Dashboard + Predição de Obesidade

# ==================================================
# BIBLIOTECAS
# ==================================================

import joblib
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# ==================================================
# CONFIGURAÇÃO DA PÁGINA
# ==================================================

st.set_page_config(
    page_title='Painel de Apoio à Identificação de Alunos em Risco de Defasagem',
    # page_icon='icone.png',
    layout='wide'
)

col1, col2 = st.columns([1, 8])

with col1:
    st.image("logotipo.png", width=180)

with col2:

    st.markdown(
        """
        <div style="
            height:120px;
            display:flex;
            align-items:center;
        ">
            <h1 style="
                font-family: Verdana;
                margin:0;
                font-size:30px;
                color: #1a365d;
            ">
            PAINEL DE APOIO À PREVENÇÃO E DIAGNÓSTICO DE OBESIDADE
            </h1>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('---')

# ==================================================
# CARREGAMENTO DO MODELO TREINADO
# ==================================================

modelo = joblib.load('C:/Users/diego/Desktop/RM368720_DATATHON_FASE_05/models/modelo_previsao_defasagem.pkl')

# ==================================================
# ABAS PARA NAVEGAÇÃO DE PÁGINA
# ==================================================

st.markdown('**NAVEGAÇÃO DE PÁGINAS**')

tab1, tab2, tab3, tab4 = st.tabs([
    '🏠 Visão Geral',
    '⚠️ Fatores de Risco',
    '❤️ Hábitos Preventivos',
    '🩺 Predição Individual'
])

# ==================================================
# VISÃO GERAL
# ==================================================

with tab1:

    st.markdown('---')

    st.markdown(
        '''
        Este painel foi desenvolvido para apoiar a identificação de fatores
        associados à obesidade e auxiliar ações de prevenção e promoção da saúde.
        
        A solução utiliza técnicas de Ciência de Dados e Machine Learning para
        analisar características comportamentais e corporais relacionadas aos
        diferentes níveis de obesidade.
        '''
    )

    st.markdown('---')

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            '🤖 **MODELO UTILIZADO**',
            'XGBoost'
        )

    with col2:
        st.metric(
            '🎯 **ACURÁCIA OBTIDA**',
            '96,2%'
        )

    with col3:
        st.metric(
            '📊 **CLASSES PREVISTAS**',
            '7 níveis'
        )

    st.markdown('---')

    st.subheader('📋 Funcionalidades')

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            '''
            📊 **ANÁLISE DE FATORES ASSOCIADOS À OBESIDADE**

            Identificação das variáveis mais relevantes para a classificação
            dos níveis de obesidade.
            '''
        )

        st.info(
            '''
            ⚠️ **AVALIAÇÃO DE FATORES DE RISCO**

            Destaque para hábitos e comportamentos associados ao aumento
            da probabilidade de obesidade.
            '''
        )

    with col2:

        st.info(
            '''
            ❤️ **HÁBITOS PREVENTIVOS**

            Apresentação de práticas relacionadas à promoção da saúde
            e prevenção da obesidade.
            '''
        )

        st.info(
            '''
            🩺 **PREDIÇÃO INDIVIDUAL**

            Simulação personalizada do nível de obesidade com base
            nas características pessoais informadas pelo usuário.
            '''
        )

    st.markdown('---')

    st.subheader('🔎 Principais Achados')

    st.success(
        '''
        • Medidas corporais como peso e altura apresentaram forte influência
        na classificação dos níveis de obesidade.

        • Fatores comportamentais também demonstraram relevância,
        especialmente hábitos alimentares e padrões de consumo.

        • O modelo XGBoost apresentou o melhor desempenho entre os modelos avaliados.

        • Os resultados reforçam a importância de estratégias preventivas
        focadas em alimentação saudável e estilo de vida ativo.
        '''
    )

    st.caption(
        '''
        Este sistema possui finalidade educacional e de apoio à análise de dados.
        Os resultados não substituem avaliação médica ou diagnóstico profissional.
        '''
    )

# ==================================================
# FATORES DE RISCO
# ==================================================

with tab2:

    st.markdown('---')

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        '🍺 **CONSUMO DE ÁLCOOL**',
        'Alto Impacto'
    )

    col2.metric(
        '🍔 **ALIMENTAÇÃO**',
        'Alto Impacto'
    )

    col3.metric(
        '🚶 **SEDENTARISMO**',
        'Moderado'
    )

    col4.metric(
        '🚬 **CIGARRO**',
        'Baixo'
    )

    st.markdown('---')
    
    st.subheader('Principais Fatores Associados ao Aumento do Risco')

    col1, col2 = st.columns(2)

    with col1:

        st.warning(
            '''
            🍺 **CONSUMO DE ÁLCOOL**

            O consumo frequente de bebidas alcoólicas pode aumentar
            a ingestão calórica diária e favorecer o ganho de peso
            ao longo do tempo.
            '''
        )

        st.warning(
            '''
            🍔 **CONSUMO DE ALIMENTOS ALTAMENTE CALÓRICOS**

            O consumo frequente de alimentos ricos em gorduras,
            açúcares e ultraprocessados está associado ao ganho
            excessivo de peso.
            '''
        )

    with col2:

        st.warning(
            '''
            🍪 **LANCHES ENTRE REFEIÇÕES**

            O hábito frequente de consumir alimentos entre as
            refeições principais pode contribuir para o excesso
            de ingestão calórica.
            '''
        )

        st.warning(
            '''
            🚗 **SEDENTARISMO E DESLOCAMENTO**

            Meios de transporte mais ativos, como caminhar ou
            pedalar, contribuem para maior gasto energético
            diário quando comparados ao uso exclusivo de veículos.
            '''
        )

    st.markdown('---')

    st.subheader('Interpretação')
    
    st.info(
        '''
        Os resultados indicam que hábitos relacionados à alimentação,
        consumo de álcool e nível de atividade cotidiana estão entre os
        principais fatores associados aos diferentes níveis de obesidade.

        Embora características corporais como peso e altura tenham grande
        influência na classificação, fatores comportamentais representam
        oportunidades importantes para prevenção e promoção da saúde.
        '''
    )

# ==================================================
# HÁBITOS PREVENTIVOS
# ==================================================

with tab3:

    st.markdown('---')

    col1, col2 = st.columns(2)

    with col1:

        st.success(
            '''
            🏃 **ATIVIDADE FÍSICA**

            Praticar exercícios regularmente contribui para o controle do peso corporal,
            melhora a saúde cardiovascular e reduz o risco de obesidade.
            '''
        )

        st.success(
            '''
            🥗 **ALIMENTAÇÃO BALANCEADA**

            Aumentar o consumo de vegetais e reduzir alimentos ultraprocessados
            está associado a melhores indicadores de saúde.
            '''
        )

    with col2:

        st.success(
            '''
            💧 **HIDRATAÇÃO**

            A ingestão adequada de água auxilia o funcionamento do organismo
            e favorece hábitos alimentares mais saudáveis.
            '''
        )

        st.success(
            '''
            😴 **ESTILO DE VIDA SAUDÁVEL**

            A combinação entre alimentação equilibrada, atividade física e
            monitoramento da saúde contribui para a prevenção da obesidade.
            '''
        )

    st.markdown('---')

    st.subheader('Interpretação')

    st.info(
        '''
        Os resultados obtidos indicam que hábitos relacionados à prática de atividade física,
        alimentação saudável e hidratação apresentam associação com menores níveis de obesidade.

        Embora fatores corporais como peso e altura sejam os mais influentes na classificação,
        os hábitos de vida continuam desempenhando papel importante na prevenção e no controle
        do excesso de peso.

        Dessa forma, estratégias de educação alimentar, incentivo à atividade física e promoção
        da saúde podem contribuir para a redução dos fatores de risco associados à obesidade.
        '''
    )

# ==================================================
# PREDIÇÃO INDIVIDUAL
# ==================================================

with tab4:

    st.markdown('---')

    st.markdown(
        '''
        Informe os indicadores atuais do(a) aluno(a) para estimar a
        probabilidade de ocorrência de piora na Defasagem na próxima
        avaliação.

        O modelo foi treinado utilizando Random Forest e considera os
        mesmos indicadores utilizados durante a etapa de modelagem.
        '''
    )

    with st.form('form_predicao'):

        st.subheader('Indicadores do Aluno')

        col1, col2 = st.columns(2)

        with col1:

            inde = st.number_input(
                'INDE',
                min_value=0.0,
                max_value=10.0,
                value=7.0,
                step=0.1,
                format='%.1f'
            )

            ida = st.number_input(
                'IDA',
                min_value=0.0,
                max_value=10.0,
                value=7.0,
                step=0.1,
                format='%.1f'
            )

            iaa = st.number_input(
                'IAA',
                min_value=0.0,
                max_value=10.0,
                value=7.0,
                step=0.1,
                format='%.1f'
            )

            ieg = st.number_input(
                'IEG',
                min_value=0.0,
                max_value=10.0,
                value=7.0,
                step=0.1,
                format='%.1f'
            )

        with col2:

            ips = st.number_input(
                'IPS',
                min_value=0.0,
                max_value=10.0,
                value=7.0,
                step=0.1,
                format='%.1f'
            )

            ipp = st.number_input(
                'IPP',
                min_value=0.0,
                max_value=10.0,
                value=7.0,
                step=0.1,
                format='%.1f'
            )

            ipv = st.number_input(
                'IPV',
                min_value=0.0,
                max_value=10.0,
                value=7.0,
                step=0.1,
                format='%.1f'
            )

            defasagem = st.selectbox(
                'Defasagem Atual',
                [-5, -4, -3, -2, -1, 0, 1, 2, 3],
                index=5
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
                O modelo estima baixa probabilidade de piora na Defasagem
                na próxima avaliação. Recomenda-se manter o acompanhamento
                pedagógico e monitorar periodicamente os indicadores do(a)
                aluno(a).
                '''
            )

        elif probabilidade < 0.60:

            st.warning(
                '🟡 **Risco moderado de aumento da Defasagem**'
            )

            st.info(
                '''
                O modelo indica atenção para possível piora da Defasagem.
                Recomenda-se acompanhar a evolução do(a) aluno(a) e avaliar
                intervenções pedagógicas preventivas.
                '''
            )

        else:

            st.error(
                '🔴 **Alto risco de aumento da Defasagem**'
            )

            st.info(
                '''
                O modelo estima elevada probabilidade de aumento da
                Defasagem na próxima avaliação. Recomenda-se priorizar
                o acompanhamento pedagógico e adotar estratégias de
                intervenção para reduzir o risco de queda no desempenho.
                '''
            )

        st.markdown('---')

        st.caption(
            '''
            A probabilidade apresentada corresponde à estimativa produzida
            pelo modelo Random Forest treinado neste trabalho. Trata-se de
            uma ferramenta de apoio à tomada de decisão, não substituindo a
            avaliação pedagógica realizada pela equipe escolar.
            '''
        )