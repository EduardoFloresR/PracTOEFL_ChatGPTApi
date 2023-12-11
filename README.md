
# Proyecto PracTOEFL: Práctica de escritura para el TOEFL

Este proyecto es una aplicación web creada con Flask que usa la API de ChatGPT para practicar la escritura de ensayos cortos en idioma inglés con el objetivos de prepararse para el examen TOEFL.
El chatbot está configurado para evaluar 4 criterios principales: 1. Contenido y relevancia de la información, 2. Organización y estructura del ensayo, 3. Uso de lenguaje y vocabulario, 4. Gramática.
Usando SQLAlchemy se crea una base de datos local ("datos.db") que contiene diversos registros de calificaciones obtenidas al probar la herramienta.
Con el algoritmo de agrupamiento k-medias se obtienen los clusters de los vectores almacenados en dicha base de datos, generando 3 tipos de grupos de acuerdo a las calificaciones obtenidas; además, se usan dichos agrupamientos para asigarle al usuario un grupo de acuerdo a su calificación promedio en cada sección, de manera que se le brinda un consejo personalizado para mejorar su escritura.
Los colores y la estrcutura de la página están basados en la página oficial del exmane [TOEFL IBT](https://toefltest.mx/).

## Configuración

Para comenzar, sigue estos pasos:

### 1. Clonar el Repositorio

Clona este repositorio a tu máquina local usando:

```bash
git clone https://github.com/EduardoFloresR/PracTOEFL_ChatGPTApi.git
```

### 2. Crear un Entorno Virtual

Es recomendable usar un entorno virtual para instalar las dependencias. Puedes crear uno usando:

```bash
python -m venv .venv
```

Activar el entorno virtual:

En Windows:
```bash
.venv\Scripts\activate
```

En MacOS/Linux:
```bash
source .venv/bin/activate
```

### 3. Instalar Dependencias

Instala las dependencias necesarias con:

```bash
pip install -r requirements.txt
```

### 4. Configurar API de ChatGPT

Obtén una clave API de ChatGPT (token) registrándote y pagando en [openai](https://platform.openai.com/account/billing/overview). Asegúrate de no subir tu clave API a tu repositorio.

### 5. Ejecutar la Aplicación

Para ejecutar la aplicación, usa:

```bash
python runApp.py
```

## Uso
### 1. Apertura de la aplicación web

Abre tu navegador y dirígete a la dirección IP `http://127.0.0.1:5000/` para ver la aplicación.

### 2. Creación de cuenta

Si NO deseas crear tu propia cuenta o ya tienes una cuenta registrada en la base de datos "datos.db", pasa al siguiente punto.
Presiona el botón "Log in" en el lado derecho de la ventana. Llena los datos del formulario con tus datos y haz clic en el botón "Send".
Nota: la contraseña ingresada debe contener al menos una letra mayúscula, un número y algún caracter especial de los siguientes @$!%*#?&.

### 3. Inicio de sesión

En caso de que no hayas registrado tu propia cuenta, puedes ingresar con las credenciales siguientes:
    email: practoefl@gmail.com
    password: 12341234Q!

En caso de que tengas tu propias credenciales, ingrésalas en el formulario.
Una vez que hayas llenado los datos, haz clic en el botón "Verify".

### 4. Página de inicio

Cuando hayas iniciado sesión, serás redirigido a la pestaña "Home" y aparecerá una barra de navegación en la parte superior de la ventana.
En esta página se muestra un pequeño resumen de cómo usar la aplicaicón web. El botón "Visit TOEFL Test" a la derecha, carga la página oficial del TOEFL IBT.

### 5. Prueba de escritura

Para comenzaaz clic en el botón "Writing" de la barra de navegación.
Este botón cargará la página de escritura, que consiste en una caja de texto donde podrás ingresar tu ensayo corto (entre 50 y 600 palabras).
En la parte superior de la caja de texto se mostrará una sugerencia de tema para el ensayo, en caso de que desees uno distinto, haz clic en el botón "Change topic" de la derecha.
Cuando hayas terminado, haz clic en el botón "Check" para que se envíe el texto y comience su revisión.
Este proceso de revisión puede tardar algo de tiempo de acuerdo a la longitud del ensayo, la conexión a internet y la disponibilidad de la API de ChatGPT, por lo que se recomienda paciencia.

### 6. Resultados de la prueba

La ventana desplegada mostrará otra caja de texto con una explicación de tus resultados, la cual se desglozará en las 4 secciones de evaluación.
En la sección derecha de la ventana podrás observar un resumen de la calificación obtenida en cada sección.
También estará disponible el botón "Try again" para volver a cargar el formulario de escritura.
Debajo del formulario de resultados, se encuentra el botón "See your ranking" que permite visualizar la información del usuario.

### 7. Estadísticas del usuario

En la pestaña "My profile", que se puede acceder desde la barra de navegación o con el botón "See your ranking" después de enviar un ensayo, se pueden observar las estadísiticas del usuario y compararlas con el resto de registros que se tienen en la base de datos. Esta comparación se lleva a cabo al situar al promedio del usuario en uno de los 3 grupos obtenidos al aplicar el algoritmo K-medias sobre todos los registros. Al asignar las calificaciones del usuario a un cluster, es posible obtener algunas características de sus respuestas y brindarle consejos personalizados.

### 8. Acerca del proyecto

En la pestaña "About us" se muestra información básica sobre el funcionamiento y construcción de la aplicación web, como las tecnologías y librerías que se emplearón.
También se despliega un código QR que permite acceder al repositorio de Github donde se puede descargar el código completo de la implementación.

## Contribuir

Para contribuir al proyecto, asegúrate de no subir tu entorno virtual o tu clave API de OpenAI.
