// clientes/static/js/clientes.js
$(document).ready(function() {
    $('#nuevo-registro').click(function() {
      $('#formulario-registro').show();
    });
  
    $('#guardar-registro').click(function() {
      var nombre = $('#nombre').val();
      var apellido = $('#apellido').val();
      $.ajax({
        type: 'POST',
        url: '/clientes/nuevo-registro/',
        data: {
          nombre: nombre,
          apellido: apellido
        },
        success: function(data) {
          console.log(data);
          $('#formulario-registro').hide();
        }
      });
    });
  });