//debug.js
//FUNCTIONS & DECLARATIONS
var players;
var get_things = function() {
	players = state["players"];
	//what else?
	
	for (p in players) {
		//
	}
}

// DOCUMENT
$(document).ready( () => {
	$('#nav_menu').hide();
	get_state(get_things);
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
});

$('#seven_test').on('click', () => {
	test_seven_segment();
});
