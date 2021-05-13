//game.js
//****************
//DECLARATIONS & FUNCTIONS
var player = '';
var order;
var num;
var length;
var card;
var others;
var knight_victim;
var monopoly_res;
var plenty_one;
var plenty_two;
var give_qty;
var rec_qty;
var dom_to;
var give_res;
var rec_res;
var mari_give_qty;
var mari_rec_qty;
var mari_give_res;
var mari_rec_res;
var rob_victim;
var longest_rd_ck = function() {
	var long_player = 'Nobody';
	var length = 0;
	for (p in state["players"]) {
		if (state["players"][p]["roads"].length > length) {
			length = state["players"][p]["roads"].length;
			long_player = state["players"][p]["name"];
		}
	}
	var str = long_player + ' (' + length + ')';
	$('#longest_p').text(str);
}
var largest_army_ck = function() {
	var large_army = 'Nobody';
	var size = 0;
	for (p in state["players"]) {
		if (state["players"][p]["army"] > size) {
			size = state["players"][p]["army"];
			large_army = state["players"][p]["name"];
		}
	}
	var str = large_army + ' (' + size + ')';
	$('#largest_p').text(str);
}
var static_refresh = function() {
	$('#brick_amt').text(state["players"][order]["resources"]["Brick"]);
	$('#wool_amt').text(state["players"][order]["resources"]["Wool"]);
	$('#ore_amt').text(state["players"][order]["resources"]["Ore"]);
	$('#lumber_amt').text(state["players"][order]["resources"]["Lumber"]);
	$('#grain_amt').text(state["players"][order]["resources"]["Grain"]);
	$('#point_total').text(state["players"][order]["victory_points"]);
	longest_rd_ck();
	largest_army_ck();
}
var notif_pop = function() {
	$('#notif_pop').show();
	$('#notif_message').text(JSON.stringify(notif));
}
var get_turn = function() {
	var turn_order = state["turn"][1];
	var round = state["turn"][0];
	console.log("round " + round + " turn " + turn_order);
	if (order == turn_order) {
		$('#p1_text').show();
		$('#dev').show();
		$('#turn_player').text('YOUR');
		$('#roll_br').show();
		$('#dev_br').show();
		$('#to_trade').show();
		if (round < 2) {
			$('#dice').hide();
			$('#roll_br').hide();
			$('#to_trade').hide();
			$('#trade_br').hide();
			$('#p1_text').hide();
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
		}
	}
	else {
		get_state(() => {$('#turn_player').text(state["players"][turn_order]["name"] + '\'s');});
	}
	get_notifications(player,notif_pop);
}
var get_dev = function() {
	length = state["players"][order]["developments"].length
	if (length == 0) {
		$('#dev_pop').hide();
		$('#notif_pop').show();
		$('#notif_message').text("You have no development cards.");
	}
	else {
		$('#dev_pop').show();
	}
	card = state["players"][order]["developments"][num];
	$('#card_num').text((num + 1));
	if (card == "vp") {
		$(".progress_content").hide();
		$(".victory_content").show();
		$(".knight_content").hide();
		$(".monopoly_content").hide();
		$(".plenty_content").hide();
		$(".road_content").hide();
		$("#use").hide();
		$("#knight_sel").remove();
	}
	else if (card == "knight") {
		$(".progress_content").hide();
		$(".victory_content").hide();
		$(".knight_content").show();
		$(".monopoly_content").hide();
		$(".plenty_content").hide();
		$(".road_content").hide();
		$("#use").show();
		var knight_sel_text = '';
		for (p in others) {
			var opt = '<option>' + others[p] + '</option>';
			knight_sel_text = knight_sel_text.concat(opt);
		}
		var knight_sel = '<br/><select id=\'knight_sel\'>' + knight_sel_text + '</select>';
		$("#pre_knight_sel").after(knight_sel);
	}
	else if (card == "monopoly") {
		$(".progress_content").show();
		$(".victory_content").hide();
		$(".knight_content").hide();
		$(".monopoly_content").show();
		$(".plenty_content").hide();
		$(".road_content").hide();
		$("#use").show();
		$("#knight_sel").remove();
	}
	else if (card == "plenty") {
		$(".progress_content").show();
		$(".victory_content").hide();
		$(".knight_content").hide();
		$(".monopoly_content").hide();
		$(".plenty_content").show();
		$(".road_content").hide();
		$("#use").show();
		$("#knight_sel").remove();
	}
	else if (card == "road") {
		$(".progress_content").show();
		$(".victory_content").hide();
		$(".knight_content").hide();
		$(".monopoly_content").hide();
		$(".plenty_content").hide();
		$(".road_content").show();
		$("#use").show();
		$("#knight_sel").remove();
	}
}
var get_drawn = function() {
	length = state["players"][order]["dev_queue"].length;
	card = state["players"][order]["dev_queue"][length];
	if (card == 'vp') {
		var name = "Victory Point";
	}
	else if (card == 'knight') {
		var name = "Knight";
	}
	else if (card == 'monopoly') {
		var name = "Monopoly";
	}
	else if (card == 'plenty') {
		var name = "Year of Plenty";
	}
	else if (card == 'road') {
		var name = "Road Building";
	}
	$('#buy_message').text('You drew a ' + name + 'card!');
}
var use_card = function() {
	if (card == 'knight') {
		knight_victim = $('#knight_sel').val();
		play_knight();
	}
	else if (card == 'monopoly') {
		monopoly_res = $('#monopoly_sel').val();
		play_monopoly();
	}
	else if (card == 'plenty') {
		plenty_one = $('#plenty_1').val();
		plenty_two = $('#plenty_2').val();
		play_year_of_plenty();
	}
	else if (card == 'road') {
		play_build_road();
	}
	$('#dev_pop').hide();
}
var get_others = function() {
	others = [];
	for (p in state["players"]) {
		if (state["players"][p]["name"] != player) {
			others.push(state["players"][p]["name"]);
		}
	}
}
var rob = function() {
	var rob_sel_text = '';
	for (p in others) {
		var opt = '<option>' + others[p] + '</option>';
		rob_sel_text = rob_sel_text.concat(opt);
	}
	var rob_sel = '<br/><select id=\'robber_sel\'>' + rob_sel_text + '</select>';
	$("#pre_robber_sel").after(rob_sel);
	rob_victim = $('#robber_sel').val();
	robber_steal();
}
//*****************************
//DOCUMENT
$(document).ready( () => {
	var torch = new URLSearchParams(window.location.search);
	player = torch.get("pname");
	order = torch.get("porder");
	$('#nav_menu').hide();
	$('#error_pop').hide();
	$('#notif_pop').hide();
	$('#trade_pop').hide();
	$('#rob_discard_pop').hide();
	$('#rob_steal_pop').hide();
	$('#dev_pop').hide();
	$('#domestic_pop').hide();
	$('#maritime_pop').hide();
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
	$('#confirm').hide();
	get_state(get_turn);
	get_state(static_refresh);
	get_state(get_others);
	get_notifications(player,notif_pop);
	console.log(player + ', ' + order);
});

