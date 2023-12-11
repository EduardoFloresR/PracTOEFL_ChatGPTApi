// script_seeResults.js

// Espera a que el DOM esté completamente cargado antes de ejecutar el código
document.addEventListener('DOMContentLoaded', function () {
    // Agrega un evento de clic al elemento con el id 'resultsBtn'
    document.getElementById('resultsBtn').addEventListener('click', function () {
        // Redirecciona a la ruta '/see_results' al hacer clic en el botón 'resultsBtn'
        window.location.href = '/see_results';
    });
});

// Espera a que el DOM esté completamente cargado antes de ejecutar el código
document.addEventListener('DOMContentLoaded', function () {
    // Agrega un evento de clic al elemento con el id 'rankingBtn'
    document.getElementById('rankingBtn').addEventListener('click', function () {
        // Redirecciona a la ruta '/my_profile' al hacer clic en el botón 'rankingBtn'
        window.location.href = '/my_profile';
    });
});
