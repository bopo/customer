function $Showhtml(){
	player='<embed id="cont" type="application/x-shockwave-flash" src="http://static.youku.com/v1.0.0098/v/swf/qplayer.swf" wmode="transparent" id="movie_player" name="movie_player" bgcolor="#FFFFFF" quality="high" allowfullscreen="true" flashvars="isShowRelatedVideo=false&showAd=0&show_pre=1&show_next=1&VideoIDS='+Players.Url+'&isAutoPlay=true&isDebug=false&UserID=&winType=interior&playMovie=true&MMControl=false&MMout=false&RecordCode=1001,1002,1003,1004,1005,1006,2001,3001,3002,3003,3004,3005,3007,3008,9999" pluginspage="http://www.macromedia.com/go/getflashplayer" width="100%" height="'+Players.Height+'"></embed>';
	return player;
}

Players.Show();

if(Players.Second){
	$$('buffer').style.height = Players.Height;
	$$("buffer").style.display = "block";
	setTimeout("Players.BufferHide();",Players.Second*1000);
}
	