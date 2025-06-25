import streamlit as st
import pandas as pd

st.set_page_config(page_title="AXA Panel", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "home"

st.logo("images/logo.png", size="large")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: white;
    }
    h1 {
        color: #00008f !important;
        font-size: 4em;
        font-weight: bold;
        margin-bottom: 40px;
    }
    .stButton>button {
        margin-bottom: 1rem;
        color: #00008f !important;
        font-weight: bold !important;
        border: none !important;
        background-color: transparent !important;
    }
    .left-content {
        margin-top: 4vh;
    }
    .nav-buttons {
        display: flex;
        gap: 1rem;
        justify-content: center;
        margin-top: 4vh;
    }
    .nav-buttons button {
        background-color: transparent !important;
        color: #00008f !important;
        border: none !important;
        font-weight: bold;
        font-size: 1.1em;
    }
    </style>
""", unsafe_allow_html=True)

# 🔁 NAVIGATION BAR SEGÚN LA PÁGINA ACTUAL
def nav_bar(current):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if current == "home":
            st.markdown("**Home**")
        else:
            if st.button(" Home", key=f"{current}_home"):
                st.session_state.page = "home"

    with col2:
        if current == "sobre_mi":
            st.markdown("**Sobre mí**")
        else:
            if st.button(" Sobre mí", key=f"{current}_sobre_mi"):
                st.session_state.page = "sobre_mi"

    with col3:
        if current == "resolucion":
            st.markdown("**Resolución**")
        else:
            if st.button(" Resolución", key=f"{current}_resolucion"):
                st.session_state.page = "resolucion"

    with col4:
        if current == "conclusiones":
            st.markdown("**Conclusiones**")
        else:
            if st.button(" Conclusiones", key=f"{current}_conclusiones"):
                st.session_state.page = "conclusiones"



# HOME
if st.session_state.page == "home":
    col1, col2 = st.columns([2, 1], gap="large")
    with col1:
        st.markdown('<div class="left-content">', unsafe_allow_html=True)
        st.markdown("<h1>TECH GRADUATE PROGRAM</h1>", unsafe_allow_html=True)
        col_a, col_b, col_c = st.columns([1, 1, 1])
        with col_a:
            if st.button("Sobre mí", key="home_sobre_mi"):
                st.session_state.page = "sobre_mi"
        with col_b:
            if st.button("Resolución del caso", key="home_resolucion"):
                st.session_state.page = "resolucion"
        with col_c:
            if st.button("Conclusiones", key="home_conclusiones"):
                st.session_state.page = "conclusiones"

    with col2:
        st.image("images/logo.png", width=300)

# SOBRE MÍ
elif st.session_state.page == "sobre_mi":
    nav_bar("sobre_mi")
    st.write("###  Soy Arabela Carceles, estudiante de Master en Business Analytics")
    # Imagen centrada
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col1:
        st.image("images/perfil.jpeg", width=350)
    with col2:
        st.markdown("### 🔗 Enlaces de interés")
        st.markdown("""
            <ul style="font-size: 1.1em; list-style: none; padding-left: 0;">
                <li> <a href="https://www.linkedin.com/in/arabela-carceles-carrillo/" target="_blank">LinkedIn</a></li>
                <li> <a href="https://github.com/arabelacarceles/" target="_blank">GitHub</a></li>
            </ul>
        """, unsafe_allow_html=True)
    

# RESOLUCIÓN
elif st.session_state.page == "resolucion":
    nav_bar("resolucion")
    st.write("###  Resolución del caso")
    st.write("Aquí puedes desarrollar tu análisis, mostrar gráficos, texto o resultados...")

# CONCLUSIONES
elif st.session_state.page == "conclusiones":
    nav_bar("conclusiones")
    st.write("###  Conclusiones")
    st.write("Aquí puedes cerrar tu presentación con los puntos clave o aprendizajes finales.")
