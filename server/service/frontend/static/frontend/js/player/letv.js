function $Showhtml(){
	player  = '<object width="'+Players.Width+'" height="'+Players.Height+'">';
	player += '<param name="allowFullScreen" value="true" />';
	player += '<param name="flashVars" value="id='+Players.Url+'" />';
	player += '<param name="movie" value="http://i7.imgs.letv.com/player/swfPlayer.swf?autoplay=1" />';
	player += '<embed src="http://i7.imgs.letv.com/player/swfPlayer.swf?autoplay=1" flashVars="id='+Players.Url+'" width="'+Players.Width+'" height="'+Players.Height+'" allowFullScreen="true" type="application/x-shockwave-flash" />';
	player += '</object>';
	return player;
}

Players.Show();

if(Players.Second){
	$$('buffer').style.height = Players.Height-45;
	$$("buffer").style.display = "block";
	setTimeout("Players.BufferHide();",Players.Second*1000);
}
