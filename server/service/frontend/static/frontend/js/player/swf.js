function $Showhtml(){
	player ='<object classid="clsid:D27CDB6E-AE6D-11CF-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0" border="0" width="100%" height="'+Players.Height+'" >';
	player += '<param name="movie" value="'+Players.Url+'">';
	player += '<param name="quality" value="High">';
	player += '<embed src="'+Players.Url+'" pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" name="obj1" quality="High" width="100%" height="'+Players.Height+'"></object>';
	return player;
}
Players.Show();