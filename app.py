import streamlit as st
import plotly.figure_factory as ff
import graphviz as gv

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
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if current == "home":
            st.markdown("**Home**")
        else:
            if st.button(" Home", key=f"nav_{current}_home"):
                st.session_state.page = "home"

    with col2:
        if current == "sobre_mi":
            st.markdown("**Sobre mí**")
        else:
            if st.button(" Sobre mí", key=f"nav_{current}_sobre_mi"):
                st.session_state.page = "sobre_mi"

    with col3:
        if current == "desarrollo":
            st.markdown("**Desarrollo**")
        else:
            if st.button(" Desarrollo", key=f"nav_{current}_desarrollo"):
                st.session_state.page = "desarrollo"

    with col4:
        if current == "aplicacion":
            st.markdown("**Aplicación**")
        else:
            if st.button(" Aplicación", key=f"nav_{current}_aplicacion"):
                st.session_state.page = "aplicacion"

    with col5:
        if current == "presupuesto":
            st.markdown("**Presupuesto**")
        else:
            if st.button(" Presupuesto", key=f"nav_{current}_presupuesto"):
                st.session_state.page = "presupuesto"

# HOME
if st.session_state.page == "home":
    col1, col2 = st.columns([2, 1], gap="large")
    with col1:
        st.markdown('<div class="left-content">', unsafe_allow_html=True)
        st.markdown("<h1>TECH GRADUATE PROGRAM</h1>", unsafe_allow_html=True)
        col_a, col_b, col_c, col_d = st.columns([1, 1, 1, 1])
        with col_a:
            if st.button("Sobre mí", key="home_sobre_mi"):
                st.session_state.page = "sobre_mi"
        with col_b:
            if st.button("Desarrollo", key="home_desarrollo"):
                st.session_state.page = "desarrollo"
        with col_c:
            if st.button("Aplicación", key="home_aplicacion"):
                st.session_state.page = "aplicacion"
        with col_d:
            if st.button("Presupuesto", key="home_presupuesto"):
                st.session_state.page = "presupuesto"

    with col2:
        st.image("images/logo.png", width=300)

# SOBRE MÍ
elif st.session_state.page == "sobre_mi":
    nav_bar("sobre_mi")
    st.write("### Soy Arabela Carceles, estudiante de Master en Business Analytics")
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

# DESARROLLO
elif st.session_state.page == "desarrollo":
    nav_bar("desarrollo")
    st.write("### Desarrollo")

    opcion = st.selectbox(
        "Selecciona una sección para ver los detalles:",
        ("", "Diseño funcional", "Desarrollo backend")
    )

    if opcion == "Diseño funcional":
        st.write("#### 🛠️ Diseño funcional")
        st.write("A continuación se muestra el flujo inicial del prototipo con las pantallas clave:")

        st.markdown("##### Pantalla de bienvenida")
        st.image("images/welcomePage.png", caption="Pantalla de bienvenida (Soy cliente / Entrar como invitado)", width=200)

        st.markdown("⬇️")

        st.markdown("##### Desde la pantalla de bienvenida, el flujo diverge en dos caminos:")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("###### 👉 Flujo 'Soy cliente'")
            st.image("images/inicio sesion.png", caption="Login de cliente", width=200)
            st.markdown("⬇️")
            st.image("images/pagina principal.png", caption="Pantalla principal tras iniciar sesión", width=200)
            st.markdown("*Desde la pantalla principal, el cliente puede gestionar citas, póliza, reportes y más.*")

        with col2:
            st.markdown("###### 👉 Flujo 'Entrar como invitado'")
            st.image("images/no usuario.png", caption="Pantalla principal para invitado", width=200)
            st.markdown("*El invitado accede a información básica, simuladores o contacto.*")

        st.markdown("""
        ---
        **Resumen de flujo:**
        - **Pantalla de bienvenida**: elige entre *Soy cliente* o *Entrar como invitado*.
        - **Flujo cliente**:
            - Login → Pantalla principal de gestión → funcionalidades completas.
        - **Flujo invitado**:
            - Acceso directo a funcionalidades limitadas.
        """)

    elif opcion == "Desarrollo backend":
        st.write("#### 🖥️ Desarrollo backend")
        st.write("A continuación se muestra un diagrama simplificado de la arquitectura propuesta:")

        diagram = gv.Digraph(format='png')
        diagram.attr(rankdir='TB', size='12,8')

        diagram.node('App', '📱 App móvil\nFlutter (Android/iOS)', shape='box', style='filled', color='lightblue')
        diagram.node('API', '🌐 API Gateway', shape='box', style='filled', color='lightskyblue')
        diagram.node('Micro', '🧩 Microservicios Backend', shape='box', style='filled', color='lightcyan')
        diagram.node('Gest', '👤 Gestión Clientes\nDB Relacional', shape='box')
        diagram.node('IA', '🤖 Diagnóstico IA\n📷 CV & 💬 NLP', shape='box')
        diagram.node('Sin', '📝 Siniestros', shape='box')
        diagram.node('Noti', '🔔 Notificaciones', shape='box')
        diagram.node('DBRel', '🗃️ DB Relacional', shape='box', style='filled', color='lightgreen')
        diagram.node('DBNoSQL', '📂 DB NoSQL', shape='box', style='filled', color='lightgreen')
        diagram.node('Cloud', '☁️ Infraestructura Cloud\n🐳 Docker + ☸️ Kubernetes', shape='box', style='filled', color='lightgrey')

        diagram.edges([('App', 'API'), ('API', 'Micro')])
        diagram.edges([('Micro', 'Gest'), ('Micro', 'IA'), ('Micro', 'Sin'), ('Micro', 'Noti')])
        diagram.edge('Gest', 'DBRel')
        diagram.edge('IA', 'DBNoSQL')
        diagram.edge('Micro', 'Cloud')
        diagram.edge('Cloud', 'DBRel')
        diagram.edge('Cloud', 'DBNoSQL')

        st.graphviz_chart(diagram)

