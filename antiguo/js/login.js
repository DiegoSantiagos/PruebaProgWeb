$(function () {
    $('.btnLog').click(function () {
        if ($('.txtEmail').val() == '') {
            alert('No especificó el correo');
        } else if (!/^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/.test($('.txtEmail').val())) {
            alert('El formato del correo no es válido');
        } else if ($('.txtClave').val() == "") {
            alert('No especificó la clave');
        } else if (!/^[a-zA-Z0-9]+$/.test($('.txtClave').val())) {
            alert('La clave solo puede contener letras y números');
        } else {
            alert('Los datos se enviaron correctamente');
        }
    });
});
