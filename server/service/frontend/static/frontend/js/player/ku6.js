function $Showhtml(){
	player = '<embed type="application/x-shockwave-flash" src="http://Players.ku6cdn.com/default/out/pV2.7.3.swf" id="mymovie" name="mymovie" quality="high" flashvars="ver=108&amp;jump=0&amp;api=1&amp;auto=1&amp;color=0&amp;deflogo=0&amp;flag=hd&amp;adss=0&amp;vid='+Players.Url+'&amp;type=v" wmode="transparent" allowscriptaccess="always" allowfullscreen="true" width="100%" height="'+Players.Height+'">';
	return player;
}
Players.Show();
if(Players.Second){
	$$('buffer').style.position = 'absolute';
	$$('buffer').style.height = Players.Height-60;
	$$("buffer").style.display = "block";
	setTimeout("Players.BufferHide();",Players.Second*1000);
}