$('#nav_arrow').on('click', () => {
	$('#nav_arrow').toggleClass('rotate');
	$('#nav_menu').slideToggle(150);
});

$('#notif_accept').on('click', () => {
	$('#notif_pop').hide();
	get_state(static_refresh);
	get_notifications(player,notif_pop);
});

$('#error_accept').on('click', () => {
	$('#error_pop').hide();
	get_state(static_refresh);
	get_notifications(player,notif_pop);
});

$('#trade_accept').on('click', () => {
	$('#trade_pop').hide();
	get_state(static_refresh);
	get_notifications(player,notif_pop);
});

$('#trade_decline').on('click', () => {
	$('#trade_pop').hide();
	get_state(static_refresh);
	get_notifications(player,notif_pop);
});

$('#robber_discard').on('click', () => {
	$('#rob_discard_pop').hide();
	get_state(static_refresh);
	get_notifications(player,notif_pop);
});

$('#robber_steal').on('click', () => {
	$('#rob_steal_pop').hide();
	robber_steal();
	get_state(static_refresh);
	get_notifications(player,notif_pop);
});

$('#dev').on('click', () => {
	num = 0;
	get_state(get_dev);
	get_state(static_refresh);
	get_notifications(player,notif_pop);
});

$('.x-close').on('click', () => {
	$('#dev_pop').hide();
	$('#domestic_pop').hide();
	$('#maritime_pop').hide();
	$('#error_pop').hide();
	$('#notif_pop').hide();
	$('#domestic_sel').remove();
	get_state(static_refresh);
	get_notifications(player,notif_pop);
});

