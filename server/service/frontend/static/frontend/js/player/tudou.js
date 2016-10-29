function $Showhtml(){
	player = '<embed allowNetworking="internal" allowFullScreen="true" allowscriptaccess="never" src="http://www.tudou.com/a/oO9sKFzT3Gs/&resourceId=0_05_05_99&iid='+Players.Url+'&bid=05/v.swf&autoPlay=true" type="application/x-shockwave-flash" width="100%" height="'+Players.Height+'"></embed>';
	return player;
}

Players.Show();
Players.Show();

if(Players.Second){
	$$('buffer').style.height = Players.Height-20;
	$$("buffer").style.display = "block";
	setTimeout("Players.BufferHide();",Players.Second*1000);
}