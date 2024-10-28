
 Este repositorio contiene el código para un chatbot de IA implementado en Streamlit. La aplicación permite al usuario interactuar con el modelo de lenguaje natural utilizando la API de Groq, seleccionando entre varios modelos de IA, y visualizando la conversación en una interfaz amigable.
 Descripción
La aplicación "Mi chat de IA" permite al usuario:

Ingresar su nombre y recibir un saludo personalizado.
Elegir entre varios modelos de IA (llama3-8b-8192, llama3-70b-8192, mixtral-8x7b-32768) para interactuar con el chatbot.
Mantener una conversación con el chatbot, que responde en tiempo real.
Ver el historial de la conversación en la misma interfaz, con avatares para usuario y asistente.
Requisitos
Python 3.8+
Librerías necesarias en requirements.txt
Cuenta en Groq para acceder a la API y obtener una clave secreta (clave_api)
Instalación
Clonar el Repositorio

bash
git clone https://github.com/tu_usuario/tp-chatbot-streamlit.git
cd tp-chatbot-streamlit
Instalar las Dependencias

bash
pip install -r requirements.txt
Configurar la Clave API de Groq

Añadir tu clave secreta de Groq en Secrets de Streamlit. Puedes configurarla en tu archivo .streamlit/secrets.toml como sigue:
toml
[secrets]
clave_api = "TU_CLAVE_DE_API"
Ejecutar la Aplicación

bash
streamlit run app.py
Uso
Al iniciar la aplicación, se abrirá una interfaz en tu navegador. Ingresa tu nombre, elige el modelo de IA con el que deseas chatear y escribe tus mensajes para interactuar con el chatbot.
