//debug.js
$(document).ready( () => {
	$('#nav_menu').hide();
});

$('#nav_arrow').on('click', () => {
	$('#nav_arrow').toggleClass('rotate');
	$('#nav_menu').slideToggle(150);
});

$('#strip_test').on('click', () => {
	test_led_strip();
});

$('#button_test').on('click', () => {
	test_button_input();
//	$('#button_byte').text(butt_byte);
});

$('#seven_test').on('click', () => {
	test_seven_segment();
});
