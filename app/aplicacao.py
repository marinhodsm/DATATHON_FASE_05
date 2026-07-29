# ==================================================
# BIBLIOTECAS E CONFIGURACOES
# ==================================================
import joblib
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# ==================================================
# CONFIGURACAO DA PAGINA
# ==================================================
st.set_page_config(
    page_title='Painel de Apoio à Identificação de Alunos em Risco de Defasagem',
    page_icon='assets/icone.png',
    layout='wide'
)

col1, col2 = st.columns([1, 8])

with col1:

    st.markdown(
        '''
        <div style='margin-top:0px;'>
        ''',
        unsafe_allow_html=True
    )
    st.image('assets/logotipo.png', width=180)
    st.markdown(
        '''
        </div>
        ''',
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        '''
        <div style='
            height:110px;
            display:flex;
            align-items:center;
        '>
            <h1 style='
                font-family: Verdana;
                margin:0;
                font-size:30px;
                color: #1a365d;
                font-weight:700;
            '>
            <span style='font-size:20px;color:#718096;font-weight:400'>PAINEL DE APOIO</span><br>
            IDENTIFICAÇÃO DE RISCO DE DEFASAGEM ESCOLAR
            </h1>
        </div>
        ''',
        unsafe_allow_html=True
    )

# ==================================================
# CARREGAMENTO DO MODELO TREINADO
# ==================================================
modelo = joblib.load('models/modelo_previsao_defasagem.pkl')

# ==================================================
# NAVEGACAO DE PAGINA
# ==================================================
tab1, tab2, tab3, tab4 = st.tabs([
    '🏠 **VISÃO GERAL**',
    '📊 **DASHBOARD**',
    '⭐ **PRINCIPAIS INDICADORES**',
    '🎯 **PREDIÇÃO DO ALUNO**'
])

