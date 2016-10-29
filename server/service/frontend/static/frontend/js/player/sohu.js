function $Showhtml(){
	player = '<embed type="application/x-shockwave-flash" src="http://tv.sohu.com/upload/swf/20101021/Main.swf?isPlayerAd=0&autoplay=true&vid='+Players.Url+'" width="100%" height="'+Players.Height+'" type="application/x-shockwave-flash" allowFullScreen="true" allownetworking="internal" allowscriptaccess="never" wmode="opaque">';
	return player;
}
Players.Show();
if(Players.Second){
	$$('buffer').style.position = 'absolute';
	$$('buffer').style.height = Players.Height;
	$$("buffer").style.display = "block";
	setTimeout("Players.BufferHide();",Players.Second*1000);
}