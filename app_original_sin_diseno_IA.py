import streamlit as st
import datetime
import zoneinfo
import pandas as pd
import numpy as np
import libreria_funciones_proyecto1 as lfp1
import librería_clases_proyecto1 as lcp1
import libreria_gestor_clases as lgc

#funcion para el ejercicio 1, para obtener totales de ingresos y gastos
def obtener_totales(lista):
   ingresos = 0.00
   gastos = 0.00
   for x in lista:
       if x > 0:
            ingresos = ingresos + x
       else:
            gastos = gastos + (x*-1)
   return {
        "Ingresos": ingresos,
        "Gastos"  : gastos
        } 

#opciones del selectbox
HOME       = "Home"
EJERCICIO1 = "Ejercicio 1"
EJERCICIO2 = "Ejercicio 2"
EJERCICIO3 = "Ejercicio 3"
EJERCICIO4 = "Ejercicio 4"

FUNCION_ERROR_TXS = "Tasa de error de transacciones"

# Configuración de la página
st.set_page_config(
    page_title="Especialización en Python for Analytics - Módulo 1",
    layout="wide",
    page_icon=":armenia:"  #mis iniciales AM
)

st.title("Especialización en Python for Analytics",text_alignment="center")

#crea tres columnas para mostrar la imagen centrada
col1, col2, col3 = st.columns(3)
#coloca la imagen en la columna del medio
col2.image("img/python-logo.png")

#en la barra lateral izq muestra la imagen y crea el select box
st.sidebar.image("img/python-for-analytics.png")
opcion = st.sidebar.selectbox(
    "**Seleccione una opción**",
    (HOME, EJERCICIO1, EJERCICIO2, EJERCICIO3, EJERCICIO4),
    index=0
)

if opcion == HOME:
  #página home de presentación del proyecto
  st.header("👨‍🎓 Elaborado por: ",text_alignment ="center")
  st.subheader("Anibal Abraham Minaya Cubillas",text_alignment ="center")
  st.header("Módulo:",text_alignment ="center")
  st.subheader("Módulo 1: Python Fundamentals",text_alignment ="center")
  st.header("Información general del estudiante:",text_alignment ="center")
  st.subheader("Me he desempeñado como Developer JAVA y Developer Cobol",text_alignment ="center")
  st.header("Año:",text_alignment ="center")
  st.subheader(f"{datetime.datetime.now().year}",text_alignment ="center")
  st.header("Breve descripción del proyecto:",text_alignment ="center")
  st.subheader("Aplicación interactiva en Streamlit que integra los conceptos",text_alignment ="center")
  st.subheader("aprendidos durante el Módulo 1 del curso, que incluyen, entre otros,",text_alignment ="center")
  st.subheader("el uso de listas, arrays, DataFrames, funciones y clases (POO)",text_alignment ="center")          
  st.write("")
  st.write("")
  st.header("Tecnologías utilizadas:",text_alignment ="center")
  col1, col2, col3 = st.columns(3)
  col1.image("img/python-logo.png")
  col2.image("img/streamlit.png")
  col3.image("img/github.png")
elif opcion == EJERCICIO1:
  #Ejercicio 1 – Flujo de caja con listas
  #inicializa listas
  lista_conceptos = []
  lista_tipos_mov = []
  lista_valores   = []
  
  #Verifica si existen las variables de sesion: lista de conceptos, tipos y montos
  #si no existen, las inicializa, si existen, las recupera
  
  if 'LISTA_CONCEPTOS' not in st.session_state:
    st.session_state['LISTA_CONCEPTOS'] = lista_conceptos
    st.session_state['LISTA_TIPO_MOV'] = lista_tipos_mov
    st.session_state['LISTA_VALOR'] = lista_valores
  else:
    lista_conceptos = st.session_state['LISTA_CONCEPTOS']
    lista_tipos_mov = st.session_state['LISTA_TIPO_MOV']
    lista_valores   = st.session_state['LISTA_VALOR']

  st.header("🏦 Ejercicio 1 – Flujo de caja con listas")
  st.markdown("**En este ejercicio se desarrolla un módulo para registrar movimientos financieros en una lista vacía.**")
  #crea 4 columnas para mostrar los elementos del formulario en forma horizontal
  col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

  concepto = col1.text_input("Concepto")
  tipo_mov = col2.selectbox("Tipo Movimiento",("Ingreso","Gasto"),index=None,placeholder="Seleccione...")
  valor = round(col3.number_input("Valor S/",value=0.00,min_value=0.00,format="%.2f"),2)
  col4.write("")
  col4.write("")
  if col4.button("Añadir",type="primary"):
      if concepto.strip() == "":
          st.error("El campo concepto no puede estar vacío.")
      elif tipo_mov == None:
          st.error("Seleccione un tipo de movimiento")
      elif valor == 0:
          st.error("El campo valor no puede ser cero.")
      elif valor < 0:
          st.error("El campo valor no puede ser menor a cero.")
      else:
          lista_conceptos.append(concepto)
          lista_tipos_mov.append(tipo_mov)
          if tipo_mov == "Gasto":
              lista_valores.append(valor*-1)
          else:
              lista_valores.append(valor)
          st.session_state['LISTA_CONCEPTOS'] = lista_conceptos
          st.session_state['LISTA_TIPO_MOV'] = lista_tipos_mov
          st.session_state['LISTA_VALOR'] = lista_valores
          st.success("El movimiento se añadió a la lista")

  diccionario_datos = {"Concepto" : lista_conceptos, "Tipo Movimiento" : lista_tipos_mov, "Valor" : lista_valores}
  df = pd.DataFrame(diccionario_datos)
  df.style.format( { "Valor" : "S/ {:.2f}" } )
  st.dataframe(df, hide_index=True,column_config={"Valor": st.column_config.NumberColumn("Valor", format="S/ %.2f")})
  totales = obtener_totales(lista_valores)
  col1, col2, col3, col4 = st.columns(4)
  col1.metric("Ingresos", totales["Ingresos"], format="S/ %.2f")
  col2.metric("Gastos", totales["Gastos"], format="S/ %.2f")
  saldo = totales["Ingresos"] - totales["Gastos"]
  col3.metric("Saldo", saldo, format="S/ %.2f")
  if saldo > 0:
     col4.metric("Caja","A favor",delta=saldo, format="S/ %.2f")
  elif saldo < 0:
     col4.metric("Caja","En contra",delta=saldo, format="S/ %.2f")
  else:
     col4.metric("Caja","Equilibrio",delta=saldo, format="S/ %.2f")
