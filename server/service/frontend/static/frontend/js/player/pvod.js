function $Showhtml(){
	player ='<object width="100%" height="'+Players.Height+'" classid="clsid:A74BF134-5213-46B5-AF36-CE1888315DC7" onError="Players.Install();" id="pipiwebplayer_control">';
	player +='<PARAM NAME="URL" VALUE="'+Players.Url+'">';
	player +='<PARAM NAME="lActiveXStyle" VALUE="1">';
	player +='</object>';
	return player;
}
Players.Show();
try {
	new ActiveXObject("PIPIWEBPlayers.PIPIWebPlayerCtrl.1");
	document.getElementById("pipiwebplayer_control").playurl(Players.Url);
} catch(e) {}