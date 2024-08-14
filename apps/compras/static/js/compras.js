// compras/static/js/compras.js
$(document).ready(function() {
    $('#nueva-compra').click(function() {
      $('#formulario-compra').show();
    });
  
    $('#guardar-compra').click(function() {
      var cliente = $('#cliente').val();
      var fecha = $('#fecha').val();
      var productos = $('#productos').val();
      $.ajax({
        type: 'POST',
        url: '/compras/nueva-compra/',
        data: {
          cliente: cliente,
          fecha: fecha,
          productos: productos
        },
        success: function(data) {
          console.log(data);
          $('#formulario-compra').hide();
        }
      });
    });
  });