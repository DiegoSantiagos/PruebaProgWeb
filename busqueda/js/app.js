function convertirPesosADolares() {
    const elementos = document.getElementsByClassName('precio');

    for (let i = 0; i < elementos.length; i++) {
        const labelElement = elementos[i];
        const texto = labelElement.textContent;

        // Extraer el precio de la cadena de texto utilizando una expresión regular
        const precio = texto.match(/\d+(\.\d+)?/)[0];

        const pesos = parseFloat(precio);
        const dollars = pesos / 20;

        // Reemplazar solo el precio en el texto utilizando la función replace y la expresión regular
        const nuevoTexto = texto.replace(/\d+(\.\d+)?/, dollars.toFixed(2));

        // Reemplazar solo la parte del precio en el texto original
        const textoModificado = texto.replace(precio, nuevoTexto);

        labelElement.textContent = textoModificado;
    }
}
