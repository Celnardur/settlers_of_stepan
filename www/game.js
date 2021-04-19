//game.js
$(document).ready( () => {
	$('#nav_menu').hide();
	$('#error_pop').hide();
	$('#trade_pop').hide();
	$('#rob_discard_pop').hide();
	$('#rob_steal_pop').hide();
	$('#dev_pop').hide();
	$('#domestic_pop').hide();
	$('#maritime_pop').hide();
	$('#roll').hide();
	$('#dev').hide();
	$('#build_road').hide();
	$('#build_city').hide();
	$('#build_sett').hide();
	$('#buy_card').hide();
	$('#domestic').hide();
	$('#maritime').hide();
	$('#end').hide();
	$('#p1_text').hide();
	$('#p2_text').hide();
	$('#p3_text').hide();
	$('#dice').hide();
	$('#to_trade').hide();
	$('#to_build').hide();
	$('#buy_message').hide();
	$('#roll_br').hide();
	$('#dev_br').hide();
	$('#road_br').hide();
	$('#city_br').hide();
	$('#sett_br').hide();
	$('#buy_br').hide();
	$('#domestic_br').hide();
	$('#maritime_br').hide();
	$('#end_br').hide();
	$('#trade_br').hide();
});

$('#nav_arrow').on('click', () => {
	$('#nav_arrow').toggleClass('rotate');
	$('#nav_menu').slideToggle(150);
});

$('#turn_test').on('click', () => { //TEMPORARY
	$('#p1_text').show();
	$('#static_info').hide();
	$('#roll').show();
	$('#dev').show();
	$('#turn_test').text('YOUR');
	$('#roll_br').show();
	$('#dev_br').show();
});

// $('#error_test').on('click', () => {
	// $('#error_pop').show();
// });

$('#error_accept').on('click', () => {
	$('#error_pop').hide();
});

// $('#trade_test').on('click', () => {
	// $('#trade_pop').show();
// });

$('#trade_accept').on('click', () => {
	$('#trade_pop').hide();
});

$('#trade_decline').on('click', () => {
	$('#trade_pop').hide();
});

// $('#robber_test').on('click', () => {
	// $('#rob_discard_pop').show();
// });

$('#robber_discard').on('click', () => {
	$('#rob_discard_pop').hide();
});

$('#roll').on('click', () => {
	$('#dice').show();
	$('#roll').hide();
	$('#to_trade').show();
	$('#trade_br').hide();
});

// $('#steal_test').on('click', () => {
	// $('#rob_steal_pop').show();
// });

$('#robber_steal').on('click', () => {
	$('#rob_steal_pop').hide();
});

$('#dev').on('click', () => {
	$('#dev_pop').show();
	$('.knight_content').show(); //TEMPORARY
	$('.progress_content').hide();
	$('.victory_content').hide();
});

$('#x-close').on('click', () => {
	$('#dev_pop').hide();
});

$('#prev_card').on('click', () => {
	$('.knight_content').hide();
	$('.progress_content').hide();
	$('.victory_content').show();
});

$('#next_card').on('click', () => { //TEMPORARY
	$('.knight_content').hide();
	$('.progress_content').show();
	$('.victory_content').hide();
});

$('#use').on('click', () => { //TEMPORARY
	$('.knight_content').show();
	$('.progress_content').hide();
	$('.victory_content').hide();
});

$('#to_trade').on('click', () => {
	$('#dice').hide();
	$('#roll_br').hide();
	$('#to_trade').hide();
	$('#trade_br').hide();
	$('#static_info').show();
	$('#domestic').show();
	$('#domestic_br').show();
	$('#maritime').show();
	$('#maritime_br').show();
	$('#to_build').show();
	$('#p1_text').hide();
	$('#p2_text').show();
	window.scrollTo(0,0);
});

$('#domestic').on('click', () => {
	$('#domestic_pop').show();
});

$('#maritime').on('click', () => {
	$('#maritime_pop').show();
});

$('#domestic_submit').on('click', () => {
	$('#domestic_pop').hide();
});

$('#maritime_submit').on('click', () => {
	$('#maritime_pop').hide();
});

$('#to_build').on('click', () => {
	$('#domestic').hide();
	$('#domestic_br').hide();
	$('#maritime').hide();
	$('#maritime_br').hide();
	$('#to_build').hide();
	$('#p2_text').hide();
	$('#p3_text').show();
	$('#end').show();
	$('#end_br').show();
	$('#build_road').show();
	$('#road_br').show();
	$('#build_city').show();
	$('#city_br').show();
	$('#build_sett').show();
	$('#sett_br').show();
	$('#buy_card').show();
	$('#buy_br').show();
	window.scrollTo(0,0);
});

$('#buy_card').on('click', () => {
	$('#buy_message').show();
});

$('#build_sett').on('click', () => {
	build_settlement();
});

$('#end').on('click', () => {
	$('#p3_text').hide();
	$('#turn_test').text('Sarah\'s');
	$('#build_road').hide();
	$('#road_br').hide();
	$('#build_city').hide();
	$('#city_br').hide();
	$('#build_sett').hide();
	$('#sett_br').hide();
	$('#buy_card').hide();
	$('#buy_br').hide();
	$('#end').hide();
	$('#end_br').hide();
	$('#dev').hide();
	$('#dev_br').hide();
	$('#buy_message').hide();
	window.scrollTo(0,0);
});