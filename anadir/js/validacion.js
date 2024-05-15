$(function () {
    $('.btnLimp').click(function (event) {
        event.preventDefault(); // Evitar el envío del formulario
        $('.txtProd, .txtDesc, txtPrec').val('');
        $('.imgProd').attr('src', 'img/imagen.jpg');
    });
    $('.btnGuar').click(function (event) {
        event.preventDefault(); // Evitar el envío del formulario
        //    Comprobar producto
        if ($('.txtProd').val() == '') {
            alert('No especificó el nombre del producto');
        } else if ($('.txtDesc').val() == "") {
            // Comprobar descripción
            alert('No especificó la descripción del producto');
        } else if ($('.txtPrec').val() == '') {
            // Comprobar precio
            alert('No especificó el precio del producto');
        } else if (!/^[0-9.,]+$/.test($('.txtPrec').val())) {
            alert('El precio solo puede contener números');
        } else if ($('.txtStock').val() == '') {
            // Comprobar stock
            alert('No especificó el stock del producto');
        } else if ($('.imgProd').attr('src') == '') {
            // Comprobar imagen
            alert('No especificó la imagen del producto');
        } else {
            // enivar datos
            alert('Los datos se enviaron correctamente');
        }
    });
});