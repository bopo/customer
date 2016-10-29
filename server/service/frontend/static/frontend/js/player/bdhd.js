var BdPlayer = new Array();
Players.Url = $BdhdUrl(Players.Url,Players.UrlName);
Players.NextUrl = $BdhdUrl(Players.NextUrl,Players.UrlNextName);
if(Players.Url == Players.NextUrl){ Players.NextUrl = ''; }
BdPlayer['time'] = Players.Second;//缓冲广告展示时间(如果设为0,则根据缓冲进度自动控制广告展示时间)
BdPlayer['buffer'] = Players.Buffer;//贴片广告网页地址
BdPlayer['pause'] = Players.Buffer;//暂停广告网页地址
BdPlayer['end'] = Players.Buffer;//影片播放完成后加载的广告
BdPlayer['download'] = ff_bdhd;//播放器下载地址
BdPlayer['width'] = '100%';//播放器宽度(只能为数字)
BdPlayer['height'] = Players.Height;//播放器高度(只能为数字)
BdPlayer['showclient'] = 1;//是否显示拉起拖盘按钮(1为显示 0为隐藏)
BdPlayer['url'] =  Players.Url;//当前播放任务播放地址
BdPlayer['nextcacheurl'] = Players.NextUrl;//下一集播放地址(没有请留空)
BdPlayer['lastwebpage'] = Players.LastWebPage;//上一集网页地址(没有请留空)
BdPlayer['nextwebpage'] = Players.NextWebPage;//下一集网页地址(没有请留空)
document.write('<scr'+'ipt language="javascript" src="/assets/scripts/player/bdplayer.js" charset="utf-8"></scr'+'ipt>');
function $BdhdUrl(url,urlname){
	if(url.indexOf("bdhd://")>0){
		onurl = url.split("|");
		//获取地址后缀
		var parts = onurl[2].split(".");
		if (parts.length > 1) {
			suffix = parts.pop();
		}else{
			suffix = 'rmvb';
		}
		return(onurl[0]+"|"+onurl[1]+"|"+vod_name+"[www.mi-tang.com]"+urlname+"."+suffix);
	}
	return(url);
}
Players.Show();