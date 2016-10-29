function $Showhtml(){
	player ='<object width="100%" height="'+Players.Height+'" classid="clsid:1DD5176B-B71E-4956-8F32-691702ACDCFE" onError="Players.Install();">';
	player +='<PARAM NAME="URL" VALUE="'+Players.Url+'">';
	player +='<PARAM NAME="NextWebUrl" VALUE="'+Players.NextUrl+'">';
	player +='</object>';
	return player;
}
$ShowPlayer();