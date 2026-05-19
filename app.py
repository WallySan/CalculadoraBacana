import streamlit as pd
import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Calculadora de Orçamento Freelance",
    page_icon="💰",
    layout="centered"
)

# 2. BACKEND BÁSICO (Simulado com Session State)
# O session_state funciona como um banco de dados temporário na memória do navegador.
if "historico_orcamenentos" not in st.session_state:
    st.session_state.historico_orcamenentos = []

# 3. CABEÇALHO DO APP
st.title("💰 Calculadora de Orçamento Freelance")
st.markdown("""
Esta ferramenta ajuda você a calcular o valor justo para o seu projeto freela 
com base nas suas horas de trabalho, custos e margem de lucro.
""")

st.divider()

# 4. FORMULÁRIO DE ENTRADA DE DADOS
st.subheader("📊 Dados do Projeto")

# Organizando os campos em colunas para ficar visualmente limpo
col1, col2 = st.columns(2)

with col1:
    nome_projeto = st.text_input("Nome do Projeto", placeholder="Ex: Site Institucional")
    valor_hora = st.number_input("Quanto vale sua hora? (R$)", min_value=10.0, value=50.0, step=5.0)
    horas_estimadas = st.number_input("Horas estimadas de trabalho", min_value=1, value=20, step=1)

with col2:
    custos_extras = st.number_input("Custos extras (Template, API, etc.) (R$)", min_value=0.0, value=0.0, step=10.0)
    margem_lucro = st.slider("Margem de lucro desejada (%)", min_value=0, max_value=100, value=20, step=5)

# 5. LÓGICA DE CÁLCULO
# Cálculo baseado nas variáveis inseridas pelo usuário
custo_tempo = valor_hora * horas_estimadas
subtotal = custo_tempo + custos_extras
valor_lucro = subtotal * (margem_lucro / 100)
preco_final = subtotal + valor_lucro

st.divider()

# 6. EXIBIÇÃO DOS RESULTADOS
st.subheader("💵 Resumo do Orçamento")

# Exibindo os resultados em cards (metrics)
c1, c2, c3 = st.columns(3)
c1.metric("Custo do Tempo", f"R$ {custo_tempo:,.2f}")
c2.metric("Margem de Lucro", f"R$ {valor_lucro:,.2f}")
c3.metric("Preço Final Mínimo", f"R$ {preco_final:,.2f}", delta_color="inverse")

# 7. BOTÃO PARA SALVAR (Ação do Backend)
if st.button("💾 Salvar Orçamento no Histórico", type="primary"):
    if nome_projeto.strip() == "":
        st.error("Por favor, dê um nome ao projeto antes de salvar!")
    else:
        # Criando um dicionário que representa nossa "linha" no banco de dados
        novo_registro = {
            "Projeto": nome_projeto,
            "Valor/Hora": f"R$ {valor_hora:.2f}",
            "Horas": horas_estimadas,
            "Custos Extras": f"R$ {custos_extras:.2f}",
            "Lucro (%)": f"{margem_lucro}%",
            "Preço Final": preco_final
        }
        # Adicionando a lista que está na memória do Streamlit
        st.session_state.historico_orcamenentos.append(novo_registro)
        st.success(f"Orçamento para '{nome_projeto}' salvo com sucesso!")

st.divider()

# 8. EXIBIÇÃO DO HISTÓRICO
st.subheader("📚 Orçamentos Salvos (Sessão Atual)")

if len(st.session_state.historico_orcamenentos) > 0:
    # Convertendo a lista de dicionários em um DataFrame do Pandas para exibição bonita
    df = pd.DataFrame(st.session_state.historico_orcamenentos)
    
    # Exibe a tabela formatada
    st.dataframe(df, use_container_width=True)
    
    # Botão para limpar o "banco de dados"
    if st.button("🗑️ Limpar Histórico"):
        st.session_state.historico_orcamenentos = []
        st.rerun()
else:
    st.info("Nenhum orçamento salvo ainda nesta sessão. Preencha os dados acima e clique em 'Salvar'.")