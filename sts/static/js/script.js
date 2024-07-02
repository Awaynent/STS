$(document).ready(function() {
  $('#qr-form').submit(function(event) {
    event.preventDefault();
    let name = $('#qr-input').val();
    $.post('/check_registration', { name: name }, function(data) {
      $('#result').text(data);
    });
  });
});
