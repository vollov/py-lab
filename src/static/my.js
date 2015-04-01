$(document).ready(function() {
	// $('#message').load("message");
	// $('#message').text("new dialog title");
	$('a#calculate').bind('click', function() {
		$.getJSON($SCRIPT_ROOT + '/_add', {
			a : $('input[name="a"]').val(),
			b : $('input[name="b"]').val()
		}, function(data) {
			$("#result").text(data.result);
		});
		return false;
	});
});