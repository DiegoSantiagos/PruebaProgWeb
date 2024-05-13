$(function () {
    $('.btnLimpiar').click(function () {
        $('.txtEma, .txtCla, txtRun').val('');
    });
    $('.btnGuar').click(function () {
        //    Comprobar correo
        if ($('.txtEma').val() == '') {
            alert('No especificó el correo');
        } else if (!/^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/.test($('.txtEma').val())) {
            alert('El formato del correo no es válido');
            // Comprobar contrasena
        } else if ($('.txtCla').val() == "") {
            alert('No especificó la clave');
        } else if (!/^[a-zA-Z0-9]+$/.test($('.txtCla').val())) {
            alert('La clave solo puede contener letras y números');
            // comprobar Rut
        } else if ($('.txtRun').val() == '') {
            alert('No especificó el Run');
        } else if (!/^[0-9]+-[0-9kK]{1}$/.test($('.txtRun').val())) {
            alert('El formato del Run no es válido');
        } else if ($('.txtNom').val() == '') {
            alert('No especificó el nombre');
        } else if ($('.txtApe').val() == '') {
            alert('No especificó el apellido');
        } else if ($('.txtFec').val() == '') {
            alert('No especificó la fecha de nacimiento');
        } else if ($('.txtFon').val() == '') {
            alert('No especificó el teléfono');
        } else if (!/^[0-9]+$/.test($('.txtFon').val())) {
            alert('El teléfono solo puede contener números');
        } else {
            // enivar datos
            alert('Los datos se enviaron correctamente');
        }
    });
});