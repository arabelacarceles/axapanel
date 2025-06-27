from flask import Flask, render_template_string, request, redirect, url_for, jsonify, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = "clave_super_secreta"

citas = []
puntos = 0

TEMPLATE_CLIENTE = """
<!doctype html>
<html lang="es"><head>
  <meta charset="utf-8">
  <title>Panel Cliente</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/fullcalendar@6.1.8/index.global.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/fullcalendar@6.1.8/index.global.min.js"></script>
  <style>
    body {
      margin:0; padding:0; height:100vh;
      display:flex; justify-content:center; align-items:center;
      background:#cbcbf8; font-family:'Poppins', sans-serif;
    }
    .frame {
      width:375px; height:667px; background:white; border-radius:30px;
      box-shadow:0 0 20px rgba(0,0,0,0.2); overflow:hidden; position:relative;
    }
    .header {
      display:flex; align-items:center; padding:10px 20px; background:white;
    }
    .logo {width:50px; margin-right:auto;}
    .menu-icon {font-size:22px; cursor:pointer; color:#00008f;}
    .content {padding:10px;}
    #calendar {max-width:100%; margin-top:10px; font-size:0.7em;}
    .fc-toolbar-title {
      font-size:1.1em !important; color:#00008f; text-transform:capitalize;
    }
    .fc-button {
      font-size:0.6em !important; padding:4px 6px !important;
      background:#00008f !important; border:none !important; border-radius:6px !important;
    }
    .fc-button:hover {background:#000060 !important;}
    .add-cita-btn {
      width:100%; margin-top:10px; background:#00008f; color:white;
      border:none; padding:12px; border-radius:10px; font-size:1em; cursor:pointer;
    }
    .chatbot-btn {
      position: absolute; bottom: 20px; right: 20px; width: 55px; height: 55px;
      border-radius:50%; box-shadow:0 0 10px rgba(0,0,0,0.3); cursor:pointer;
    }
    .modal, .modal-puntos {
      display:none; position:absolute; top:0; left:0; width:100%; height:100%;
      background: rgba(0,0,0,0.5); justify-content:center; align-items:center;
      z-index:1000;
    }
    .modal-content, .puntos-content {
      background:#cbcbf8; color:#00008f; padding:20px; border-radius:20px;
      text-align:center; width:80%; position:relative;
    }
    .modal-content button, .puntos-content button {
      width:45%; margin:5px; font-size:1em;
    }
    .close-btn {
      position:absolute; top:10px; right:15px; font-size:20px; cursor:pointer;
    }
  </style>
</head>
<body>
  <div class="frame">
    <div class="modal" id="consejoModal">
      <div class="modal-content">
        <span class="close-btn" onclick="cerrarModal('consejoModal'); marcarPosponer();">❌</span>
        <h2>Tarea del día 🐾</h2>
        <p>{{ consejo }}</p>
        <div>
          <button onclick="marcarHecho()">✅ Hecho</button>
          <button onclick="cerrarModal('consejoModal'); marcarPosponer();">⏰ Posponer</button>
        </div>
      </div>
    </div>
    <div class="modal-puntos" id="puntosModal">
      <div class="puntos-content">
        <span class="close-btn" onclick="cerrarModal('puntosModal')">❌</span>
        <p id="puntosMensaje"></p>
      </div>
    </div>
    <div class="header">
      <img src="/static/logo.png" alt="AXA Logo" class="logo">
      <div class="menu-icon" onclick="alert('Menú en construcción')">&#9776;</div>
    </div>
    <div class="content">
      <h2 style="text-align:center;font-size:1em; margin-bottom:5px;">🎉 Bienvenido, {{ usuario }}</h2>
      <div id='calendar'></div>
      <a href="{{ url_for('nueva_cita') }}"><button class="add-cita-btn">➕ Añadir cita</button></a>
    </div>
    <img src="/static/chatbot.png" alt="Chatbot" class="chatbot-btn" onclick="alert('¡Hola! Soy tu asistente virtual 🐾')">
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      {% if show_popup %}
      document.getElementById('consejoModal').style.display = 'flex';
      {% endif %}
      var calendarEl = document.getElementById('calendar');
      var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        height: 320,
        locale: 'es',
        headerToolbar: { left:'prev,next', center:'title', right:'' },
        events: [
          {% for c in citas %}
          { title:"🐾 {{ c['motivo'] }}", start:"{{ c['fecha'] }}" },
          {% endfor %}
        ],
        dayCellDidMount: function(info) {
          const dateStr = info.date.toISOString().split('T')[0];
          const hoy = new Date().toISOString().split('T')[0];
          if (dateStr === hoy) {
            info.el.style.backgroundColor = '#cbcbf8';
          }
        }
      });
      calendar.render();
    });

    function cerrarModal(id) {
      document.getElementById(id).style.display='none';
    }

    function marcarHecho() {
      fetch('/sumar_punto').then(response => response.json()).then(data => {
        document.getElementById('consejoModal').style.display='none';
        document.getElementById('puntosMensaje').innerText = "🎉 ¡Has ganado 1 punto! Te quedan " + data.faltan + " para obtener una recompensa.";
        document.getElementById('puntosModal').style.display='flex';
      });
    }

    function marcarPosponer() {
      fetch('/posponer');
    }
  </script>
</body></html>
"""

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        session.clear()  # limpiar popups al iniciar sesión de nuevo
        return redirect(url_for("panel_cliente", usuario=usuario))
    return """
    <!doctype html><html><head>
      <title>Login Cliente</title>
      <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
    </head><body style="display:flex; justify-content:center; align-items:center; height:100vh; background:#cbcbf8; font-family:'Poppins', sans-serif;">
      <div style="width:375px;height:667px;background:white;border-radius:30px;box-shadow:0 0 20px rgba(0,0,0,0.2);overflow-y:auto;padding:20px;box-sizing:border-box;">
        <h1 style="text-align:center;">🔐 Iniciar sesión</h1>
        <form method="POST" action="/login">
          Usuario:<br><input type="text" name="usuario" style="width:100%;" required><br>
          Contraseña:<br><input type="password" name="password" style="width:100%;" required><br><br>
          <input type="submit" value="Entrar" style="width:100%;font-size:1.2em;">
        </form>
      </div>
    </body></html>
    """

