import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA (Tema escuro traz mais requinte para carros)
st.set_page_config(
    page_title="Apex Motors | Premium Club",
    page_icon="🏎️",
    layout="wide"
)

# 2. HEADER / MENU SUPERIOR SIMULADO
col_logo, col_vazio, col_redes = st.columns([2, 5, 2])
with col_logo:
    st.markdown("### 🏎️ **APEX MOTORS**")
with col_redes:
    st.markdown("<p style='text-align: right; color: gray;'>Fale Conosco: 0800 777 9000</p>", unsafe_allow_html=True)

st.divider()

# 3. HERO SECTION (Chamada Principal)
# Usando colunas para colocar o texto de impacto do lado esquerdo e o carro principal do direito
st.markdown("<h1 style='text-align: center; font-size: 3rem;'>O Futuro da Performance Chegou</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray; font-size: 1.2rem;'>Conheça a nova linha Hyper-E de esportivos elétricos e híbridos de alta performance.</p>", unsafe_allow_html=True)

st.write("") # Espaçador

col_hero_txt, col_hero_img = st.columns([4, 6], gap="large")

with col_hero_txt:
    st.markdown("## **Apex Hyper-E Sport**")
    st.markdown("""
    * **0 a 100 km/h:** Em apenas 2.4 segundos.
    * **Autonomia:** Até 650km com uma única carga completa.
    * **Tecnologia:** Cockpit inteligente guiado por Inteligência Artificial.
    * **Exclusividade:** Apenas 50 unidades destinadas ao mercado nacional.
    """)
    st.write("")
    st.info("💡 Agende um Test-Drive exclusivo e sinta a aceleração contínua do motor elétrico.")
    
    # Gatilho de conversão (CTA)
    if st.button("🏁 Quero Garantir Minha Unidade", type="primary", use_container_width=True):
        st.toast("Preencha o formulário no final da página para receber o convite!", icon="🚀")

with col_hero_img:
    # Imagem de um carro esportivo elétrico laranja moderno
    st.image("https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcR_gaaFUciXLzrzyoTJr8vcfgjDpsBzG0alpCqVQdkdI_2i6drLSgMvD3DjRjeqZpZl3KUdyRgabn_9BM4", 
             caption="Apex Hyper-E Sport — Aerodinâmica e potência redefinidas.", use_container_width=True)

st.divider()

# 4. GALERIA E CARACTERÍSTICAS (O Showcase)
st.markdown("<h2 style='text-align: center;'>Destaques da Experiência Premium</h2>", unsafe_allow_html=True)
st.write("")

col_g1, col_g2 = st.columns(2, gap="medium")

with col_g1:
    # Painel interno do carro de luxo
    st.image("https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcSvJs8iFdP2s6U1vXb0oDrGYx3AdnzzI1Su7of_f6p_mba-vbWehOjIRoHiFZIrPvhUNapdesfrq_m63OY", 
             caption="Interior artesanal com acabamento em couro legítimo e fibra de carbono.", use_container_width=True)

with col_g2:
    # Showroom de carros da concessionária
    st.image("https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcQ8ErTKgtkwXjr9vQuiFg5JLebgMBLu90MRyhLAjbtuKkeNut2A_I6jGnpZcyWiiquru6gfcG98JeJElf0", 
             caption="Visite nosso Showroom Conceito e viva o atendimento sob medida.", use_container_width=True)

st.divider()

# 5. FORMULÁRIO DE CAPTURA (Lead Generation)
# Centralizar o formulário usando colunas vazias nas pontas
_, col_form, _ = st.columns([2, 4, 2])

with col_form:
    st.markdown("<h3 style='text-align: center;'>Entre no Círculo Exclusivo</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Receba a ficha técnica completa e fale com um consultor especialista.</p>", unsafe_allow_html=True)
    
    # Criando o formulário
    with st.form("captura_leads"):
        nome = st.text_input("Seu Nome Completo")
        email = st.text_input("Seu Melhor E-mail")
        telefone = st.text_input("Telefone com WhatsApp")
        
        modelo_interesse = st.selectbox(
            "Modelo de Interesse", 
            ["Apex Hyper-E Sport (Elétrico)", "Apex GrandTour V8 (Híbrido)", "Apex Horizon (SUV Premium)"]
        )
        
        # Botão de envio dentro do formulário
        enviado = st.form_submit_button("Me Inscrever na Lista VIP", use_container_width=True)
        
        if enviado:
            if nome and email and telefone:
                st.success(f"Obrigado, {nome}! Nossa equipe de especialistas entrará em contato em menos de 15 minutos.")
                # Aqui em uma aula você ensina que esses dados seriam enviados para um CRM ou banco
            else:
                st.error("Por favor, preencha todos os campos para continuar.")

# 6. RODAPÉ
st.write("")
st.divider()
st.markdown("<p style='text-align: center; color: gray; font-size: 0.8rem;'>© 2026 Apex Motors S.A. Todos os direitos reservados. Fotos meramente ilustrativas.</p>", unsafe_allow_html=True)