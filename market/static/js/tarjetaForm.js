function validate() {
    var regex = /^[0-9]{15,16}|(([0-9]{4}\s){3}[0-9]{3,4})$/; // 16 digits or groups of 4 separated by spaces.
    var numero = document.getElementById('numero');
    var resultadoValidacion = document.getElementById('resultadoValidacion');

    // Remove non-numeric characters
    numero.value = numero.value.replace(/\D/g, '');

    if (numero.value.length > 0) {
        resultadoValidacion.innerHTML = regex.test(numero.value) ? 'Valido' : 'Invalido';
    } else {
        resultadoValidacion.innerHTML = 'Solo ingresar Numeros';
    }
}

// Add the input event to the text field
document.getElementById('numero').addEventListener('input', validate);


// Add the input event to the cvv field
document.getElementById('cvv').addEventListener('input', validateCvv);

function validateCvv() {
    var cvv = document.getElementById('cvv');
    var regex = /^[0-9]+$/; // Only numbers

    // Remove non-numeric characters
    cvv.value = cvv.value.replace(/\D/g, '');
}