
function $Showhtml(){
//	player ='<OBJECT id=flvplayer1 classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" codebase="http://fpdownload.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,0,0" width="100%" height="'+Players.Height+'" align="middle">';
//	player +='<PARAM NAME="Movie" VALUE="http://www.qiyi.com/player/20110714102816/qiyi_n_player.swf">';
//	player +='<param name="allowFullScreen" value="true" />';
//	player +='<param name="wmode" value="transparent" />';
//	player +='<param name="AllowScriptAccess" value="always" />';
//	player +='<param name="quality" value="high" />';
//	player +='<PARAM NAME="FlashVars" VALUE="flag=0&vid='+Players.Url+'">';
//	player +='<embed allowfullscreen="true" wmode="transparent" quality="high" src="http://www.qiyi.com/player/20110714102816/qiyi_n_player.swf?flag=1&vid='+Players.Url+'" quality="high" bgcolor="#000" width="100%" height="'+Players.Height+'" name="player" id="playerr" align="middle" allowScriptAccess="always" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer">';
//	player +='</object>';
//
//	var wdurl = unescape(window.location.href);
//	var allargs = wdurl.split("&");
//	var url=allargs[1].split("a=")[1];
//	var w=allargs[2].split("w=")[1];
//	var h=allargs[3].split("h=")[1];
//	url=url.replace(/-/g,"&");
//
//	if(url.indexOf("vid=") > -1 )
//		player = '<embed bgcolor="#000000" type="application/x-shockwave-flash" src="http://www.qiyi.com/player/20110714102816/qiyi_n_player.swf" width="100%" height="'+Players.Height+'" quality="high" allowfullscreen="true" allowscriptaccess="always" wmode="Opaque" flashvars="'+Players.Url+'&coop=qc_200010_300010">';
//	else

    player = "<embed pluginspage=\"http://www.macromedia.com/go/getflashplayer\" loop=\"true\" play=\"true\" quality=\"hight\" scale=\"showall\" devicefont=\"false\" allowfullscreen=\"true\" menu=\"true\" type=\"application/x-shockwave-flash\" width=\"100%\" height=\""+Players.Height+"\" src=\"http://dispatcher.video.qiyi.com/disp/shareplayer.swf\" id=\"flash\" bgcolor=\"#000000\" flashvars=\"vid="+Players.Url+"&amp;coop=coop_yiyi&amp;cid=qc_0000&amp;bd=1&amp;autoPlay=1\" align=\"middle\" allowscriptaccess=\"always\">";

	return player;
}

Players.Show();

if(Players.Second){
	$$('buffer').style.height = Players.Height-30;
	$$("buffer").style.display = "block";
	setTimeout("Players.BufferHide();",Players.Second * 1000);
}