# APLICACIÓN
elif st.session_state.page == "aplicacion":
    nav_bar("aplicacion")
    st.write("### Aplicación")
    st.write("Aquí puedes interactuar con la demo de la app:")
    st.markdown("""
    <iframe src="https://axapanel.onrender.com/login" width="375" height="667" style="border:none; border-radius:20px;"></iframe>
    """, unsafe_allow_html=True)
    
# PRESUPUESTO
elif st.session_state.page == "presupuesto":
    nav_bar("presupuesto")
    st.write("### Presupuesto y calendario de desarrollo")

    st.markdown("""
✅ **Estrategia de desarrollo**

- Desarrollo principal externalizado → velocidad.
- Mantenimiento tras MVP → equipo interno.

✅ **Equipo mínimo**

- Internos: PM, Solution Architect.
- Externos: 2 devs móviles, UI/UX, QA.

✅ **Recursos clave**

- Dispositivos Android/iOS.
- Herramientas: Figma, Android Studio, Xcode, Jenkins/GitHub Actions.

✅ **Principales riesgos y mitigaciones**

- Integración APIs: pruebas y docs anticipadas.
- Transferencia conocimiento: handover + formación.
- Seguridad/RGPD: biometría, cifrado, NDA.
- Baja adopción: validar con MVP.
- Cambios requisitos: reuniones semanales.
""")

    if st.button("💰 Calcular presupuesto final"):
        st.success("✅ El coste total estimado del proyecto es de **69,000 €**")

    tasks = [
        dict(Task="Diseño y prototipo", Start='2025-09-01', Finish='2025-09-05', Resource='MVP'),
        dict(Task="Funcionalidades básicas", Start='2025-09-08', Finish='2025-09-26', Resource='MVP'),
        dict(Task="Pruebas MVP", Start='2025-09-29', Finish='2025-10-03', Resource='MVP'),
        dict(Task="Lanzamiento MVP", Start='2025-10-06', Finish='2025-10-06', Resource='MVP'),
        dict(Task="Feedback usuarios", Start='2025-10-06', Finish='2025-10-17', Resource='Feedback'),
        dict(Task="Desarrollo ampliado", Start='2025-10-20', Finish='2025-11-07', Resource='Desarrollo'),
        dict(Task="Pruebas finales", Start='2025-11-10', Finish='2025-11-21', Resource='Desarrollo'),
        dict(Task="Lanzamiento final", Start='2025-11-24', Finish='2025-11-24', Resource='Desarrollo'),
    ]

    fig = ff.create_gantt(
        tasks, 
        index_col='Resource', 
        show_colorbar=True, 
        group_tasks=True, 
        showgrid_x=True, 
        showgrid_y=True,
        title="Calendario de desarrollo: MVP, Feedback y Lanzamiento final"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.write("""
    **Duración estimada:** del **1 sept 2025** al **24 nov 2025** (12 semanas).
    """)
