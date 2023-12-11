// script_writing.js

// Escucha el evento de carga del contenido DOM y redirige al hacer clic en el botón 'changeTopicBtn'
document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('changeTopicBtn').addEventListener('click', function(){
        window.location.href = '/writing';
    });
});
