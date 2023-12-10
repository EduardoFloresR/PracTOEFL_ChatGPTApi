// script_signup.js

function validateForm() {
    var name = document.getElementById("name").value;
    var lastname = document.getElementById("lastname").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    // Verificar que el correo contenga "@"
    if (email.indexOf("@") === -1) {
        alert("Please enter a valid email.");
        return false;
    }

    // Verificar que la contraseña cumpla con los requisitos
    var passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;
    if (!passwordRegex.test(password)) {
        alert("The password must have at least 8 characters, 1 number, 1 uppercase letter and a special character (@$!%*#?&).");
        return false;
    }

    return true;
}
