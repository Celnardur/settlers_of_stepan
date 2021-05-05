//mithril_func.js
var player = '';
var order;
var test;
var test_server = function() {
    m.request({
        method: "PUT",
        url: "/api/test",
        body: {test_send: 'Sent from web GUI!'},
    })
    .then(function(data) {
        test = JSON.stringify(data);
		console.log('got: ', test);
    })
}

var notif;
var get_notifications = function(player, pass) {
    m.request({
		method: "PUT",
		url: "/api/get_notifications",
		body: {name: player},
    })
	.then(function(data) {
		notif = data;
		if (notif.length != 0) {
			console.log("Got some mail!");
			console.log(notif);
			pass();
		}
		else {
			console.log("No mail.");
		}
	})
}

var test_led_strip = function() {
    m.request({
		method: "PUT",
		url: "/api/test_led_strip",
    })
}

var butt_byte;
var test_button_input = function() {
    m.request({
		method: "PUT",
		url: "/api/test_gpio",
		body: {address: 61},
    })
    .then(function(data) {
		butt_byte = JSON.stringify(data);
		console.log('got: ', butt_byte);
		$('#button_byte').text(butt_byte);
    })
}

var test_seven_segment = function() {
    m.request({
		method: "PUT",
		url: "/api/test_7seg",
		body: {address: 93},
	})
}

var new_game = function() {
	m.request({
		method: "PUT",
		url: "/api/new_game",
	})
}

var randomize_players = function() {
	m.request({
		method: "PUT",
		url: "/api/randomize_players",
	})
}

var remove_player = function() {
	m.request({
		method: "PUT",
		url: "/api/remove_player",
		body: {name: player},
	})
}

var player_ready = function() {
	m.request({
		method: "PUT",
		url: "/api/player_ready",
		body: {name: player},
	})
}

var add_player = function() {
	m.request({
		method: "PUT",
		url: "/api/add_player",
		body: {name: player, color: color_RGB, order: order},
	})
}

var change_player_color = function() {
	m.request({
		method: "PUT",
		url: "/api/change_player_color",
		body: {name: player, color: color_RGB},
	})
}

var build_settlement = function() {
	m.request({
		method: "PUT",
		url: "/api/build_settlement",
		body: {name: player},
	})
}

var build_road = function() {
	m.request({
		method: "PUT",
		url: "/api/build_road",
		body: {name: player},
	})
}

var build_city = function() {
	m.request({
		method: "PUT",
		url: "/api/build_city",
		body: {name: player},
	})
}

var draw_dev = function() {
	m.request({
		method: "PUT",
		url: "/api/draw_dev",
	})
}

var end_turn = function() {
	m.request({
		method: "PUT",
		url: "/api/end_turn",
		body: {name: player},
	})
}

// /api/move_robber--not activated by GUI!

var pay_taxes = function() {
	m.request({
		method: "PUT",
		url: "/api/pay_taxes",
	})
}

var maritime_trade = function() {
	m.request({
		method: "PUT",
		url: "/api/maritime_trade",
		body: {name: player, give: {mari_give_res: mari_give_qty}, get: {mari_rec_res: mari_rec_qty}}
	})
}

var state;
var get_state = function(pass) {
	m.request({
		method: "PUT",
		url: "/api/get_state",
	})
	.then(function(data) {
		state = data;
		pass();
    })
}

var play_knight = function() {
	m.request({
		method: "PUT",
		url: "/api/play_knight",
		body: {victim: knight_victim, name: player},
	})
}

var play_monopoly = function() {
	m.request({
		method: "PUT",
		url: "/api/play_monopoly",
		body: {resource: monopoly_res, name: player},
	})
}

var play_year_of_plenty = function() {
	m.request({
		method: "PUT",
		url: "/api/play_year_of_plenty",
		body: {name: player, one: plenty_one, two: plenty_two},
	})
}

var play_build_road = function() {
	m.request({
		method: "PUT",
		url: "/api/play_build_road",
		body: {name: player},
	})
}

var propose_trade = function() {
	m.request({
		method: "PUT",
		url: "/api/propose_trade",
		body: {name: player, trade: {proposer: {name: player, give: {give_res: give_qty}}, approver: {name: dom_to, give: {rec_res: rec_qty}}}},
	})
}