$('#prev_card').on('click', () => {
	if (num > 0) {
		num = num - 1;
	}
	else {
		num = length - 1;
	}
	get_state(get_dev);
	get_state(static_refresh);
	get_notifications(player,notif_pop);
});

$('#next_card').on('click', () => {
	if (num < length - 1) {
		num = num + 1;
	}
	else {
		num = 0;
	}
	get_state(get_dev);
	get_state(static_refresh);
	get_notifications(player,notif_pop);
});

$('#use').on('click', () => {
	get_state(use_card);
	get_state(static_refresh);
	get_notifications(player,notif_pop);
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
	get_state(static_refresh);
	get_notifications(player,notif_pop);
	window.scrollTo(0,0);
});

$('#domestic').on('click', () => {
	var domestic_sel_text = '';
	for (p in others) {
		var opt = '<option>' + others[p] + '</option>';
		domestic_sel_text = domestic_sel_text.concat(opt);
	}
	var domestic_sel = '<br/><select id=\'domestic_sel\'>' + domestic_sel_text + '</select>';
	$("#pre_domestic_sel").after(domestic_sel);
	$('#domestic_pop').show();
	get_state(static_refresh);
	get_notifications(player,notif_pop);
});

$('#maritime').on('click', () => {
	$('#maritime_pop').show();
	get_state(static_refresh);
	get_notifications(player,notif_pop);
});

$('#domestic_submit').on('click', () => {
	dom_to = $('#domestic_sel').val();
	give_qty = $('#give_qty').val();
	rec_qty = $('#rec_qty').val();
	give_res = $('#dom_res_give').val();
	rec_res = $('#dom_res_rec').val();
	propose_trade();
	get_state(static_refresh);
	get_notifications(player,notif_pop);
	$('#domestic_pop').hide();
});

$('#maritime_submit').on('click', () => {
	mari_give_qty = $('#mari_give_qty').val();
	mari_give_res = $('#mari_give_res').val();
	mari_rec_qty = $('#mari_rec_qty').val();
	mari_rec_res = $('#mari_rec_res').val();
	console.log(mari_give_qty + mari_give_res + ' for ' + mari_rec_qty + mari_rec_res);
	maritime_trade();
	get_state(static_refresh);
	get_notifications(player,notif_pop);
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
	get_state(static_refresh);
	get_notifications(player,notif_pop);
	window.scrollTo(0,0);
});

$('#buy_card').on('click', () => {
	get_state(draw_dev);
	get_state(get_drawn( () => {
		$('#buy_message').show();
	}));
	get_state(static_refresh);
	get_notifications(player,notif_pop);
});

$('#build_sett').on('click', () => {
	build_settlement();
	get_state(static_refresh);
	get_notifications(player,notif_pop);
});

$('#build_road').on('click', () => {
	build_road();
	get_state(static_refresh);
	get_notifications(player,notif_pop);
});

$('#build_city').on('click', () => {
	build_city();
	get_state(static_refresh);
	get_notifications(player,notif_pop);
});

$('#reset').on('click', () => {
	$('#confirm').show();
	$('#reset').hide();
	$('#players').hide();
	get_state(static_refresh);
	get_notifications(player,notif_pop);
});

$('#reset_confirm').on('click', () => {
	new_game( () => {
		$('#confirm').hide();
		$('#add_section').show();
		$('#reset').show();
		$('#ready').hide();
	});
	get_state(static_refresh);
	get_notifications(player,notif_pop);
});

$('#reset_deny').on('click', () => {
	$('#confirm').hide();
	$('#reset').show();
	get_state(static_refresh);
	get_notifications(player,notif_pop);
});

$('#end').on('click', () => {
	end_turn( () => {
		$('#p3_text').hide();
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
		$('#dev_br').hide();
		$('#buy_message').hide();
		window.scrollTo(0,0);
	});
	get_state(static_refresh);
	get_state(get_others);
	get_state(get_turn);
	get_state(() => {$('#turn_player').text(state["players"][turn_order]["name"] + '\'s');});
	get_notifications(player,notif_pop);
	console.log(player + ', ' + order);
});
