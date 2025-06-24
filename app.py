import streamlit as st

st.set_page_config(page_title="AXA Panel", layout="wide")

# Estado de navegación
if "page" not in st.session_state:
    st.session_state.page = "home"

# Mostrar el logo en la cabecera
st.logo("images/logo.png", size="large")

# Estilos CSS personalizados
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: white;
    }
    h1 {
        color: #0040E5 !important;
        font-size: 4em;
        font-weight: bold;
        margin-bottom: 40px;
    }
    .stButton>button {
        margin-bottom: 1rem;
        font-weight: bold !important;
        color: #0040E5 !important;
        border: 2px solid #0040E5 !important;
    }
    .left-content {
        margin-top: 4vh;
    }
    .nav-buttons {
        display: flex;
        gap: 2rem;
        justify-content: center;
        margin-top: 6vh;
    }
    .nav-buttons button {
        background-color: transparent !important;
        border: none !important;
        color: #0040E5 !important;
        font-weight: bold;
        font-size: 1.1em;
    }
    </style>
""", unsafe_allow_html=True)

# HOME PAGE
if st.session_state.page == "home":
    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.markdown('<div class="left-content">', unsafe_allow_html=True)
        st.markdown("<h1>TECH GRADUATE PROGRAM</h1>", unsafe_allow_html=True)
        if st.button("🙋 Sobre mí"):
            st.session_state.page = "sobre_mi"
        if st.button("🧩 Resolución del caso"):
            st.session_state.page = "resolucion"
        if st.button("✅ Conclusiones"):
            st.session_state.page = "conclusiones"
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        pass  # el logo ya está en la cabecera con st.logo

# NAVIGATION BAR (reutilizable en todas páginas)
def nav_bar():
    st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🙋 Sobre mí"):
            st.session_state.page = "sobre_mi"
    with col2:
        if st.button("🧩 Resolución del caso"):
            st.session_state.page = "resolucion"
    with col3:
        if st.button("✅ Conclusiones"):
            st.session_state.page = "conclusiones"
    st.markdown('</div>', unsafe_allow_html=True)

# SOBRE MÍ
if st.session_state.page == "sobre_mi":
    nav_bar()
    st.write("### 👋 ¡Hola! Soy [tu nombre], participante del AXA Tech Graduate Program...")
    st.write("Aquí puedes contar tu perfil, intereses, formación o lo que te apetezca destacar.")

# RESOLUCIÓN DEL CASO
elif st.session_state.page == "resolucion":
    nav_bar()
    st.write("### 🧩 Resolución del caso")
    st.write("Aquí puedes desarrollar tu análisis, mostrar gráficos, texto o resultados...")

# CONCLUSIONES
elif st.session_state.page == "conclusiones":
    nav_bar()
    st.write("### ✅ Conclusiones")
    st.write("Aquí puedes cerrar tu presentación con los puntos clave o aprendizajes finales.")
