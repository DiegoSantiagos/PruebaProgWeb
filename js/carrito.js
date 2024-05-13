// function carrito(x) {
//     var i;
//     x = document.getElementsByClassName("filterDiv");
//     if (c == "all") c = "";
//     for (i = 0; i < x.length; i++) {
//         w3RemoveClass(x[i], "show");
//         if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
//     }
// }

// function carrito(x) {
//     var p = document.getElementsByClassName("filterDiv");
// }

function carrito(id) {
    // Añadir el id del producto al carrito en el localStorage
    var carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    carrito.push(id);
    localStorage.setItem('carrito', JSON.stringify(carrito));
}

window.onload = function () {
    // Obtener los ids de los productos en el carrito del localStorage
    var carrito = JSON.parse(localStorage.getItem('carrito')) || [];

    // Hacer visible cada producto en el carrito
    for (var i = 0; i < carrito.length; i++) {
        var id = carrito[i];
        var elementoCarrito = document.getElementById('carrito' + id);
        if (elementoCarrito) {
            elementoCarrito.style.display = 'block';
        }
    }
}