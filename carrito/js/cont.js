function sumarCanti(x) {
    let cantidadInput = document.getElementById('cantidad'.padEnd(9, x));
    let cantidad = parseInt(cantidadInput.value);
    document.getElementById('cantidad'.padEnd(9, x)).value = cantidad + 1;
}

function restarCanti(x) {
    let cantidadInput = document.getElementById('cantidad'.padEnd(9, x));
    let cantidad = parseInt(cantidadInput.value);
    if (cantidad > 1) {
        document.getElementById('cantidad'.padEnd(9, x)).value = cantidad - 1;
    }
}

