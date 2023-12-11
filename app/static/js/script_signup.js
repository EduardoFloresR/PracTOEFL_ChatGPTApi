// script_signup.js

// Función para validar el formulario de registro
function validateForm() {
    // Obtener los valores de los campos del formulario
    var name = document.getElementById("name").value;
    var lastname = document.getElementById("lastname").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    // Verificar que el correo contenga "@"
    if (email.indexOf("@") === -1) {
        // Mostrar una alerta si el correo no es válido
        alert("Please enter a valid email.");
        return false;
    }

    // Verificar que la contraseña cumpla con los requisitos
    var passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;
    if (!passwordRegex.test(password)) {
        // Mostrar una alerta si la contraseña no cumple con los requisitos
        alert("The password must have at least 8 characters, 1 number, 1 uppercase letter and a special character (@$!%*#?&).");
        return false;
    }

    // Devolver true si el formulario pasa todas las validaciones
    return true;
}
