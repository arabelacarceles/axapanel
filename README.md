# AXA Panel - Proyecto Demo

Este es un proyecto desarrollado como parte del proceso de selección para el **Tech Graduate Program** de AXA. Consta de dos partes:

- Una aplicación interactiva desarrollada con **Streamlit**, que estructura y presenta el caso propuesto.
- Una demo funcional de una app cliente simulada con **Flask**, que representa la interfaz móvil de la propuesta.

---

## 🌐 Enlaces principales

| Plataforma | Enlace |
|------------|--------|
| 🎯 Aplicación principal (Streamlit) | [https://axapanel.streamlit.app/](https://axapanel.streamlit.app/) |
| 📱 Demo de la app simulada (Flask) | [https://axapanel.onrender.com/login](https://axapanel.onrender.com/login) |

---

## 🛠️ Tecnologías utilizadas

- **Python**
- **Streamlit** – Para construir el panel de presentación del caso.
- **Flask** – Para simular la app móvil del cliente.
- **Plotly** – Para mostrar gráficos tipo Gantt.
- **Graphviz** – Para representar la arquitectura backend.
- **HTML/CSS + FullCalendar** – Para la interfaz de la app Flask.

---

## 📁 Estructura del proyecto

```
📦 axa-panel/
├── app.py # Código principal de la app en Streamlit
├── panel.py # Código de la app Flask (demo móvil)
├── requirements.txt # Dependencias necesarias
├── /images # Imágenes utilizadas
├── /static # Recursos estáticos para Flask

```


---

## 🚀 Cómo ejecutarlo localmente

### 1. Clona el repositorio

```bash
git clone https://github.com/tuusuario/axa-panel.git
cd axa-panel

```

### 2. Instala los requisitos

```bash
pip install -r requirements.txt

```

### 3. Ejecutar la app de streamlit
```bash
streamlit run app.py

```

### 4. Ejecutar la app de Flask (opcional)
```bash
python panel.py

```

## ✨ Autor

Arabela Carceles Carrillo

