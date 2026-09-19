import streamlit as st
import datetime
import pandas as pd
import numpy as np
import libreria_funciones_proyecto1 as lfp1

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
    page_icon=":armenia:"  #mis iniciales AM
)

st.title("Especialización en Python for Analytics",text_alignment="center")

#crea tres columnas para mostrar la imagen centrada
col1, col2, col3 = st.columns(3)
#coloca la imagen en la columna del medio
col2.image("python-logo.png")

#en la barra lateral izq muestra la imagen y crea el select box
st.sidebar.image("python-logo.png")
opcion = st.sidebar.selectbox(
    "**Seleccione una opción**",
    (HOME, EJERCICIO1, EJERCICIO2, EJERCICIO3, EJERCICIO4),
    index=0
)

if opcion == HOME:
  #página home de presentación del proyecto
  #st.subheader("Módulo 1")
  st.write("Elaborado por Anibal Abraham Minaya Cubillas")
  st.write("Módulo 1")
  st.write("Información general del estudiante")  
  st.write(f"Año: {datetime.datetime.now().year}")
  st.write("Breve descripción del proyecto")
  st.write("Tecnologías utilizadas")
elif opcion == EJERCICIO1:
  #Ejercicio 1 – Flujo de caja con listas
  #inicializa listas
  lista_conceptos = []
  lista_tipos_mov = []
  lista_valores   = []
  """
  Verifica si existen las variables de sesion: lista de conceptos, tipos y montos
  si no existen, las inicializa, si existen, las recupera
  """
  if 'LISTA_CONCEPTOS' not in st.session_state:
    st.session_state['LISTA_CONCEPTOS'] = lista_conceptos
    st.session_state['LISTA_TIPO_MOV'] = lista_tipos_mov
    st.session_state['LISTA_VALOR'] = lista_valores
  else:
    lista_conceptos = st.session_state['LISTA_CONCEPTOS']
    lista_tipos_mov = st.session_state['LISTA_TIPO_MOV']
    lista_valores   = st.session_state['LISTA_VALOR']

  st.markdown("**Ejercicio 1 – Flujo de caja con listas**")
  st.markdown("En este ejercicio se desarrolla un módulo para registrar movimientos financieros en una lista vacía.")
  #crea 4 columnas para mostrar los elementos del formulario en forma horizontal
  col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

  concepto = col1.text_input("Concepto")
  tipo_mov = col2.selectbox("Tipo Movimiento",("Ingreso","Gasto"),index=None,placeholder="Seleccione...")
  valor = round(col3.number_input("Valor S/",value=0.00,format="%.2f"),2)
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
  col1.write(f"Ingresos : {totales["Ingresos"]}")
  col2.write(f"Gastos   : {totales["Gastos"]}")
  saldo = totales["Ingresos"] - totales["Gastos"]
  col3.write(f"Saldo   :  {saldo}")
  if saldo > 0:
     col4.metric("Saldo","A favor",delta=saldo,label_visibility="hidden")
  elif saldo < 0:
     col4.metric("Saldo","En contra",delta=saldo,label_visibility="hidden")
  else:
     col4.metric("Saldo","Equilibrio",delta=saldo,label_visibility="hidden")
elif opcion == EJERCICIO2:
  #Ejercicio 2 – Registro con NumPy, arrays y DataFrame
  #inicializa array
  arreglo=np.empty((0, 5), dtype=object)
  
  if 'ARREGLO' not in st.session_state:
    st.session_state['ARREGLO'] = arreglo
  else:
    arreglo = st.session_state['ARREGLO']

  st.markdown("**Ejercicio 2 – Registro con NumPy, arrays y DataFrame**")
  st.markdown("ddfvdfEn este ejercicio se desarrolla un módulo para registrar movimientos financieros en una lista vacía.")
  #crea 5 columnas para mostrar los elementos del formulario en forma horizontal
  col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])

  producto = col1.text_input("Producto")
  categoria = col2.selectbox("Categoria",("Laptop","PC","Mouse","Audifono"),index=None,placeholder="Seleccione...")
  precio = round(col3.number_input("Precio S/",value=0.00,format="%.2f"),2)
  cantidad = col4.number_input("Cantidad",value=0)
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
 
elif opcion == EJERCICIO3:
  st.markdown("**Ejercicio 3 – Uso de funciones desde una librería externa**")
  st.markdown("ddfvdfEn este ejercicio se desarrolla un módulo para registrar movimientos financieros en una lista vacía.")

  funcion = st.selectbox("Función",("Tasa de error de transacciones"),index=None,placeholder="Seleccione una función...")
  #inicializa array
  arreglo_historico=np.empty((0, 5), dtype=object)

  if funcion == FUNCION_ERROR_TXS:
     if 'ARREGLO_HIST' not in st.session_state:
        st.session_state['ARREGLO_HIST'] = arreglo
     else:
        arreglo_historico = st.session_state['ARREGLO_HIST']
           
     fallidas = st.number_input("Transacciones fallidas",value=0)
     totales  = st.number_input("Transacciones totales",value=0)
     if st.button("Ejecutar",type="primary"):
        resultado = lfp1.calcular_tasa_error_transacciones(fallidas,totales)
        st.write(f"Tasa de error PCT: {resultado["tasa_error_pct"]}")
        st.write(f"Tasa de éxito PCT: {resultado["tasa_exito_pct"]}")

        nuevo_registro = np.array([[fallidas, totales, resultado["tasa_error_pct"], resultado["tasa_exito_pct"], "fecha"]], dtype=object)
        arreglo_historico = np.vstack((arreglo_historico, nuevo_registro))
        df = pd.DataFrame(arreglo_historico, columns=["TXs Fallidas", "TXs Totales", "Tasa Error", "Tasa Exito", "Fecha"])
        st.dataframe(df, hide_index=True)
        
  
        
#elif opcion == EJERCICIO4:

