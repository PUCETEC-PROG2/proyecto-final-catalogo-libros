// productos/static/js/productos.js
$(document).ready(function() {
    $('#nuevo-registro').click(function() {
      $('#formulario-registro').show();
    });
  
    $('#guardar-registro').click(function() {
      var nombre = $('#nombre').val();
      var precio = $('#precio').val();
      $.ajax({
        type: 'POST',
        url: '/productos/nuevo-registro/',
        data: {
          nombre: nombre,
          precio: precio
        },
        success: function(data) {
          console.log(data);
          $('#formulario-registro').hide();
        }
      });
    });
  });