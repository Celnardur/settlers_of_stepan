//index.js
$(document).ready( () => {
	$('#nav_menu').hide();
	$('#reset').hide();
	$('#players').hide();
	$('#confirm').hide();
});

$('#nav_arrow').on('click', () => {
	$('#nav_arrow').toggleClass('rotate');
	$('#nav_menu').slideToggle(150);
});

$('#add').on('click', () => {
	$('#add_section').hide();
	$('#reset').show();
	$('#players').show();
});

$('#x-marker').on('click', () => {
	$('#add_section').show();
	$('#reset').hide();
	$('#players').hide();
});

$('#reset').on('click', () => {
	$('#confirm').show();
	$('#reset').hide();
	$('#players').hide();
});

$('#reset_confirm').on('click', () => {
	$(location).attr('href','./game.html');
});

$('#reset_deny').on('click', () => {
	$('#confirm').hide();
	$('#reset').show();
	$('#players').show();
});

$('#server_test').on('click', () => { //TEMPORARY	
	test_server();
	$('#server_test').text(test);
});