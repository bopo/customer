function $Showhtml(){
	Players.Url = $Coolurl(Players.Url,Players.UrlName);
	Players.NextUrl = $Coolurl(Players.NextUrl,Players.UrlNextName);
	player ='<object id="CoolPlayer" name="CoolPlayer" width="100%" height="'+Players.Height+'" classid="clsid:73BAB958-AC02-5108-B2B8-665834A9C63A" onError="Players.Install();" style="display:none;">';
	player +='<PARAM NAME="URL" VALUE="'+Players.Url+'">';
	player +='<PARAM NAME="Autoplay" VALUE="1">';
	player +='<PARAM NAME="CoolAdUrl" VALUE="'+Players.Buffer+'">';
	player +='<PARAM NAME="NextWebPage" VALUE="'+Players.NextWebPage+'">';
	player +='</object>';
	if(!window.ActiveXObject){
		player +='<embed URL="'+Players.Url+'" type="application/cool-plugin" width="100%" height="'+Players.Height+'" onError="Players.Install();" ></embed>';
	}
	return player;
}
function $CoolStatus(){
	if(CoolPlayers.Full == 0){
		if(CoolPlayers.PlayState == 3){
			$$('buffer').style.display = 'none';
		}else{
			$$('buffer').style.display = 'block';
		}
	}
}
function $CoolNextDown(){
	if(CoolPlayers.get_CurTaskProcess() > 900 && !bstartnextplay){
		CoolPlayers.StartNextDown(Players.NextUrl);
		bstartnextplay = true;
	}
}
function $Coolurl(url,urlname){
	if(url.indexOf("cool://")>0){
		url = url.split("|");
		coolurl = url[0]+"|"+url[1]+"|"+urlname+"[www.feifeicms.com].rmvb|";
		return coolurl;
	}
	return url;
}
ff_cool = '';
Players.Show();
if(CoolPlayers.URL != undefined){
	$$('buffer').height = Players.Height-60;
	CoolPlayers.style.display = 'block';
	setInterval("$CoolStatus()",500);
	if(Players.NextWebPage){
		var bstartnextplay = false;
		setInterval("$CoolNextDown()",9333);
	}
}