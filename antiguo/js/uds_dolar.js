async function obtenerTasaDeCambio() {
    const respuesta = await fetch('https://api.exchangerate-api.com/v4/latest/CLP');
    const datos = await respuesta.json();
    return datos.rates.USD;
}
let isPrecioEnUSD = false; // Declarar isPrecioEnUSD como una variable global

async function cambiar() {
    const boton_clp_usd = document.getElementById('boton-clp-usd');
    if (boton_clp_usd.innerHTML == 'CLP a USD') {
        boton_clp_usd.innerHTML = 'USD a CLP';
        isPrecioEnUSD = true;
    } else {
        boton_clp_usd.innerHTML = 'CLP a USD';
        isPrecioEnUSD = false;
    }
    await actualizarPrecio();
}

async function actualizarPrecio() {
    const elementosPrecio = document.querySelectorAll('#precio'); // Cambiado de '.precio' a '#precio'
    const tasaDeCambio = await obtenerTasaDeCambio();

    elementosPrecio.forEach((elementoPrecio) => {
        let precioActual = Number(elementoPrecio.textContent);
        if (isPrecioEnUSD) {
            precioActual = precioActual * tasaDeCambio;
        } else {
            precioActual = precioActual / tasaDeCambio;
        }
        elementoPrecio.textContent = precioActual.toFixed(2);
    });
}