@app.route("/cliente/<usuario>")
def panel_cliente(usuario):
    global puntos
    usuario_fmt = usuario.capitalize()
    consejos = [
        "🐶 Recuerda cepillar a tu perro para evitar enredos.",
        "🐱 Dedica 5 minutos a jugar con tu gato.",
        "🐾 Asegúrate de que tu mascota tenga agua fresca."
    ]
    consejo = random.choice(consejos)

    show_popup = not session.get("popup_shown", False)
    return render_template_string(TEMPLATE_CLIENTE, usuario=usuario_fmt, citas=citas, consejo=consejo, show_popup=show_popup)

@app.route("/sumar_punto")
def sumar_punto():
    global puntos
    puntos += 1
    session["popup_shown"] = True
    faltan = max(0, 40 - puntos)
    return jsonify({"puntos": puntos, "faltan": faltan})

@app.route("/posponer")
def posponer():
    session["popup_shown"] = True
    return jsonify({"status": "ok"})

@app.route("/nueva_cita", methods=["GET", "POST"])
def nueva_cita():
    if request.method == "POST":
        fecha = request.form["fecha"]
        hora = request.form["hora"]
        motivo = request.form["motivo"]
        citas.append({"fecha": fecha, "hora": hora, "motivo": motivo})
        return redirect(url_for("panel_cliente", usuario="Cliente"))
    return """
    <!doctype html><html><head>
      <title>Añadir cita</title>
      <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
    </head><body style="display:flex;justify-content:center;align-items:center;height:100vh;background:#cbcbf8;font-family:'Poppins',sans-serif;">
      <div style="width:375px;height:667px;background:white;border-radius:30px;box-shadow:0 0 20px rgba(0,0,0,0.2);overflow-y:auto;padding:20px;box-sizing:border-box;">
        <h1 style="text-align:center;">🗓️ Añadir nueva cita</h1>
        <form method="POST" action="/nueva_cita">
          Fecha:<br><input type="date" name="fecha" style="width:100%;" required><br>
          Hora:<br><input type="time" name="hora" style="width:100%;" required><br>
          Motivo:<br><input type="text" name="motivo" style="width:100%;" required><br><br>
          <input type="submit" value="Guardar cita" style="width:100%;font-size:1.2em;">
        </form>
      </div>
    </body></html>
    """

if __name__ == "__main__":
    app.run(debug=True)