elif opcion == EJERCICIO2:
  #Ejercicio 2 – Registro con NumPy, arrays y DataFrame
  #inicializa array
  arreglo=np.empty((0, 5), dtype=object)
  
  if 'ARREGLO' not in st.session_state:
    st.session_state['ARREGLO'] = arreglo
  else:
    arreglo = st.session_state['ARREGLO']

  st.header("💸 Ejercicio 2 – Registro con NumPy, arrays y DataFrame")
  st.markdown("**En este ejercicio se desarrolla un formulario para registrar ventas usando arreglos de `NumPy`.**")
  #crea 5 columnas para mostrar los elementos del formulario en forma horizontal
  col1, col2, col3, col4, col5 = st.columns([2, 2, 1, 1, 1])

  producto = col1.text_input("Producto")
  categoria = col2.selectbox("Categoria",("Laptop","PC","Celular","Audifono","Tablet","Mouse"),index=None,placeholder="Seleccione...")
  precio = round(col3.number_input("Precio S/",min_value=0.00,value=0.00,format="%.2f"),2)
  cantidad = col4.number_input("Cantidad",min_value=0,value=0)
  col5.write("")
  col5.write("")
  if col5.button("Añadir",type="primary"):
      if producto.strip() == "":
          st.error("El campo producto no puede estar vacío.")
      elif categoria == None:
          st.error("Seleccione una categoria")
      elif precio <= 0:
          st.error("El campo precio no puede ser menor o igual a cero.")
      elif cantidad <= 0:
          st.error("El campo cantidad no puede ser menor o igual a cero.")
      else:
          total = precio * cantidad
          nuevo_registro = np.array([[producto, categoria, precio, cantidad, total]], dtype=object)
          arreglo = np.vstack((arreglo, nuevo_registro)) #no funcionó con append
          
          st.session_state['ARREGLO'] = arreglo
          st.success("El movimiento se añadió a la lista")

  df = pd.DataFrame(arreglo, columns=["Producto", "Categoría", "Precio", "Cantidad", "Total"])
  df.style.format( { "Total" : "S/ {:.2f}" } )
  st.dataframe(df, hide_index=True,column_config={"Total": st.column_config.NumberColumn("Total", format="S/ %.2f")})

  venta_total = np.sum(arreglo[:, 4].astype(float))
  st.metric("Ventas Totales", f"S/ {venta_total:,.2f}")
elif opcion == EJERCICIO3:
  st.header("📆 Ejercicio 3 – Uso de funciones desde una librería externa")
  st.markdown("**En este ejercicio se invoca una función de la librería `libreria_funciones_proyecto1.py`**")

  funcion = st.selectbox("**Función**",("Tasa de error de transacciones"),index=None,placeholder="Seleccione una función...")
  #inicializa array
  arreglo_historico=np.empty((0, 5), dtype=object)

  if 'ARREGLO_HIST' not in st.session_state:
      st.session_state['ARREGLO_HIST'] = arreglo_historico
  else:
      arreglo_historico = st.session_state['ARREGLO_HIST']
        
  if funcion == FUNCION_ERROR_TXS:
    fallidas = st.number_input("Transacciones fallidas",value=0)
    totales  = st.number_input("Transacciones totales",value=0)
    fecha = datetime.datetime.now(zoneinfo.ZoneInfo("America/Lima"))
    fecha_formato = fecha.strftime("%Y/%m/%d %H:%M:%S")

    if st.button("Ejecutar",type="primary"):
       try:
          resultado = lfp1.calcular_tasa_error_transacciones(fallidas,totales)
          error = resultado["tasa_error_pct"]
          exito = resultado["tasa_exito_pct"]
          st.success(f"Función ejecutada correctamente. **Resultado:** Tasa de error PCT: {error}. Tasa de éxito PCT: {exito}")
       except Exception as e:
          error = "Error"
          exito = "Error"
          st.error(f"Error: {e}")
       nuevo_registro = np.array([[fallidas, totales, error, exito, fecha_formato]], dtype=object)
       arreglo_historico = np.vstack((arreglo_historico, nuevo_registro))
       st.session_state['ARREGLO_HIST'] = arreglo_historico
    st.markdown("**Histórico de ejecuciones**")   
    df = pd.DataFrame(arreglo_historico, columns=["TXs Fallidas", "TXs Totales", "Tasa Error", "Tasa Exito", "Fecha"])
    st.dataframe(df, hide_index=True)
        
