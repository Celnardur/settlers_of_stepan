//mithril_func.js
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
		body: {name: $(this).closest('pname').text},
	})
}

var add_player = function() {
	m.request({
		method: "PUT",
		url: "/api/add_player",
		body: {name: $('#name').text},
	})
}

var build_settlement = function() {
	m.request({
		method: "PUT",
		url: "/api/build_settlement",
	})
}