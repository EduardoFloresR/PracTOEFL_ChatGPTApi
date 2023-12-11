// script.js

// Escucha el evento de carga del contenido DOM y redirige al hacer clic en el botón 'writingBtn'
document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('writingBtn').addEventListener('click', function(){
        window.location.href = '/writing';
    });
});

// Escucha el evento de carga del contenido DOM y redirige al hacer clic en el botón 'loginBtn'
document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('loginBtn').addEventListener('click', function(){
        window.location.href = '/login_form';
    });
});

// Escucha el evento de carga del contenido DOM y redirige al hacer clic en el botón 'signupBtn'
document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('signupBtn').addEventListener('click', function(){
        window.location.href = '/signup_form';
    });
});

// Escucha el evento de carga del contenido DOM y redirige al hacer clic en el botón 'resultsBtn'
document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('resultsBtn').addEventListener('click', function(){
        window.location.href = '/see_results';
    });
});
