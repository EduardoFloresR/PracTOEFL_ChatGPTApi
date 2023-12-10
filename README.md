
# Proyecto PracTOEFL: Práctica de escritura para el TOEFL

Este proyecto es una aplicación web creada con Flask que usa la API de ChatGPT para practicar la habilidad de escritura en idioma inglés para el examen TOEFL.

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

Abre tu navegador y dirígete a `http://127.0.0.1:5000/` para ver la aplicación.

## Contribuir

Para contribuir al proyecto, asegúrate de no subir tu entorno virtual o tu clave API de OpenAI.