elif opcion == EJERCICIO4:
    st.header("🏢 Ejercicio 4 – Uso de clases desde una librería externa con CRUD")
    st.markdown("**En este ejercicio se conecta una clase de la librería `libreria_clases_proyecto1.py`. Clase elegida: `Servidor`**")
    st.header("🖥️ Gestión de Servidores")

    gestor_serv = lgc.GestorServidores()
    if 'GESTOR_SERV' not in st.session_state:
        st.session_state['GESTOR_SERV'] = gestor_serv
    else:
        gestor_serv = st.session_state['GESTOR_SERV']

    with st.expander("Agregar Servidor"):
       nombre = st.text_input("Nombre del servidor")
       tiempo_total = st.number_input("Tiempo total de operación en horas")
       tiempo_caida = st.number_input("Tiempo caída en horas")
       almac_total  = st.number_input("Almacenamiento total en GB")
       almac_usado  = st.number_input("Almacenamiento usado en GB")
       if st.button("Agregar Servidor",type="primary"):
        if nombre.strip() == "":
            st.error("El campo nombre no puede estar vacío.")
        elif tiempo_total <= 0:
            st.error("El campo tiempo total no puede ser menor o igual a cero.")
        elif almac_total <= 0:
            st.error("El campo almacenamiento total no puede ser menor o igual a cero.")
        else:
            servidor = lcp1.Servidor(nombre,tiempo_total,tiempo_caida,almac_total,almac_usado)
            try:
                gestor_serv.crear_servidor(servidor)
                st.success(f"Servidor {nombre} creado exitosamente.")
            except ValueError as e:
                st.error(f"Error: {str(e)}")
    with st.expander("Actualizar Servidor"):
       nombre = st.selectbox("Nombre del servidor a actualizar", gestor_serv.mostrar_nombres_servidores(), 
                             index=None, placeholder="Seleccione...")
       tiempo_total = st.number_input("Nuevo Tiempo total de operación en horas")
       tiempo_caida = st.number_input("Nuevo Tiempo caída en horas")
       almac_total  = st.number_input("Nuevo Almacenamiento total en GB")
       almac_usado  = st.number_input("Nuevo Almacenamiento usado en GB")
       if st.button("Actualizar Servidor",type="primary"):
          if tiempo_total <= 0:
            st.error("El campo tiempo total no puede ser menor o igual a cero.")
          elif almac_total <= 0:
            st.error("El campo almacenamiento total no puede ser menor o igual a cero.")
          else:
            for serv in gestor_serv.servidores:
                if serv.nombre == nombre:
                    serv.tiempo_total_h = tiempo_total
                    serv.tiempo_caida_h = tiempo_caida
                    serv.almacenamiento_total_gb = almac_total
                    serv.almacenamiento_usado_gb = almac_usado
                    st.success(f"Servidor {nombre} actualizado exitosamente.")
                    break
                else:
                    st.error(f"Servidor con nombre {nombre} no encontrado.")
    with st.expander("Eliminar Servidor"):
       nombre = st.selectbox("Nombre del servidor a eliminar", gestor_serv.mostrar_nombres_servidores(), 
                                    index=None, placeholder="Seleccione...")
       if st.button("Eliminar Servidor",type="primary"):
           try:
               gestor_serv.eliminar_servidor(nombre)
               st.success(f"Servidor {nombre} eliminado exitosamente.")
           except Exception as e:
               st.error(f"Error: {e}")
    with st.expander("Ver Servidores"):
           st.markdown("**Lista de Servidores y resultado de invocación de los métodos de la clase `Servidor`**")
           array_serv = gestor_serv.mostrar_info_servidores()
           df = pd.DataFrame(array_serv, columns=["Nombre", "Tiempo Total(hrs)", "Tiempo Caída(hrs)",
                                                  "Almacenamiento Total(GB)", "Almacenamiento Usado(GB)",
                                                  "Disponibilidad(%)*",
                                                  "Uso Almacenamiento(%)*",
                                                  "Estado*"])
           st.dataframe(df, hide_index=True)
