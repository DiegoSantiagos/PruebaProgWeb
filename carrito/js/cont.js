
function sumarCantidad() {
    let cantidadInput = document.getElementById('cantidad2');
    let cantidad = parseInt(cantidadInput.value);
    cantidadInput.value = cantidad + 1;
}

function restarCantidad() {
    let cantidadInput = document.getElementById('cantidad2');
    let cantidad = parseInt(cantidadInput.value);
    if (cantidad > 1) {
        cantidadInput.value = cantidad - 1;
    }
}


function sumarCanti(x) {
    let cantidadInput = document.getElementById(x);
    let cantidad = parseInt(cantidadInput.value);
    cantidadInput.value = cantidad + 1;
}

function restarCanti(x) {
    let cantidadInput = document.getElementById(x);
    let cantidad = parseInt(cantidadInput.value);
    if (cantidad > 1) {
        cantidadInput.value = cantidad - 1;
    }
}

