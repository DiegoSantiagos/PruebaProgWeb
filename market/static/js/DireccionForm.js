document.getElementById('codigo_postal').addEventListener('input', validateCodigo_postal);

function validateCodigo_postal() {
    var codigo_postal = document.getElementById('codigo_postal');
    var regex = /^[0-9]+$/; // Only numbers

    // Remove non-numeric characters
    codigo_postal.value = codigo_postal.value.replace(/\D/g, '');
}