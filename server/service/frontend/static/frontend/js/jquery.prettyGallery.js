function PlayHistoryClass(){
	var cookieStr,nameArray,urlArray,allVideoArray;
	this.getPlayArray=function (){
		cookieStr = document.cookie;
		var start = cookieStr.indexOf("pp_vod_v=") + "pp_vod_v=".length,end = cookieStr.indexOf("_$_|",start),allCookieStr= unescape(cookieStr.substring(start,end))
		if(end==-1){allCookieStr="";return;}
		allVideoArray = allCookieStr.split("_$_");
		nameArray = new Array(),urlArray = new Array();
		for(var i = 0; i < allVideoArray.length; i++){
			var singleVideoArray = allVideoArray[i].split("^");
			nameArray[i] = singleVideoArray[0];urlArray[i] = singleVideoArray[1];
		}
	}
	this.viewPlayHistory=function (div){
		var tag = document.getElementById(div),n = 12;
		
		if(navigator.cookieEnabled){
			var innerStr = "";
			if(nameArray!=undefined&&nameArray!=null){
			for(var i =nameArray.length - 1; i >= 0; i--){
				var textCount = nameArray[i].replace(/[^\x00-\xff]/g,"cc").length;
				if(textCount <= n*2){
					texts = nameArray[i];
				}else{
					texts = nameArray[i].substr(0,n)+"...";
				}
				//innerStr += "<li><a target=_blank class=name href=\"" + urlArray[i] + "\"" + " title=\"" + nameArray[i] + "\">" + texts + "</a><a target=_blank class=now href=\"" + urlArray[i] + "\"" + " title=\"" + nameArray[i] + "\">�����ۿ�</a></li>"
				innerStr += "<li><h5><a href=\"" + urlArray[i] + "\">"+nameArray[i]+"</a></h5><label><a class=\"color\" href=\"" + urlArray[i] + "\">�����ۿ�</a></label></li>"

		}
	}
			$("#his-todo").show();
			$("#morelog").hide();	
			if(innerStr.length>0){
				$("#emptybt").unbind();
				$("#emptybt").click(function(){
					PlayHistoryObj.emptyhistory('ck');
				});
				tag.innerHTML= innerStr;$(".delck").click(function(e){
					if(PlayHistoryObj.removeHistory($(this).attr('data'),$(this).attr('mtype'))){
						$(this).parents('li').remove();
					}
				});
			}
			else{
				document.getElementById('playhistory').innerHTML="<li class='no-his'><p>���޲�����ʷ�б�...</p></li>";
			}
		}else{
			set(tag,"��������ر���cookie���ܣ�����Ϊ���Զ�����������������ҳ��")
		}
	}
	
	this.addPlayHistory=function (name,url,cid){
		
		var count = 10; //������ʷ�б��������
		var code_name = escape(name) + "^",code_url = escape(url) + "_$_",expireTime = new Date(new Date().setDate(new Date().getDate() + 30)),timeAndPathStr = "|; expires=" + expireTime.toGMTString() + "; path=/";
		if((cookieStr.indexOf("pp_vod_v=") != -1 || cookieStr.indexOf("_$_|") != -1)&&allVideoArray!=undefined){
			var newCookieStr = "";
			if(allVideoArray.length < count){
				for(i in allVideoArray){
					if(nameArray[i] == name) continue;
					newCookieStr += escape(nameArray[i]) + "^" + escape(urlArray[i]) + "_$_" ;
				}
			}else{
				for(var i = 1; i < count; i++){
					if(nameArray[i] == name) continue;
					newCookieStr += escape(nameArray[i]) + "^" + escape(urlArray[i]) + "_$_" ;
				}
			}
		//	alert("pp_vod_v=" + newCookieStr + code_name + code_url + timeAndPathStr);
			document.cookie = "pp_vod_v=" + newCookieStr + code_name + code_url + timeAndPathStr;
		}else{
		//	alert("pp_vod_v="+ code_name + code_url + timeAndPathStr);
			document.cookie = "pp_vod_v="+ code_name + code_url + timeAndPathStr;
		}
	}

}
//var cookiedomain="1.22";
function _GC(){
	document.getElementById('playhistory').innerHTML="<li class='no-his'><p>���޲�����ʷ�б�...</p></li>";
	var expdate=new Date(1970, 1, 1);
	document.cookie = "pp_vod_v=; path=/";
}
var PlayHistoryObj=new PlayHistoryClass()
PlayHistoryObj.getPlayArray()
function killErrors() {
    return true;
}
//window.onerror = killErrors;