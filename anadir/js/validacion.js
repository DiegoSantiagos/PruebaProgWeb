$(function () {
    $('.btnLimp').click(function () {
        $('.txtProd, .txtDesc, txtPrec').val('');
        $('.imgProd').attr('src', 'img/imagen.jpg');
    });
    $('.btnGuar').click(function () {
        //    Comprobar producto
        if ($('.txtProd').val() == '') {
            alert('No especificó el nombre del producto');
        } else if ($('.txtDesc').val() == "") {
            // Comprobar descripción
            alert('No especificó la descripción del producto');
        } else if ($('.txtPrec').val() == '') {
            // Comprobar precio
            alert('No especificó el precio del producto');
        } else if (!/^[0-9]+$/.test($('.txtPrec').val())) {
            alert('El precio solo puede contener números');
        } else {
            // enivar datos
            alert('Los datos se enviaron correctamente');
        }
    });
});