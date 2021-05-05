//index.js
//DON'T SHOW/HIDE/DO THINGS IF THERE'S AN ERROR, OR FORCE GOING BACK IN THE ERROR POP-UP
var color_RGB;
var notif_pop = function() {
	$('#notif_pop').show();
	$('#notif_message').text(JSON.stringify(notif));
}
//*********************
$(document).ready( () => {
	$('#error_pop').hide();
	$('#notif_pop').hide();
	$('#nav_menu').hide();
	$('#players').hide();
	$('#confirm').hide();
	$('#ready').hide();
	$('#color_panel').hide();
	//$('#reset').hide(); TURN THIS BACK ON
});

$('#notif_accept').on('click', () => {
	$('#notif_pop').hide();
});

$('#nav_arrow').on('click', () => {
	$('#nav_arrow').toggleClass('rotate');
	$('#nav_menu').slideToggle(150);
});

$('#add').on('click', () => {
	var rgbString = '';
	player = $('#name').val();
	if ($('#color_sel').val() == "Orange") {
		color_RGB = [255,85,0];
	}
	else if ($('#color_sel').val() == "Blue") {
		color_RGB = [0,0,255];
	}
	else if ($('#color_sel').val() == "White") {
		color_RGB = [255,255,255];
	}
	else if ($('#color_sel').val() == "Red") {
		color_RGB = [255,0,0];
	}
	order = ($('#order').val() - 1);
	add_player();
	$('#add_section').hide();
	$('#reset').show();
	$('#players').show();
	$('#ready').show();
	$('#list_name').text(player);
	rgbString = 'rgb(' + color_RGB[0] + ',' + color_RGB[1] + ',' + color_RGB[2] + ')';
	$('#color_block').css('color',rgbString);
	get_notifications(player,notif_pop);
});

$('#x-marker').on('click', () => {
	remove_player();
	$('#add_section').show();
	$('#players').hide();
	$('#ready').hide();
});

$('#color_change').on('click', () => {
	$('#players').hide();
	$('#color_panel').show();
	$('#ready').hide();
});

$('#color_submit').on('click', () => {
	if ($('#change_sel').val() == "Orange") {
		color_RGB = [255,85,0];
	}
	else if ($('#change_sel').val() == "Blue") {
		color_RGB = [0,0,255];
	}
	else if ($('#change_sel').val() == "White") {
		color_RGB = [255,255,255];
	}
	else if ($('#change_sel').val() == "Red") {
		color_RGB = [255,0,0];
	}
	change_player_color();
	rgbString = 'rgb(' + color_RGB[0] + ',' + color_RGB[1] + ',' + color_RGB[2] + ')';
	$('#color_block').css('color',rgbString);
	$('#players').show();
	$('#color_panel').hide();
	$('#ready').show();
});

$('#reset').on('click', () => {
	$('#confirm').show();
	$('#reset').hide();
	$('#players').hide();
});

$('#reset_confirm').on('click', () => {
	new_game();
	//randomize_players();
	$('#confirm').hide();
	$('#add_section').show();
	$('#reset').show();
	$('#ready').hide();
	get_notifications(player,notif_pop);
});

$('#reset_deny').on('click', () => {
	$('#confirm').hide();
	$('#reset').show();
});

$('#ready').on('click', () => {
	//player_ready(); FIX THIS
	var torch = new URLSearchParams();
	torch.append("pname",player);
	torch.append("porder",order);
	$(location).attr('href','./game.html?' + torch.toString());
	get_notifications(player,notif_pop);
});