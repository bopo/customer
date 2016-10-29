function $Showhtml(){
	player = '<embed allowfullscreen="true" wmode="opaque" src="http://Players.cntv.cn/standard/cntvPlayers.swf?v=0.171.5.7.9.0&videoCenterId='+Players.Url+'&videoId=20110711" quality="high" bgcolor="#000" width="100%" height="'+Players.Height+'" name="player" id="playerr" align="middle" allowScriptAccess="always" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer"></embed>';
	return player;
}
Players.Show();
if(Players.Second){
	$$('buffer').style.height = Players.Height-35;
	$$("buffer").style.display = "block";
	setTimeout("Players.BufferHide();",Players.Second*1000);
}