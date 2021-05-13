//mithril_func.js
var player = '';
var order;
var test;
var err = null;
var e = null;
var rob;
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
	.catch(function(e) {
		$('#error_pop').show();
		$('#error_message').text(e.message);
		err = e;
		e = null;
	})
	.then(function(data) {
		if (err == null) {
			notif = data;
			if (notif.length != 0) {
				console.log("Got some mail!");
				console.log(notif);
				pass();
				for (n in notif) {
					if (notif[n]["move_robber"]) {
						if (notif[n]["move_robber"] == true) {
							rob();
							$('#rob_steal_pop').show();
						}
					}
				}
			}
			else {
				console.log("No mail.");
			}
		}
		err = null;
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

var new_game = function(pass) {
	m.request({
		method: "PUT",
		url: "/api/new_game",
	})
	.catch(function(e) {
		$('#error_pop').show();
		$('#error_message').text(e.message);
		err = e;
		e = null;
	})
	.then( () => {
		if (err == null) {
			pass();
		}
		err = null;
	})
}

var randomize_players = function(pass) {
	m.request({
		method: "PUT",
		url: "/api/randomize_players",
	})
	.catch(function(e) {
		$('#error_pop').show();
		$('#error_message').text(e.message);
		err = e;
		e = null;
	})
	.then( () => {
		if (err == null) {
			pass();
		}
		err = null;
	})
}

var remove_player = function(pass) {
	m.request({
		method: "PUT",
		url: "/api/remove_player",
		body: {name: player},
	})
	.catch(function(e) {
		$('#error_pop').show();
		$('#error_message').text(e.message);
		err = e;
		e = null;
	})
	.then( () => {
		if (err == null) {
			pass();
		}
		err = null;
	})
}

var player_ready = function(pass) {
	m.request({
		method: "PUT",
		url: "/api/player_ready",
		body: {name: player},
	})
	.catch(function(e) {
		$('#error_pop').show();
		$('#error_message').text(e.message);
		err = e;
		e = null;
	})
	.then( () => {
		if (err == null) {
			pass();
		}
		err = null;
	})
}

var add_player = function(pass) {
	m.request({
		method: "PUT",
		url: "/api/add_player",
		body: {name: player, color: color_RGB, order: order},
	})
	.catch(function(e) {
		$('#error_pop').show();
		$('#error_message').text(e.message);
		err = e;
		e = null;
		console.log('after reset, e = ' + e);
	})
	.then( () => {
		if (err == null) {
			pass();
		}
		err = null;
		console.log('after then, err = ' + err);
	})
}

var change_player_color = function(pass) {
	m.request({
		method: "PUT",
		url: "/api/change_player_color",
		body: {name: player, color: color_RGB},
	})
	.catch(function(e) {
		$('#error_pop').show();
		$('#error_message').text(e.message);
		err = e;
		e = null;
	})
	.then( () => {
		if (err == null) {
			pass();
		}
		err = null;
	})
}

var build_settlement = function(pass) {
	m.request({
		method: "PUT",
		url: "/api/build_settlement",
		body: {name: player},
	})
	.catch(function(e) {
		$('#error_pop').show();
		$('#error_message').text(e.message);
		err = e;
		e = null;
	})
	.then( () => {
		if (err == null) {
			pass();
		}
		err = null;
	})
}

var build_road = function(pass) {
	m.request({
		method: "PUT",
		url: "/api/build_road",
		body: {name: player},
	})
	.catch(function(e) {
		$('#error_pop').show();
		$('#error_message').text(e.message);
		err = e;
		e = null;
	})
	.then( () => {
		if (err == null) {
			pass();
		}
		err = null;
	})
}

var build_city = function(pass) {
	m.request({
		method: "PUT",
		url: "/api/build_city",
		body: {name: player},
	})
	.catch(function(e) {
		$('#error_pop').show();
		$('#error_message').text(e.message);
		err = e;
		e = null;
	})
	.then( () => {
		if (err == null) {
			pass();
		}
		err = null;
	})
}

var draw_dev = function(pass) {
	m.request({
		method: "PUT",
		url: "/api/draw_dev",
	})
	.catch(function(e) {
		$('#error_pop').show();
		$('#error_message').text(e.message);
		err = e;
		e = null;
	})
	.then( () => {
		if (err == null) {
			pass();
		}
		err = null;
	})
}

var end_turn = function(pass) {
	m.request({
		method: "PUT",
		url: "/api/end_turn",
		body: {name: player},
	})
	.catch(function(e) {
		$('#error_pop').show();
		$('#error_message').text(e.message);
		err = e;
		e = null;
	})
	.then( () => {
		if (err == null) {
			pass();
		}
		err = null;
	})
}

var pay_taxes = function(pass) {
	m.request({
		method: "PUT",
		url: "/api/pay_taxes",
	})
	.catch(function(e) {
		$('#error_pop').show();
		$('#error_message').text(e.message);
		err = e;
		e = null;
	})
	.then( () => {
		if (err == null) {
			pass();
		}
		err = null;
	})
}

var maritime_trade = function(pass) {
	m.request({
		method: "PUT",
		url: "/api/maritime_trade",
		body: {name: player, give: {mari_give_res: mari_give_qty}, get: {mari_rec_res: mari_rec_qty}}
	})
	.catch(function(e) {
		$('#error_pop').show();
		$('#error_message').text(e.message);
		err = e;
		e = null;
	})
	.then( () => {
		if (err == null) {
			pass();
		}
		err = null;
	})
}

var state;
var get_state = function(pass) {
	m.request({
		method: "PUT",
		url: "/api/get_state",
	})
	.catch(function(e) {
		$('#error_pop').show();
		$('#error_message').text(e.message);
		err = e;
		e = null;
	})
	.then(function(data) {
		if (err == null) {
			state = data;
			pass();
		}
		err = null;
    })
}

var play_knight = function(pass) {
	m.request({
		method: "PUT",
		url: "/api/play_knight",
		body: {victim: knight_victim, name: player},
	})
	.catch(function(e) {
		$('#error_pop').show();
		$('#error_message').text(e.message);
		err = e;
		e = null;
	})
	.then( () => {
		if (err == null) {
			pass();
		}
		err = null;
	})
}

var play_monopoly = function(pass) {
	m.request({
		method: "PUT",
		url: "/api/play_monopoly",
		body: {resource: monopoly_res, name: player},
	})
	.catch(function(e) {
		$('#error_pop').show();
		$('#error_message').text(e.message);
		err = e;
		e = null;
	})
	.then( () => {
		if (err == null) {
			pass();
		}
		err = null;
	})
}

var play_year_of_plenty = function(pass) {
	m.request({
		method: "PUT",
		url: "/api/play_year_of_plenty",
		body: {name: player, one: plenty_one, two: plenty_two},
	})
	.catch(function(e) {
		$('#error_pop').show();
		$('#error_message').text(e.message);
		err = e;
		e = null;
	})
	.then( () => {
		if (err == null) {
			pass();
		}
		err = null;
	})
}

var play_build_road = function(pass) {
	m.request({
		method: "PUT",
		url: "/api/play_build_road",
		body: {name: player},
	})
	.catch(function(e) {
		$('#error_pop').show();
		$('#error_message').text(e.message);
		err = e;
		e = null;
	})
	.then( () => {
		if (err == null) {
			pass();
		}
		err = null;
	})
}

var propose_trade = function(pass) {
	m.request({
		method: "PUT",
		url: "/api/propose_trade",
		body: {name: player, trade: {proposer: {name: player, give: {give_res: give_qty}}, approver: {name: dom_to, give: {rec_res: rec_qty}}}},
	})
	.catch(function(e) {
		$('#error_pop').show();
		$('#error_message').text(e.message);
		err = e;
		e = null;
	})
	.then( () => {
		if (err == null) {
			pass();
		}
		err = null;
	})
}

var robber_steal = function(pass) {
	m.request({
		method: "PUT",
		url: "/api/move_robber",
		body: {mover: player, victim: rob_victim},
	})
	.catch(function(e) {
		$('#error_pop').show();
		$('#error_message').text(e.message);
		err = e;
		e = null;
	})
	.then( () => {
		if (err == null) {
			pass();
		}
		err = null;
	})
}