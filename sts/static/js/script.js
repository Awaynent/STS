$(document).ready(function() {
  $('#qr-form').submit(function(event) {
    event.preventDefault();
    var scannedName = $('#qr-input').val();
    checkRegistration(scannedName);
  });
});

function checkRegistration(name) {
  $.ajax({
    url: 'check_registration',
    type: 'POST',
    data: { name: name },
    success: function(response) {
      $('#result').text(response);
    },
    error: function(xhr, status, error) {
      console.error('Error:', status, error);
      $('#result').text('An error occurred while checking the registration.');
    }
  });
}
