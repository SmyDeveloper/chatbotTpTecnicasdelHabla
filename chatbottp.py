import streamlit as st
from groq import Groq


# Configuración básica

# Le agregamos el nombre a la pestaña y un ícono. Esta configuración tiene que ser la primer linea de streamlit.
st.set_page_config(page_title="Mi chat de IA", page_icon="8️⃣", layout="centered")

# Título de la aplicación
st.image("logo.jpg", width=150)
st.title("Tp ChatBot - Técnicas del Procesamiento del habla")

# Entrada de texto
nombre = st.text_input("¿Cuál es tu nombre?")

# Botón para mostrar el saludo
if st.button("Saludar"):
    st.write(f"¡Hola, {nombre}! Bienvenido/a, Gracias por usar mi chatBot")

MODELOS = ['llama3-8b-8192', 'llama3-70b-8192', 'mixtral-8x7b-32768']
def configurar_pagina():
   
    # Agregamos un título principal a nuestra página
    st.title("Mi chat de IA")
    st.sidebar.title("Configuración de la IA") # Creamos un sidebar con un título.
    elegirModelo =  st.sidebar.selectbox('Elegí un Modelo', options=MODELOS, index=0)
    return elegirModelo

# Ciente
def crear_usuario_groq():
    claveSecreta = st.secrets["clave_api"]
    return Groq(api_key=claveSecreta)

def configurar_modelo(cliente, modelo, mensajeDeEntrada):
    return cliente.chat.completions.create(
        model=modelo,
        messages=[{"role": "user", "content": mensajeDeEntrada}],
        stream=True
    )

def inicializar_estado():
    '''
    st.session_state: Es un diccionario especial de Streamlit que permite almacenar datos persistentes entre interacciones de usuario en la aplicación.
    "mensajes" not in st.session_state: Comprueba si "mensajes" no es una clave existente en st.session_state.
    Esto es útil para mantener un estado persistente de los mensajes en la aplicación,
    permitiendo que los datos se almacenen y recuperen entre diferentes interacciones del usuario con la aplicación
    Este mecanismo es fundamental para aplicaciones interactivas donde el estado del usuario (como los mensajes en un chat) debe mantenerse a lo largo
    del uso de la aplicación.
    '''
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []



def actualizar_historial(rol, contenido, avatar):
    st.session_state.mensajes.append({"role": rol, "content": contenido, "avatar":avatar})
    
def mostrar_historial():
    for mensaje in st.session_state.mensajes:
        with st.chat_message(mensaje["role"], avatar=mensaje["avatar"]):
            st.markdown(mensaje["content"])

def area_chat():
    contenedorDelChat = st.container(height=400,border=True)
    # Abrimos el contenedor del chat y mostramos el historial.
    with contenedorDelChat:
        mostrar_historial()
    
def generar_respuesta(chat_completo):
    respuesta_completa = ""
    for frase in chat_completo:
        if frase.choices[0].delta.content:
            respuesta_completa += frase.choices[0].delta.content
            yield frase.choices[0].delta.content
    return generar_respuesta

def main():
    modelo = configurar_pagina()
    clienteUsuario = crear_usuario_groq()
    inicializar_estado()
    area_chat() # Función de esta clase
    mensaje = st.chat_input("Escribí tu mensaje:")
    # print(mensaje)

    if mensaje:
        actualizar_historial("user", mensaje, "🧑‍💻")      
       
        chat_completo = configurar_modelo(clienteUsuario, modelo, mensaje)
        
        if chat_completo:
            with st.chat_message("assistant"):
                respuesta_completa= st.write_stream(generar_respuesta(chat_completo))
                actualizar_historial("assistant", respuesta_completa,"🤖")
            
  
                st.rerun()

if __name__ == "__main__":
    main()

        
