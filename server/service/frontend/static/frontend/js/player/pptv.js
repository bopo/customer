function $Showhtml(){
	player = '<embed src="http://Players.pptv.com/v/'+Players.Url+'.swf" quality="high" width="100%" height="'+Players.Height+'" align="middle" allowScriptAccess="always" allownetworking="all" type="application/x-shockwave-flash" wmode="window" allowFullScreen="true" play="true"></embed>';
	return player;
}
Players.Show();
if(Players.Second){
	$$('buffer').style.position = 'absolute';
	$$('buffer').style.height = Players.Height-40;
	$$("buffer").style.display = "block";
	setTimeout("Players.BufferHide();",Players.Second*1000);
}