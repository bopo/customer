function $Showhtml(){
	player ='<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" codebase="http://fpdownload.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=8,0,0,0" width="100%" height="'+Players.Height+'">';
	player +='<param name="movie" value="'+ff_root+'assets/scripts/player/flv.swf"><param name="quality" value="high">';
	player +='<param name="menu" value="false"><param name="wmode" value="opaque"><param name="allowFullScreen" value="true" />';
	player +='<param name="FlashVars" value="vcastr_file='+Players.Url+'&vcastr_title=adn&IsAutoPlay=1">';
	player +='<embed src="'+ff_root+'assets/scripts/player/flv.swf" allowFullScreen="true" FlashVars="vcastr_file='+Players.Url+'&vcastr_title=www.feifeicms.com&IsAutoPlay=1" menu="false" quality="high" width="100%" height="'+Players.Height+'" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer" /></object>';
	return player;
}

Players.Show();
