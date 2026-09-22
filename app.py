import streamlit as st
import datetime
import zoneinfo
import pandas as pd
import numpy as np
import libreria_funciones_proyecto1 as lfp1
import librería_clases_proyecto1 as lcp1
import libreria_gestor_clases as lgc

# ============================================================
# CONFIGURACIÓN VISUAL / DESIGN SYSTEM
# ============================================================
st.set_page_config(
    page_title="Python for Analytics | Módulo 1",
    layout="wide",
    page_icon=":armenia:",  #mis iniciales AM
    initial_sidebar_state="expanded",
)

# Paleta empresarial:
# Navy #0B1F33 | Blue #1769AA | Cyan #19B5FE | Slate #536579
# Success #19A974 | Warning #E9A23B | Danger #D9534F
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #0B1F33;
    --navy-2: #102D47;
    --blue: #1769AA;
    --blue-2: #2185D0;
    --cyan: #19B5FE;
    --text: #182B3A;
    --muted: #637587;
    --surface: #FFFFFF;
    --surface-2: #F4F7FA;
    --border: #DCE5ED;
    --success: #19A974;
    --warning: #E9A23B;
    --danger: #D9534F;
    --shadow: 0 12px 35px rgba(11,31,51,.10);
}

* { font-family: 'Inter', sans-serif; }
.stApp {
    background:
        radial-gradient(circle at 88% 5%, rgba(25,181,254,.09), transparent 25%),
        linear-gradient(180deg, #F7F9FC 0%, #EEF3F7 100%);
    color: var(--text);
}
[data-testid="stHeader"] {
    background: rgba(247,249,252,.78);
    backdrop-filter: blur(12px);
}
.block-container { padding-top: 1.8rem; padding-bottom: 3rem; max-width: 1450px; }

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, var(--navy) 0%, #0E2A43 100%);
    border-right: 1px solid rgba(255,255,255,.08);
}
[data-testid="stSidebar"] * { color: #EAF3FA !important; }
[data-testid="stSidebar"] .stSelectbox > div > div {
    background: rgba(255,255,255,.08);
    border: 1px solid rgba(255,255,255,.15);
    border-radius: 12px;
}
.sidebar-brand {
    padding: 14px 4px 18px;
    margin-bottom: 16px;
    border-bottom: 1px solid rgba(255,255,255,.12);
}
.sidebar-brand .mini {
    color: #8FB2CD;
    font-size: .72rem;
    text-transform: uppercase;
    letter-spacing: .14em;
    font-weight: 700;
}
.sidebar-brand .name {
    font-size: 1.15rem;
    font-weight: 800;
    margin-top: 4px;
}

/* Hero */
.hero {
    position: relative;
    overflow: hidden;
    padding: 30px 34px;
    border-radius: 22px;
    background: linear-gradient(125deg, var(--navy) 0%, #123A5B 62%, #1769AA 100%);
    box-shadow: 0 18px 45px rgba(11,31,51,.18);
    color: white;
    margin-bottom: 24px;
}
.hero:before {
    content: "";
    position: absolute;
    width: 280px; height: 280px;
    right: -80px; top: -130px;
    border-radius: 50%;
    background: rgba(25,181,254,.20);
    filter: blur(2px);
    animation: floatGlow 6s ease-in-out infinite;
}
.hero:after {
    content: "";
    position: absolute;
    width: 160px; height: 160px;
    right: 190px; bottom: -100px;
    border-radius: 50%;
    background: rgba(255,255,255,.08);
    animation: floatGlow 8s ease-in-out infinite reverse;
}
.hero h1 { margin: 0; font-size: clamp(1.7rem, 3vw, 2.5rem); letter-spacing: -.03em; }
.hero p { margin: 9px 0 0; color: #C8D9E7; max-width: 850px; }
.hero .badge {
    display: inline-block;
    padding: 6px 11px;
    border: 1px solid rgba(255,255,255,.18);
    background: rgba(255,255,255,.08);
    border-radius: 999px;
    font-size: .72rem;
    font-weight: 700;
    letter-spacing: .1em;
    text-transform: uppercase;
    margin-bottom: 12px;
}

/* Cards */
.card, .metric-card {
    background: rgba(255,255,255,.94);
    border: 1px solid var(--border);
    border-radius: 18px;
    box-shadow: var(--shadow);
    transition: transform .22s ease, box-shadow .22s ease, border-color .22s ease;
}
.card {
    padding: 22px;
    height: 100%;
}
.card:hover, .metric-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 18px 42px rgba(11,31,51,.15);
    border-color: rgba(33,133,208,.40);
}
.card-icon {
    width: 44px; height: 44px;
    display: grid; place-items: center;
    border-radius: 13px;
    background: linear-gradient(135deg, #E8F4FC, #D9EEFA);
    color: var(--blue);
    font-size: 1.25rem;
    margin-bottom: 14px;
}
.card h3 { margin: 0 0 7px; color: var(--navy); font-size: 1.02rem; }
.card p { margin: 0; color: var(--muted); line-height: 1.6; font-size: .9rem; }

/* Streamlit components */
.stButton > button {
    border: 0 !important;
    border-radius: 11px !important;
    font-weight: 700 !important;
    transition: all .2s ease !important;
    box-shadow: 0 6px 18px rgba(23,105,170,.14) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) scale(1.01);
    box-shadow: 0 10px 24px rgba(23,105,170,.25) !important;
}
.stButton > button:active { transform: translateY(0) scale(.99); }
div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div,
div[data-baseweb="textarea"] {
    border-radius: 11px !important;
    border-color: var(--border) !important;
    transition: box-shadow .2s ease, border-color .2s ease !important;
}
div[data-baseweb="input"] > div:focus-within,
div[data-baseweb="select"] > div:focus-within {
    border-color: var(--blue-2) !important;
    box-shadow: 0 0 0 3px rgba(33,133,208,.12) !important;
}
label { font-weight: 600 !important; color: var(--text) !important; }
[data-testid="stMetric"] {
    background: white;
    padding: 18px 20px;
    border-radius: 16px;
    border: 1px solid var(--border);
    box-shadow: 0 8px 24px rgba(11,31,51,.07);
    transition: transform .2s ease, box-shadow .2s ease;
}
[data-testid="stMetric"]:hover { transform: translateY(-3px); box-shadow: 0 13px 30px rgba(11,31,51,.12); }
[data-testid="stMetricLabel"] { color: var(--muted) !important; }
[data-testid="stMetricValue"] { color: var(--navy) !important; font-weight: 800 !important; }
[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid var(--border);
}
div[data-testid="stExpander"] {
    border: 1px solid var(--border);
    border-radius: 15px;
    background: rgba(255,255,255,.75);
    margin-bottom: 12px;
    box-shadow: 0 5px 18px rgba(11,31,51,.05);
}
div[data-testid="stExpander"] details[open] {
    box-shadow: 0 12px 30px rgba(11,31,51,.08);
}
hr { border-color: var(--border) !important; }
.small-caption {
    color: var(--muted);
    font-size: .82rem;
}
.section-title {
    display: flex; align-items: center; gap: 10px;
    margin: 8px 0 16px;
}
.section-title .line {
    width: 5px; height: 27px; border-radius: 10px;
    background: linear-gradient(180deg, var(--cyan), var(--blue));
}
.section-title h2 { margin: 0; color: var(--navy); font-size: 1.45rem; }

/* Status pills */
.status {
    display: inline-flex; align-items: center; gap: 7px;
    border-radius: 999px; padding: 6px 11px;
    font-size: .76rem; font-weight: 700;
}
.status.ok { background: #E8F8F1; color: #087A51; }
.status.info { background: #E8F3FB; color: #125C91; }
.status.warn { background: #FFF4E3; color: #9A5D00; }

/* Motion */
@keyframes floatGlow {
    0%,100% { transform: translate3d(0,0,0) scale(1); }
    50% { transform: translate3d(-12px,14px,0) scale(1.05); }
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
.main .block-container > div { animation: fadeUp .45s ease both; }

/* Footer */
.footer {
    text-align:center; color:#7A8B99; font-size:.75rem;
    padding:28px 0 8px; border-top:1px solid var(--border); margin-top:30px;
}
</style>
""", unsafe_allow_html=True)

# Pequeño efecto JS visual: halo que sigue el cursor dentro de un panel aislado.
# No modifica la lógica de Streamlit; complementa los efectos CSS.
st.components.v1.html("""
<div id="glow" style="position:fixed;inset:0;pointer-events:none;z-index:0;"></div>
<script>
const glow = document.getElementById("glow");
document.addEventListener("mousemove", e => {
  glow.style.background =
    `radial-gradient(280px circle at ${e.clientX}px ${e.clientY}px,
      rgba(25,181,254,.055), transparent 70%)`;
});
</script>
""", height=0)

# ============================================================
# LÓGICA ORIGINAL
# ============================================================
def obtener_totales(lista):
    ingresos = 0.00
    gastos = 0.00
    for x in lista:
        if x > 0:
            ingresos += x
        else:
            gastos += x * -1
    return {"Ingresos": ingresos, "Gastos": gastos}

HOME = "Home"
EJERCICIO1 = "Ejercicio 1"
EJERCICIO2 = "Ejercicio 2"
EJERCICIO3 = "Ejercicio 3"
EJERCICIO4 = "Ejercicio 4"
FUNCION_ERROR_TXS = "Tasa de error de transacciones"

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:

    try:
        st.image("img/python-for-analytics.png", use_container_width=True)
    except Exception:
        pass

    opcion = st.selectbox(
        "🐬Navegación",
        (HOME, EJERCICIO1, EJERCICIO2, EJERCICIO3, EJERCICIO4),
        index=0,
    )
    st.markdown("""
    <div style="margin-top:24px;padding:14px;border:1px solid rgba(255,255,255,.12);
                border-radius:14px;background:rgba(255,255,255,.05);">
      <div style="font-size:.72rem;color:#8FB2CD;text-transform:uppercase;
                  letter-spacing:.12em;font-weight:700;">Módulo</div>
      <div style="font-weight:700;margin-top:5px;">Python Fundamentals</div>
      <div style="font-size:.76rem;color:#AFC4D4;margin-top:5px;">Aplicación interactiva</div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    try:
        st.image("img/python.png", width=120)
    except Exception:
        pass

# ============================================================
# CABECERA
# ============================================================
st.markdown("""
<div class="hero">
  <div class="badge">Especialización en Python for Analytics</div>
  <h1>Laboratorio interactivo · Módulo 1</h1>
  <p>Una experiencia profesional para explorar listas, NumPy, DataFrames,
     funciones externas y programación orientada a objetos.</p>
</div>
""", unsafe_allow_html=True)

anio = datetime.datetime.now().year
# ============================================================
# HOME
# ============================================================
if opcion == HOME:
    st.markdown("""
    <div class="section-title"><div class="line"></div><h2>Resumen del proyecto</h2></div>
    """, unsafe_allow_html=True)

    c1, c2, c3,c4 = st.columns(4)
    cards = [
        ("01", "Flujo de caja", "Registra ingresos y gastos, calcula totales y visualiza el saldo."),
        ("02", "Ventas con NumPy", "Gestiona ventas de productos mediante arrays y DataFrames."),
        ("03", "Uso de Funciones", "Ejecuta funciones externas administradas desde una librería"),
        ("04", "Programación Orientada a Objetos", "Implementa un CRUD en base a una clase proporcionada."),
    ]
    for col, (num, title, desc) in zip((c1, c2, c3,c4), cards):
        with col:
            st.markdown(f"""
            <div class="card">
              <div class="card-icon">{num}</div>
              <h3>{title}</h3>
              <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

    c1, c2 = st.columns([1.1, 1])
    with c1:
        st.markdown(f"""
        <div class="card">
          <h3>👨‍💻 Elaborado por</h3>
          <p><strong>Anibal Abraham Minaya Cubillas</strong></p>
          <p style="margin-top:10px;">Licenciado en Computación, experiencia como Developer JAVA y Developer Cobol.</p>
          <p><strong>Año : {anio}</strong></p>
          <div style="margin-top:18px;">
            <span class="status info">● Módulo 1 · Python Fundamentals</span>
          </div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="card">
          <h3>🧩 Tecnologías</h3>
          <p>🐍Python · Streamlit · GitHub · NumPy · Pandas · Programación Orientada a Objetos</p>
          <div style="margin-top:18px;">
            <span class="status ok">● Aplicación interactiva</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

    try:
        st.image("img/python-logo.png", width=120)
    except Exception:
        pass

# ============================================================
# EJERCICIO 1
# ============================================================
elif opcion == EJERCICIO1:
    lista_conceptos = []
    lista_tipos_mov = []
    lista_valores = []

    if "LISTA_CONCEPTOS" not in st.session_state:
        st.session_state["LISTA_CONCEPTOS"] = lista_conceptos
        st.session_state["LISTA_TIPO_MOV"] = lista_tipos_mov
        st.session_state["LISTA_VALOR"] = lista_valores
    else:
        lista_conceptos = st.session_state["LISTA_CONCEPTOS"]
        lista_tipos_mov = st.session_state["LISTA_TIPO_MOV"]
        lista_valores = st.session_state["LISTA_VALOR"]

    st.markdown("""
    <div class="section-title"><div class="line"></div><h2>🏦 Ejercicio 1 · Flujo de caja</h2></div>
    <p class="small-caption">Registra movimientos financieros y controla automáticamente ingresos, gastos y saldo.</p>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([2, 1, 1, .8])
    concepto = col1.text_input("Concepto")
    tipo_mov = col2.selectbox("Tipo de movimiento", ("Ingreso", "Gasto"), index=None, placeholder="Seleccione...")
    valor = round(col3.number_input("Valor S/", value=0.00, min_value=0.00, format="%.2f"), 2)
    col4.write("")
    col4.write("")
    if col4.button("＋ Añadir", type="primary", use_container_width=True):
        if concepto.strip() == "":
            st.error("El campo concepto no puede estar vacío.")
        elif tipo_mov is None:
            st.error("Seleccione un tipo de movimiento.")
        elif valor == 0:
            st.error("El campo valor no puede ser cero.")
        else:
            lista_conceptos.append(concepto)
            lista_tipos_mov.append(tipo_mov)
            lista_valores.append(-valor if tipo_mov == "Gasto" else valor)
            st.session_state["LISTA_CONCEPTOS"] = lista_conceptos
            st.session_state["LISTA_TIPO_MOV"] = lista_tipos_mov
            st.session_state["LISTA_VALOR"] = lista_valores
            st.success("Movimiento añadido correctamente.")

    df = pd.DataFrame({
        "Concepto": lista_conceptos,
        "Tipo Movimiento": lista_tipos_mov,
        "Valor": lista_valores
    })
    st.dataframe(df, hide_index=True, use_container_width=True,
                 column_config={"Valor": st.column_config.NumberColumn("Valor", format="S/ %.2f")})

    totales = obtener_totales(lista_valores)
    saldo = totales["Ingresos"] - totales["Gastos"]
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Ingresos", f"S/ {totales['Ingresos']:,.2f}")
    c2.metric("Gastos", f"S/ {totales['Gastos']:,.2f}")
    c3.metric("Saldo", f"S/ {saldo:,.2f}")
    estado = "A favor" if saldo > 0 else "En contra" if saldo < 0 else "Equilibrio"
    c4.metric("Caja", estado, delta=saldo)

# ============================================================
# EJERCICIO 2
# ============================================================
elif opcion == EJERCICIO2:
    arreglo = np.empty((0, 5), dtype=object)
    if "ARREGLO" not in st.session_state:
        st.session_state["ARREGLO"] = arreglo
    else:
        arreglo = st.session_state["ARREGLO"]

    st.markdown("""
    <div class="section-title"><div class="line"></div><h2>💸 Ejercicio 2 · Registro de ventas</h2></div>
    <p class="small-caption">Formulario conectado a arrays de NumPy y visualización mediante DataFrame.</p>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns([2, 2, 1, 1, .8])
    producto = col1.text_input("Producto")
    categoria = col2.selectbox("Categoría", ("Laptop", "PC", "Celular", "Audífono", "Tablet", "Mouse"),
                               index=None, placeholder="Seleccione...")
    precio = round(col3.number_input("Precio S/", min_value=0.00, value=0.00, format="%.2f"), 2)
    cantidad = col4.number_input("Cantidad", min_value=0, value=0)
    col5.write("")
    col5.write("")
    if col5.button("＋ Añadir", type="primary", use_container_width=True):
        if producto.strip() == "":
            st.error("El campo producto no puede estar vacío.")
        elif categoria is None:
            st.error("Seleccione una categoría.")
        elif precio <= 0:
            st.error("El precio debe ser mayor que cero.")
        elif cantidad <= 0:
            st.error("La cantidad debe ser mayor que cero.")
        else:
            total = precio * cantidad
            nuevo_registro = np.array([[producto, categoria, precio, cantidad, total]], dtype=object)
            arreglo = np.vstack((arreglo, nuevo_registro))
            st.session_state["ARREGLO"] = arreglo
            st.success("Venta añadida correctamente.")

    df = pd.DataFrame(arreglo, columns=["Producto", "Categoría", "Precio", "Cantidad", "Total"])
    st.dataframe(df, hide_index=True, use_container_width=True,
                 column_config={
                     "Precio": st.column_config.NumberColumn("Precio", format="S/ %.2f"),
                     "Total": st.column_config.NumberColumn("Total", format="S/ %.2f")
                 })
    venta_total = np.sum(arreglo[:, 4].astype(float)) if arreglo.size else 0
    st.metric("Ventas totales", f"S/ {venta_total:,.2f}")

# ============================================================
# EJERCICIO 3
# ============================================================
elif opcion == EJERCICIO3:
    st.markdown("""
    <div class="section-title"><div class="line"></div><h2>📆 Ejercicio 3 · Funciones externas</h2></div>
    <p class="small-caption">Invoca una función de la librería <code>libreria_funciones_proyecto1.py</code>.</p>
    """, unsafe_allow_html=True)

    funcion = st.selectbox("Función", (FUNCION_ERROR_TXS,), index=None, placeholder="Seleccione una función...")
    arreglo_historico = np.empty((0, 5), dtype=object)
    if "ARREGLO_HIST" not in st.session_state:
        st.session_state["ARREGLO_HIST"] = arreglo_historico
    else:
        arreglo_historico = st.session_state["ARREGLO_HIST"]

    if funcion == FUNCION_ERROR_TXS:
        c1, c2, c3 = st.columns([1, 1, .6])
        fallidas = c1.number_input("Transacciones fallidas", value=0)
        totales = c2.number_input("Transacciones totales", value=0)
        fecha = datetime.datetime.now(zoneinfo.ZoneInfo("America/Lima"))
        fecha_formato = fecha.strftime("%Y/%m/%d %H:%M:%S")

        if c3.button("▶ Ejecutar", type="primary", use_container_width=True):
            try:
                resultado = lfp1.calcular_tasa_error_transacciones(fallidas, totales)
                error = resultado["tasa_error_pct"]
                exito = resultado["tasa_exito_pct"]
                st.success(f"Función ejecutada correctamente · Error: {error} · Éxito: {exito}")
            except Exception as e:
                error = "Error"
                exito = "Error"
                st.error(f"Error: {e}")

            nuevo_registro = np.array([[fallidas, totales, error, exito, fecha_formato]], dtype=object)
            arreglo_historico = np.vstack((arreglo_historico, nuevo_registro))
            st.session_state["ARREGLO_HIST"] = arreglo_historico

        st.markdown("#### Histórico de ejecuciones")
        df = pd.DataFrame(arreglo_historico,
                          columns=["TXs Fallidas", "TXs Totales", "Tasa Error", "Tasa Éxito", "Fecha"])
        st.dataframe(df, hide_index=True, use_container_width=True)

# ============================================================
# EJERCICIO 4
# ============================================================
elif opcion == EJERCICIO4:
    st.markdown("""
    <div class="section-title"><div class="line"></div><h2>🏢 Ejercicio 4 · Gestión de servidores</h2></div>
    <p class="small-caption">CRUD sobre la clase <code>Servidor</code> mediante una librería externa.</p>
    """, unsafe_allow_html=True)

    gestor_serv = lgc.GestorServidores()
    if "GESTOR_SERV" not in st.session_state:
        st.session_state["GESTOR_SERV"] = gestor_serv
    else:
        gestor_serv = st.session_state["GESTOR_SERV"]

    with st.expander("➕ Agregar servidor", expanded=False):
        c1, c2, c3 = st.columns(3)
        nombre = c1.text_input("Nombre del servidor")
        tiempo_total = c2.number_input("Tiempo total de operación (h)")
        tiempo_caida = c3.number_input("Tiempo de caída (h)")
        c4, c5, c6 = st.columns(3)
        almac_total = c4.number_input("Almacenamiento total (GB)")
        almac_usado = c5.number_input("Almacenamiento usado (GB)")
        if c6.button("Agregar servidor", type="primary", use_container_width=True):
            if nombre.strip() == "":
                st.error("El campo nombre no puede estar vacío.")
            elif tiempo_total <= 0:
                st.error("El tiempo total debe ser mayor que cero.")
            elif almac_total <= 0:
                st.error("El almacenamiento total debe ser mayor que cero.")
            else:
                servidor = lcp1.Servidor(nombre, tiempo_total, tiempo_caida, almac_total, almac_usado)
                try:
                    gestor_serv.crear_servidor(servidor)
                    st.success(f"Servidor {nombre} creado exitosamente.")
                except ValueError as e:
                    st.error(f"Error: {e}")

    with st.expander("✏️ Actualizar servidor", expanded=False):
        nombres = gestor_serv.mostrar_nombres_servidores()
        nombre = st.selectbox("Servidor", nombres, index=None, placeholder="Seleccione...")
        c1, c2 = st.columns(2)
        tiempo_total = c1.number_input("Nuevo tiempo total de operación (h)")
        tiempo_caida = c2.number_input("Nuevo tiempo de caída (h)")
        c3, c4, c5 = st.columns([1, 1, .8])
        almac_total = c3.number_input("Nuevo almacenamiento total (GB)")
        almac_usado = c4.number_input("Nuevo almacenamiento usado (GB)")
        if c5.button("Actualizar", type="primary", use_container_width=True):
            if tiempo_total <= 0:
                st.error("El tiempo total debe ser mayor que cero.")
            elif almac_total <= 0:
                st.error("El almacenamiento total debe ser mayor que cero.")
            elif nombre is None:
                st.error("Seleccione un servidor.")
            else:
                encontrado = False
                for serv in gestor_serv.servidores:
                    if serv.nombre == nombre:
                        serv.tiempo_total_h = tiempo_total
                        serv.tiempo_caida_h = tiempo_caida
                        serv.almacenamiento_total_gb = almac_total
                        serv.almacenamiento_usado_gb = almac_usado
                        encontrado = True
                        break
                if encontrado:
                    st.success(f"Servidor {nombre} actualizado exitosamente.")
                else:
                    st.error(f"Servidor con nombre {nombre} no encontrado.")

    with st.expander("🗑️ Eliminar servidor", expanded=False):
        nombres = gestor_serv.mostrar_nombres_servidores()
        nombre = st.selectbox("Servidor a eliminar", nombres, index=None, placeholder="Seleccione...")
        if st.button("Eliminar servidor", type="primary"):
            try:
                gestor_serv.eliminar_servidor(nombre)
                st.success(f"Servidor {nombre} eliminado exitosamente.")
            except Exception as e:
                st.error(f"Error: {e}")

    with st.expander("📊 Ver servidores", expanded=True):
        array_serv = gestor_serv.mostrar_info_servidores()
        df = pd.DataFrame(array_serv, columns=[
            "Nombre Servidor", "Tiempo Total (hrs)", "Tiempo Caída (hrs)",
            "Almacenamiento Total (GB)", "Almacenamiento Usado (GB)",
            "Disponibilidad (%)*", "Uso Almacenamiento (%)*", "Estado*"
        ])
        st.dataframe(df, hide_index=True, use_container_width=True)

# ============================================================
# FOOTER
# ============================================================
st.markdown(f"""
<div class="footer">
  Python for Analytics · Módulo 1 · Interface profesional ·
  <span style="font-weight:600;">{anio}</span>
</div>
""", unsafe_allow_html=True)
