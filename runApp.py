# Importar la función create_app desde el módulo app
from app import create_app

# Crear una aplicación Flask utilizando la función create_app
app = create_app()

# Comprobar si el script se está ejecutando directamente
if __name__ == '__main__':
    # Iniciar el servidor de desarrollo de Flask con la opción de depuración activada
    app.run(debug=True)