# ==================================================
# PAGINA 01 - VISAO GERAL
# ==================================================
with tab1:

    st.markdown(
        '''
        <div style='
            background:#f7fafc;
            padding:16px 20px;
            border-radius:8px;
            border-left:5px solid #1a365d;
            font-family: Verdana;
            color:#2d3748;
            font-size:15px;
            line-height:1.5;
            margin-bottom:20px;
        '>
            <p style='margin:0 0 8px 0;'>
                Este painel foi desenvolvido para apoiar a identificação de fatores associados ao aumento da defasagem escolar
                e auxiliar ações de prevenção e intervenção pedagógica.
            </p>
            <p style='margin:0;'>
                A ferramenta utiliza técnicas de Ciência de Dados e Machine Learning para analisar indicadores acadêmicos,
                psicossociais e psicopedagógicos relacionados ao risco de queda no desempenho dos alunos.
            </p>
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.subheader('📋 Funcionalidades')

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            '''
            📊 **ANÁLISE DOS INDICADORES ACADÊMICOS**

            Avaliação dos indicadores de desenvolvimento educacional,
            desempenho acadêmico, engajamento, aspectos psicossociais e psicopedagógicos
            para identificar padrões associados ao aumento da defasagem escolar.

            '''
        )

        st.info(
            '''
            🤖 **MODELO PREDITIVO BASEADO EM MACHINE LEARNING**

            A solução utiliza o algoritmo Random Forest treinado com dados históricos
            dos estudantes para estimar a probabilidade de aumento da defasagem ou queda
            de seu desempenho na avaliação subsequente.
            '''
        )

    with col2:

        st.info(
            '''
            🎯 **IDENTIFICAÇÃO PRECOCE DE RISCO**

            O modelo estima a probabilidade de piora da defasagem antes que ela ocorra,
            permitindo identificar alunos que demandam maior atenção e acompanhamento
            pedagógico preventivo.
            '''
        )

        st.info(
            '''
            📈 **APOIO À TOMADA DE DECISÃO PEDAGÓGICA**

            Os resultados auxiliam gestores e equipes pedagógicas na priorização
            de intervenções, contribuindo para o monitoramento contínuo dos alunos
            e para a prevenção da queda no desempenho acadêmico.
            '''
        )

# ==================================================
# PAGINA 02 - DASHBOARD
# ==================================================
with tab2:

    # ================================
    # KPIs PRINCIPAIS
    # ================================

    col1, col2, col3, col4 = st.columns(4)

    col1.metric('Alunos analisados (2022-2024)', '1.586')
    col2.metric('Média do INDE (Índice de Desenvolvimento Educacional)', '7.3')
    col3.metric('Alunos com risco alto', '20,0%')
    col4.metric('Acurácia do modelo', '80,5%')

    st.markdown('---')

    col1, col2 = st.columns(2)
    # ================================
    # DISTRIBUICAO DE DEFASAGEM
    # ================================
    with col1:
    
        defasagem = [-5, -4, -3, -2, -1, 0, 1, 2, 3]
        alunos =    [ 0,  0,  3, 90, 441, 421, 81, 16, 2]

        fig_def = go.Figure()

        fig_def.add_bar(
            x=defasagem,
            y=alunos,
            text=alunos,
            textposition='outside',
            cliponaxis=False,
            marker_color='#1a365d'
        )

        fig_def.update_layout(
            title='📉 Distribuição da Defasagem (2024)',
            xaxis_title='Faixa Defasagem',
            yaxis_title='Alunos',
            height=350,
            margin=dict(l=20, r=20, t=60, b=20),
        )

        st.plotly_chart(fig_def, use_container_width=True)

    # ================================
    # IMPORTANCIA DOS INDICADORES
    # ================================
    with col2:

        indicadores = ['Defasagem', 'IPV', 'IPP', 'IDA', 'INDE', 'IEG', 'IPS', 'IAA']
        importancia = [0.258, 0.163, 0.128, 0.120, 0.118, 0.079, 0.068, 0.067]

        fig_def = go.Figure()

        fig_def.add_bar(
            x=indicadores,
            y=importancia,
            text=[f'{v:.3f}' for v in importancia],
            textposition='outside',
            cliponaxis=False,
            marker_color='#2b6cb0'
        )

        fig_def.update_layout(
            title='⭐ Importância dos Indicadores',
            xaxis_title='Indicador',
            yaxis_title='Importância',
            height=350,
            margin=dict(l=20, r=20, t=60, b=20),
        )

        st.plotly_chart(fig_def, use_container_width=True)

    st.markdown('---')

    # ================================
    # DISTRIBUIÇÃO DOS INDICADORES
    # ================================
    st.markdown('##### 📊 Distribuição dos Indicadores Acadêmicos e Psicossociais (2024)')

    col1, col2 = st.columns(2)

    with col1:
        # INDE
        valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        frequencia = [0, 0, 0, 0, 5, 51, 124, 331, 415, 127, 1]

        fig_inde = go.Figure()

        fig_inde.add_bar(
            x=valores,
            y=frequencia,
            text=frequencia,
            textposition='outside',
            cliponaxis=False,
            marker_color='#4a5568'
        )

        fig_inde.update_layout(
            title='INDE',
            xaxis_title='INDE',
            yaxis_title='Frequência',
            height=350,
            bargap=0,
            bargroupgap=0,
            margin=dict(l=20, r=20, t=60, b=20),
            uniformtext_minsize=12,
            uniformtext_mode='hide',
            xaxis=dict(
                tickmode='array',
                tickvals=valores,
                ticktext=valores
            )
        )

        st.plotly_chart(fig_inde, use_container_width=True)

    with col2:
        # IDA
        valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        frequencia = [16, 5, 19, 64, 102, 131, 137, 192, 203, 137, 48]

        fig_inde = go.Figure()

        fig_inde.add_bar(
            x=valores,
            y=frequencia,
            text=frequencia,
            textposition='outside',
            cliponaxis=False,
            marker_color='#4a5568'
        )

        fig_inde.update_layout(
            title='IDA',
            xaxis_title='IDA',
            yaxis_title='Frequência',
            height=350,
            bargap=0,
            bargroupgap=0,
            margin=dict(l=20, r=20, t=60, b=20),
            uniformtext_minsize=12,
            uniformtext_mode='hide',
            xaxis=dict(
                tickmode='array',
                tickvals=valores,
                ticktext=valores
            )
        )

        st.plotly_chart(fig_inde, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        # IPS
        valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        frequencia = [0, 0, 0, 59, 26, 23, 244, 65, 586, 46, 5]

        fig_inde = go.Figure()

        fig_inde.add_bar(
            x=valores,
            y=frequencia,
            text=frequencia,
            textposition='outside',
            cliponaxis=False,
            marker_color='#4a5568'
        )

        fig_inde.update_layout(
            title='IPS',
            xaxis_title='IPS',
            yaxis_title='Frequência',
            height=350,
            bargap=0,
            bargroupgap=0,
            margin=dict(l=20, r=20, t=60, b=20),
            uniformtext_minsize=12,
            uniformtext_mode='hide',
            xaxis=dict(
                tickmode='array',
                tickvals=valores,
                ticktext=valores
            )
        )

        st.plotly_chart(fig_inde, use_container_width=True)

    with col2:
        # IPP
        valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        frequencia = [0, 0, 0, 2, 4, 20, 88, 248, 571, 113, 8]

        fig_inde = go.Figure()

        fig_inde.add_bar(
            x=valores,
            y=frequencia,
            text=frequencia,
            textposition='outside',
            cliponaxis=False,
            marker_color='#4a5568'
        )

        fig_inde.update_layout(
            title='IPP',
            xaxis_title='IPP',
            yaxis_title='Frequência',
            height=350,
            bargap=0,
            bargroupgap=0,
            margin=dict(l=20, r=20, t=60, b=20),
            uniformtext_minsize=12,
            uniformtext_mode='hide',
            xaxis=dict(
                tickmode='array',
                tickvals=valores,
                ticktext=valores
            )
        )

        st.plotly_chart(fig_inde, use_container_width=True)

# ==================================================
# PAGINA 03 - PRINCIPAIS INDICADORES
# ==================================================
with tab3:

    st.markdown(
        '''
        <div style='
            background:#f7fafc;
            padding:22px;
            border-radius:10px;
            border:1px solid #e2e8f0;
            font-family: Verdana;
            color:#2d3748;
            line-height:1.7;
            font-size:14px;
            margin-bottom:20px;
        '>
            <h4 style='margin:0; color:#1a365d; font-weight:700;'>
                Sobre os principais indicadores
            </h4>
            <p style='margin-top:12px;'>
                Dentre vários indicadores monitorados, alguns se destacam pela forte contribuição preditiva e pelo impacto direto na análise realizada pela ferramenta.
                Esses indicadores representam dimensões essenciais do desenvolvimento acadêmico, comportamental e socioemocional dos estudantes, sendo os que mais influenciam o modelo na estimativa de risco de aumento da defasagem escolar.
            </p>
            <p>
                Eles funcionam como um conjunto de métricas-chave que sintetizam aspectos críticos da trajetória do aluno, permitindo ao sistema identificar padrões, antecipar possíveis quedas de desempenho e apoiar decisões pedagógicas com maior precisão.
            </p>
        </div>
        ''',
        unsafe_allow_html=True
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
            Ajuda a identificar fatores que podem influenciar o desempenho escolar e o bem-estar geral do aluno.
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

# ==================================================
# PAGINA 04 - PREDICAO DO ALUNO
# ==================================================
with tab4:

    st.markdown(
        '''
        <div style='
            background:#f7fafc;
            padding:16px 20px;
            border-radius:8px;
            border-left:5px solid #1a365d;
            font-family: Verdana;
            color:#2d3748;
            font-size:15px;
            line-height:1.5;
        '>
            Informe os indicadores atuais do aluno para estimar a probabilidade de ocorrência de piora na defasagem na próxima avaliação.<br>
            Como premissa, o risco não está associado apenas a alunos já em situação de elevada defasagem, mas a qualquer piora observada em sua trajetória acadêmica.
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.markdown('---')

    col_form, col_resultado = st.columns(2)

    # ==================================================
    # FORMULÁRIO
    # ==================================================

    with col_form:

        with st.form('form_predicao'):

            st.markdown(
                '<h3 style="text-align: center;">FORMULÁRIO DO ALUNO</h3>',
                unsafe_allow_html=True
            )

            col1, col2 = st.columns(2)

            with col1:

                inde = st.slider(
                    'INDE (Índice de Desenvolvimento Educacional)',
                    0.0,
                    10.0,
                    7.0,
                    0.1,
                    format='%.1f'
                )

                ida = st.slider(
                    'IDA (Indicador de Desempenho Acadêmico)',
                    0.0,
                    10.0,
                    7.0,
                    0.1,
                    format='%.1f'
                )

                iaa = st.slider(
                    'IAA (Indicador de Autoavaliação)',
                    0.0,
                    10.0,
                    7.0,
                    0.1,
                    format='%.1f'
                )

                ieg = st.slider(
                    'IEG (Indicador de Engajamento)',
                    0.0,
                    10.0,
                    7.0,
                    0.1,
                    format='%.1f'
                )

            with col2:

                ips = st.slider(
                    'IPS (Indicador Psicossocial)',
                    0.0,
                    10.0,
                    7.0,
                    0.1,
                    format='%.1f'
                )

                ipp = st.slider(
                    'IPP (Indicador Psicopedagógico)',
                    0.0,
                    10.0,
                    7.0,
                    0.1,
                    format='%.1f'
                )

                ipv = st.slider(
                    'IPV (Indicador do Ponto de Virada)',
                    0.0,
                    10.0,
                    7.0,
                    0.1,
                    format='%.1f'
                )

                defasagem = st.slider(
                    'Defasagem Atual (Quanto maior, melhor.)',
                    -5,
                    3,
                    0
                )

            submit = st.form_submit_button(
                'REALIZAR PREDIÇÃO',
                type='primary',
                use_container_width=True
            )

    # ==================================================
    # PAINEL DE RESULTADO
    # ==================================================
    with col_resultado:

        st.markdown(
            '<h3 style="text-align: center;">RESULTADO DA PREDIÇÃO</h3>',
            unsafe_allow_html=True
        )

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

            st.markdown(
                f'''
                <div style='
                    background-color: #f8fafc;
                    padding: 12px 16px;
                    border-radius: 8px;
                    border: 1px solid #e2e8f0;
                    text-align: center;
                    font-family: Verdana;
                '>
                    <div style='font-size: 14px; color: #4a5568;'>
                        Probabilidade de risco de aumento da defasagem do aluno:
                    </div>
                    <div style='font-size: 26px; font-weight: 700; color: #1a365d;'>
                        {probabilidade*100:.1f}%
                    </div>
                </div>
                ''',
                unsafe_allow_html=True
            )

            st.progress(float(probabilidade))

            if probabilidade < 0.30:

                st.success('🟢 **BAIXO RISCO**')

                recomendacao = '''
                ✔ Manter o acompanhamento pedagógico.\n
                ✔ Continuar monitorando os indicadores.\n
                ✔ Reavaliar periodicamente o desempenho.
                '''

            elif probabilidade < 0.60:

                st.warning('🟡 **RISCO MODERADO**')

                recomendacao = '''
                ✔ Intensificar o acompanhamento.\n
                ✔ Avaliar possíveis fatores de piora.\n
                ✔ Planejar intervenções preventivas.
                '''

            else:
                st.error('🔴 **ALTO RISCO**')

                recomendacao = '''
                ✔ Priorizar o acompanhamento do aluno.\n
                ✔ Planejar intervenção pedagógica.\n
                ✔ Monitorar continuamente sua evolução.
                '''

            st.markdown(
                f'''
                <div style='
                    background:#f7fafc;
                    padding:18px 22px;
                    border-radius:10px;
                    border:1px solid #e2e8f0;
                    font-family: Verdana;
                    color:#2d3748;
                    line-height:1.6;
                    font-size:15px;
                    margin-top: 10px;
                '>
                    <strong style='font-size:16px; color:#1a365d;'>Sugestões:</strong>
                    <ul style='margin-top:10px;'>
                        {recomendacao}</ul>
                </div>
                ''',
                unsafe_allow_html=True
            )
            
        else:

            st.markdown(
                '''
                <p style='text-align:center;'>
                    <em>Após o preenchimento do formulário, o resultado da predição estará visível.</em>
                </p>
                ''',
                unsafe_allow_html=True
            )

st.markdown('---')
st.caption('Esta ferramenta oferece suporte à tomada de decisão, complementando — e nunca substituindo — a avaliação pedagógica realizada pela equipe escolar.')