async function obtenerTasaDeCambio() {
    const respuesta = await fetch('https://api.exchangerate-api.com/v4/latest/CLP');
    const datos = await respuesta.json();
    return datos.rates.USD;
}

async function actualizarPrecio() {
    const elementosPrecio = document.querySelectorAll('#precio');
    const tasaDeCambio = await obtenerTasaDeCambio();

    elementosPrecio.forEach(async (elementoPrecio) => {
        const precioEnCLP = Number(elementoPrecio.textContent);
        const precioEnUSD = precioEnCLP * tasaDeCambio;
        elementoPrecio.textContent = precioEnUSD.toFixed(2);
    });
}
