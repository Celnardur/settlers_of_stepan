//proto_debug.js
$(document).ready( () => {
	$('#nav_menu').hide();
});

$('#nav_arrow').on('click', () => {
	$('#nav_arrow').toggleClass('rotate');
	$('#nav_menu').slideToggle(150);
});