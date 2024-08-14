// categorias/static/js/categorias.js
$(document).ready(function() {
    $('#nuevo-registro').click(function() {
      $('#formulario-registro').show();
    });
  
    $('#guardar-registro').click(function() {
      var nombre = $('#nombre').val();
      var descripcion = $('#descripcion').val();
      $.ajax({
        type: 'POST',
        url: '/categorias/nuevo-registro/',
        data: {
          nombre: nombre,
          descripcion: descripcion
        },
        success: function(data) {
          console.log(data);
          $('#formulario-registro').hide();
        }
      });
    });
  });