/* @name: 飞飞PHP影视系统JS
 * @version: 2.0.beta4
 * @lasttime: 2012-01-16
 * 	FF.Home
		.Url;
		.Getchannel(sid);
		.Js();
	FF.UpDown
 		.Vod(ajaxurl);
		.News(ajaxurl);
		.Show(up=100:down=88,model);
	FF.Comment
		.Show(ajaxurl);
		.Post();
	FF.Gold
		.Default(ajaxurl);
		.Show(ajaxurl);
	FF.Lazyload
   		.Show();
   		.Box('idname');
	FF.Suggest
   		.Show(id,limit,ajaxurl,jumpurl);
	FF.Cookie
 		.Set(name,value,days);
		.Get(name);
		.Del(name);
	FF.History
		.Insert(vodname,vodlink,limit,days,cidname,vodpic);
		.List(id);
 */

var FF = {
	//初始化前端js
	'Home': {
		'Url': document.URL,
		'Tpl': 'defalut',
		'Channel': '',
		'GetChannel': function ($sid){
			if($sid == '1') return 'vod';
			if($sid == '2') return 'news';
			if($sid == '3') return 'special';
		},
		'searchInput':function($objct,$fromobjct){
			if($objct.length>0){
				//改变action目标地址
				if(Sid == '2'){
					$key = '输入关键字';
					$fromobjct.attr('action', Root+'index.php?s=news-search');
				}else{
					$key = '输入影片名称或主演名称';
				}
				//默认搜索框关键字
				if($objct.val() == ''){
					$objct.val($key);
				}
				//搜索框获得焦点
				$objct.focus(function(){
					if($objct.val() == $key){
						$objct.val('');
					}
				});
				//搜索框失去焦点
				$objct.blur(function(){
					if($objct.val() == ''){
						$objct.val($key);
					}
				});
				$fromobjct.submit(function(){
					if($objct.val() == $key || $.trim($objct.val()) == '' ){
						$objct.val("");
						$objct.focus();
						return false;
					}
				});
			}
		},
		'Sc': function($objct) {
			//加入收藏夹
			$objct.click(function(e){
				var url = window.location.href;
				try{
					window.external.addFavorite(url,document.title);
				}catch(err){
					try{
						window.sidebar.addPanel(document.title, url,"");
					}catch(err){
						alert("请使用Ctrl+D为您的浏览器添加书签！");
					}
				}
				return false;
			});
		},
		'Js': function() {
			//获取频道名
			this.Channel = this.GetChannel(Sid);
		}
	},
	//监听顶踩操作事件
	'UpDown': {
		'Vod': function($ajaxurl) {
			if($("#Up").length || $("#Down").length){
				FF.UpDown.Ajax($ajaxurl, 'video', '');
			}
			$('.Up').click(function(){
				FF.UpDown.Ajax($ajaxurl, 'video', 'up');
			});
			$('.Down').click(function(){
				FF.UpDown.Ajax($ajaxurl, 'video', 'down');
			});
		},
		'News': function($ajaxurl) {
			if($("#Digup").length || $("#Digdown").length){
				this.Ajax($ajaxurl,'news','');
			}else{
				FF.UpDown.Show($("#Digup_val").html()+':'+$("#Digdown_val").html(),'news');
			}
			$('.Digup').click(function(){
				FF.UpDown.Ajax($ajaxurl,'news','up');
			})
			$('.Digdown').click(function(){
				FF.UpDown.Ajax($ajaxurl,'news','down');
			})
		},
		'Ajax': function($ajaxurl, $model, $ajaxtype){
			$.ajax({
				type: 'get',
				url: $ajaxurl + '/' + $ajaxtype,
				timeout: 5000,
				dataType:'json',
				success:function($html){
					if(!$html.status){
						alert($html.info);
					}else{
						FF.UpDown.Show($html.data, $model);
					}
				}
			});
		},
		'Show': function ($html, $model){
			if($model == 'vod'){
				$(".Up>span").html($html.split(':')[0]);
				$(".Down>span").html($html.split(':')[1]);
			}else if($model = 'news'){
				var Digs = $html.split(':');
				var sUp = parseInt(Digs[0]);
				var sDown = parseInt(Digs[1]);
				var sTotal = sUp+sDown;
				var spUp=(sUp/sTotal)*100;
				spUp = Math.round(spUp*10)/10;
				var spDown = 100-spUp;
				spDown = Math.round(spDown*10)/10;
				if(sTotal!=0){
					$('#Digup_val').html(sUp);
					$('#Digdown_val').html(sDown);
					$('#Digup_sp').html(spUp+'%');
					$('#Digdown_sp').html(spDown+'%');
					$('#Digup_img').width(parseInt((sUp/sTotal)*55));
					$('#Digdown_img').width(parseInt((sDown/sTotal)*55));
				}
			}
		}
	},
	//监听评论操作事件
	'Comment': {
		'Show': function($ajaxurl) {
			if($("#Comment").length>0){
				$.ajax({
					type: 'get',
					url: $ajaxurl,
					timeout: 5000,
					error: function(){
						$("#Comment").html('评论加载失败，请刷新...');
					},
					success:function($html){
						$("#Comment").html($html);
					}
				});
			}
		},
		'Post': function(){
			if($("#comment_content").val() == '请在这里发表您的个人看法，最多200个字。'){
				$('#comment_tips').html('请发表您的评论观点！');
				return false;
			}
			var $data = "cm_sid="+Sid+"&cm_cid="+Id+"&cm_content="+$("#comment_content").val();
			$.ajax({
				type: 'post',
				url: Root+'index.php?s=Cm-insert',
				data: $data,
				dataType:'json',
				success:function($string){
					if($string.status == 1){
						Comment.Show(Root+"index.php?s=Cm-Show-sid-"+Sid+"-id-"+Id+"-p-1");
					}
					$('#comment_tips').html($string.info);
				}
			});
		}
	},

	//监听评分事件
	'Gold': {
		'Default': function($ajaxurl){
			if($("#Gold").length>0 || $("#Goldnum").length>0){
				$.ajax({
					type: 'get',
					url: $ajaxurl,
					timeout: 5000,
					dataType:'json',
					error: function(){
						$(".Gold").html('评分加载失败');
					},
					success: function($html){
						FF.Gold.Show($ajaxurl,$html.data,'');
					}
				});
			}else{
				if($(".Gold").length>0 || $(".Goldnum").length>0){
					FF.Gold.Show($ajaxurl,$(".Goldnum").html()+':'+$(".Golder").html(),'');
				}
			}
		},
		'Show': function($ajaxurl,$html,$status){
			//去除与创建title提示
			$(".Goldtitle").remove();
			$(".Gold").after('<span class="Goldtitle" style="width:'+$(".Gold").width()+'px"></span>');
			//$(".Goldtitle").css({margin:'30px 0 0 -140px'});
			if($status == 'onclick'){
				$(".Goldtitle").html('评分成功！');
				$(".Goldtitle").show();
				$status = '';
			}
			//展示星级>评分>评分人
			$("#Gold").html(FF.Gold.List($html.split(':')[0]));
			$goldn = $html.split(':')[0];
			$goldn = "<span class='gol_x'>"+$goldn.split('.')[0]+"</span><span class='gol_n'>."+$goldn.split('.')[1]+"</span>";
			$(".Goldnum").html($goldn);
			$(".Golder").html($html.split(':')[1]);
			//鼠标划过
			$("#Gold>span").mouseover(function(){
				$id = $(this).attr('id')*1;
				$(".Goldtitle").html(FF.Gold.Title($id*2));
				$(".Goldtitle").show();
				//刷新星级图标
				$bgurl = $(this).css('background-image');
				for(i=0;i<5;i++){
					if(i>$id){
						$(".Gold>#"+i+"").css({background:$bgurl+" 56px 0 repeat"});
					}else{
						$(".Gold>#"+i+"").css({background:$bgurl});
					}
				}
			});
			//鼠标移出
			$("#Gold>span").mouseout(function(){
				//去除title提示
				$(".Goldtitle").hide();
				//刷新星级图标
				$score = $html.split(':')[0]*1/2;
				$id = $(this).attr('id')*1;
				$bgurl = $(this).css('background-image');
				for(i=0;i<5;i++){
					if(i<Math.round($score)){
						if(i == parseInt($score)){
							$(".Gold>#"+i+"").css({background:$bgurl+" 28px 0 repeat"});
						}else{
							$(".Gold>#"+i+"").css({background:$bgurl});
						}
					}else{
						$(".Gold>#"+i+"").css({background:$bgurl+" 56px 0 repeat"});
					}
				}
			});
			//鼠标点击
			$("#Gold > span").click(function(){
				$.ajax({
					type: 'get',
					url: $ajaxurl + '/' + (($(this).attr('id') * 1 + 1) * 2),
					timeout: 5000,
					dataType:'json',
					error: function(){
						$(".Goldtitle").html('评分失败!');
					},
					success: function($html){
						if(!$html.status){
							$(".Goldtitle").html($html.info);
							$(".Goldtitle").show();
						}else{
							FF.Gold.Show($ajaxurl,$html.data,'onclick');
						}
					}
				});
			});
		},
		//星级评分展示
		'List': function($score){
			var $html = '';
			$score = $score/2;
			for(var i = 0 ; i<5; i++){
				var classname = 'all';
				if(i < $score && i<Math.round($score)){
					if(i == parseInt($score)){
						classname = 'half';
					}
				}else{
					classname = 'none';
				}
				$html += '<span id="'+i+'" class="'+classname+'"></span>';// title="'+this.GoldTitle(i*2)+'"
			}
			return $html;
		},
		//提示信息
		'Title': function($score){//星级鼠标浮层提示信息
			var array_str = ['很差，浪费时间！','一般，平庸之作！','不错，不妨一看！','很好，佳作之品！','力荐，不容错过！'];
			var $score = parseFloat($score);
			if($score < 2.0) return array_str[0];
			if($score>=2.0 && $score<4.0) return array_str[1];
			if($score>=4.0 && $score<6.0) return array_str[2];
			if($score>=6.0 && $score<8.0) return array_str[3];
			if($score>=8.0) return array_str[4];
		}
	},
	//图片延时加载 FF.Lazyload.Box('frame'); <img class="lazy" data-original="{$ppvod.vod_picurl}" src="/images/blank.gif" alt="xx" />
	'Lazyload':{
		'Show': function(){
			$("img.lazy").lazyload();
		},
		//指定ID范围内的效果
		'Box': function($id){
			$("img.lazy").lazyload({
				 container: $("#"+$id)
			});
		}
	},
	//搜索联想 FF.Suggest.Show('wd',10,'index.php?s=plus-search-index','index.php?s=vod-search-wd-');
	'Suggest': {
		'Show': function($id,$limit,$ajaxurl,$jumpurl){
			$("#"+$id).autocomplete($ajaxurl, {
				width: 294,
				scrollHeight: 300,
				minChars: 1,
				matchSubset: 1,
				max: $limit,
				delay:400,
				cacheLength: 10,
				multiple: true,
				matchContains: true,
				autoFill: false,
				dataType: "json",
				parse:function(obj) {//解释返回的数据，把其存在数组里，返回给要输出的item
					if(obj.status){
						var parsed = [];
						for (var i = 0; i < obj.data.length; i++) {
							parsed[i] = {
								data: obj.data[i],
								value: obj.data[i].vod_name,
								result: obj.data[i].vod_name//返回的结果显示内容
							};
						}
						return parsed;
					}else{
						return {data:'',value:'',result:''};
					}
				},
				formatItem: function(row,i,max) {
					return row.vod_name;
				},
				formatResult: function(row,i,max) {
					return row.vod_name;//replace(/(<.+?>)/gi, '')
				}
			}).result(function(event, data, formatted) {
				location.href = $jumpurl+encodeURIComponent(data.vod_name);
			});
		}
	},
	//Cookie FF.Cookie.Set(name,value,days);
	'Cookie': {
		'Set': function(name,value,days){
			var exp = new Date();
			exp.setTime(exp.getTime() + days*24*60*60*1000);
			var arr=document.cookie.match(new RegExp("(^| )"+name+"=([^;]*)(;|$)"));
			document.cookie=name+"="+escape(value)+";path=/;expires="+exp.toUTCString();
		},
		'Get': function(name){
			var arr = document.cookie.match(new RegExp("(^| )"+name+"=([^;]*)(;|$)"));
			if(arr != null){
				return unescape(arr[2]);
				return null;
			}
		},
		'Del': function(name){
			var exp = new Date();
			exp.setTime(exp.getTime()-1);
			var cval = this.Get(name);
			if(cval != null){
				document.cookie = name+"="+escape(cval)+";path=/;expires="+exp.toUTCString();
			}
		}
	},
	'Bdhddown': {
		'Display': true,
		'Info': function($id){
			$('#'+$id).hover(function(){
				FF.Bdhddown.Show();
			}, function(){
				FF.Bdhddown.FlagHide();
			});
		},
		'Show': function(){
			var w = $('#bdhddown').width();
			var h = $('#bdhddown').height();
			var boxw = $('#bdhddown_box').width();

			var position = $('#bdhddown').position();

			$('#bdhddown_box').css({'left':position.left+w-boxw+124,'top':(position.top+28)});
			$('#bdhddown_box').show();
		},
		'Hide': function(){
			$('#bdhddown_box').hide();
		},
		'FlagHide': function(){
			$('#bdhddown_box').hover(function(){
				FF.Bdhddown.Display = false;
				FF.Bdhddown.Show();
			}, function(){
				FF.Bdhddown.Display = true;
				FF.Bdhddown.Hide();
			});
			if(FF.Bdhddown.Display){
				FF.Bdhddown.Hide();
			}
		}
	},
	//观看历史记录 FF.History.Insert('硝烟背后的战争','',10,1,'','')
	'History': {
		'Json': '',
		'Display': true,
		'List': function($id){
			this.Create($id);
			$('#'+$id).hover(function(){
				FF.History.Show();
			}, function(){
				FF.History.FlagHide();
				/*setTimeout(function() {
					FF.History.FlagHide();
				}, 200);*/
			});
		},
		'Clear': function(){
			FF.Cookie.Del('FF_Cookie');
			$('#history_box').html('<dd class="hide">已清空观看记录</dd>');
		},
		'Show': function(){

			var w = $('#history').width();
			var h = $('#history').height();
			var boxw = $('#history_box').width();

			var position = $('#history').position();
			$('#history_box').css({'left':position.left+w-boxw-2,'top':(position.top+28)});

			$('#history_box').show();
		},
		'Hide': function(){
			$('#history_box').hide();
		},
		'FlagHide': function(){
			$('#history_box').hover(function(){
				FF.History.Display = false;
				FF.History.Show();
			}, function(){
				FF.History.Display = true;
				FF.History.Hide();
			});
			if(FF.History.Display){
				FF.History.Hide();
			}
		},
		'Create': function($id){
			var jsondata = [];
			if(this.Json){
				jsondata = this.Json;
			}else{
				var jsonstr = FF.Cookie.Get('FF_Cookie');
				if(jsonstr != undefined){
					jsondata = eval(jsonstr);
				}
			}
			html = '<dl class="history_box" id="history_box"><div class="history_box_b">';
			html +='<dt><a href="javascript:void(0)" onclick="FF.History.Hide();">关闭</a><a href="javascript:void(0)" onclick="FF.History.Clear();">清空</a><div class="cl"></div></dt>';
			html +='<div class="ddbox">';
			if(jsondata.length > 0){
				for($i=0; $i<jsondata.length; $i++){
					if($i%2==1){
						html +='<dd class="odd">';
					}else{
						html +='<dd class="even">';
					}
					html +='<a href="'+jsondata[$i].vodlink+'" class="hx_title">'+jsondata[$i].vodname+'&nbsp;</a></dd>';
				}
			}else{
				html +='<dd class="hide">暂无观看记录&nbsp;</dd>';
			}
			html += '</div></div></dl>';
			$('#history').after(html);

			var w = $('#'+$id).width();
			var h = $('#'+$id).height();
			var boxw = $('#'+ $id +"_box").width();

			var position = $('#'+$id).position();
			$('#history_box').css({'left':position.left+w-boxw,'top':(position.top+h)});

			//$('#history_box').width(w);
		},
		'SmallMenuHistoryList': function($id){
			var jsondata = [];
			if(this.Json){
				jsondata = this.Json;
			}else{
				var jsonstr = FF.Cookie.Get('FF_Cookie');
				if(jsonstr != undefined){
					jsondata = eval(jsonstr);
				}
			}
			var html='';
			if(jsondata.length > 0){
				for($i=0; $i<jsondata.length; $i++){
					if($i%2==1){
						html +='<div class="odd">';
					}else{
						html +='<div class="even">';
					}
					html +='<a href="'+jsondata[$i].vodlink+'" class="hx_title">'+jsondata[$i].vodname+'&nbsp;</a></div>';
				}
			}else{
				html +='<div class="noitds">&nbsp;暂无观看记录&nbsp;</div>';
			}
			html +='<div class="clearbox"><a href="javascript:void(0)" onclick="FF.History.SmallMenuHistoryClear(\'smallhistory\');">清空</a><div class="cl"></div></div>';
			$('#'+$id).html(html);

		},
		'SmallMenuHistoryClear': function($id){
			FF.Cookie.Del('FF_Cookie');
			$('#'+$id).html('<div class="noitds">&nbsp;已清空观看记录&nbsp;</div><div class="clearbox"><a href="javascript:void(0)" onclick="FF.History.SmallMenuHistoryClear(\'smallhistory\');">清空</a><div class="cl"></div></div>');
		},
		'Insert': function(vodname, vodlink, limit, days, cidname, vodpic){
			var jsondata = FF.Cookie.Get('FF_Cookie');
			if(jsondata != undefined){
				this.Json = eval(jsondata);
				//排重
				for($i=0;$i<this.Json.length;$i++){
					if(this.Json[$i].vodlink == vodlink){
						return false;
					}
				}
				//组合新json
				if(!vodlink){vodlink = document.URL;}
				jsonstr = '{video:[{"vodname":"'+vodname+'","vodlink":"'+vodlink+'","cidname":"'+cidname+'","vodpic":"'+vodpic+'"},';
				for($i = 0; $i <= limit; $i++){
					if(this.Json[$i]){
						jsonstr += '{"vodname":"'+this.Json[$i].vodname+'","vodlink":"'+this.Json[$i].vodlink+'","cidname":"'+this.Json[$i].cidname+$i+'","vodpic":"'+this.Json[$i].vodpic+'"},';
					}else{
						break;//continue;
					}
				}
				jsonstr = jsonstr.substring(0,jsonstr.lastIndexOf(','));
				jsonstr += "]}";
			}else{
				jsonstr = '{video:[{"vodname":"'+vodname+'","vodlink":"'+vodlink+'","cidname":"'+cidname+'","vodpic":"'+vodpic+'"}]}';
			}

			this.Json = eval(jsonstr);
			FF.Cookie.Set('FF_Cookie',jsonstr,days);
		}
	}
}
var pagego = function($url,$total){
	$page = document.getElementById('page').value;
	if($page>0 && ($page<=$total)){
		$url=$url.replace('{!page!}',$page);
		if($url.split('index-1')){
			$url=$url.split('index-1')[0];
		}
		top.location.href = $url;
	}
	return false;
}
$.fn.studyplay_star=function(options,callback){
	var settings ={
		MaxStar      :20,
		StarWidth    :24,
		CurrentStar  :5,
		Enabled      :true,
		Ajaxurl      :''
	};
	if(options){jQuery.extend(settings,options);};
	$.ajax({
		type: 'get',
		url: settings.Ajaxurl,
		timeout: 5000,
		dataType:'json',
		error: function(){},
		success: function($html){
			if($html.status==1)
			{
				$("#studyplay_current").width($html.data.split(':')[0]*settings.StarWidth);
				$goldn = $html.data.split(':')[0];
				$goldn = "<span class='gol_x'>"+$goldn.split('.')[0]+"</span><span class='gol_n'>."+$goldn.split('.')[1]+"</span>";
				$(".Goldnum").html($goldn);
				$("#golder").html($html.data.split(':')[1]);
				$(".Goldtitle").html('<span class="artglod">'+$html.data.split(':')[0]+'</span><span class="arttxt">'+$html.info+'</span>');
				$("#zgoldtxtbox").html(stv($html.data.split(':')[0]));
			}
			else
			{
				$(".Goldtitle").html('<span class="artglod">0</span><span class="arttxt">'+$html.info+'</span>');
			}
		}
	});
	var container = jQuery(this);
	if(container.html()!=""){settings.CurrentStar = parseFloat(container.html());}
	container.css({"position":"relative"})
	.html('<ul class="studyplay_starBg"></ul>')
	.find('.studyplay_starBg').width(settings.MaxStar*settings.StarWidth)
	.html('<li class="studyplay_starovering" style="width:'+settings.CurrentStar*settings.StarWidth+'px; z-index:0;" id="studyplay_current"></li>');
	$(".goldbox").append('<span class="Goldtitle" style="width:240px"></span>');
	if(settings.Enabled)
	{
		var ListArray = "";
		for(k=1;k<settings.MaxStar*2+1;k++)
		{
			var n=settings.StarWidth*k/2;
			var z=(settings.MaxStar-k+10);
			var m=(settings.MaxStar-k+1);
			ListArray +='<li bsn="'+m+'" class="studyplay_starON" style="width:'+n+'px;z-index:'+z+';"></li>';
		}
		var stv = function($score){
			var array_str = ['很差，浪费时间！&nbsp;','一般，平庸之作！&nbsp;','不错，不妨一看！&nbsp;','很好，佳作之品！&nbsp;','力荐，不容错过！&nbsp;'];
			var $score = parseFloat($score);
			if($score < 2.0) return array_str[0];
			if($score>=2.0 && $score<4.0) return array_str[1];
			if($score>=4.0 && $score<6.0) return array_str[2];
			if($score>=6.0 && $score<8.0) return array_str[3];
			if($score>=8.0) return array_str[4];
		}
		var returnFloat1 =function(value) { //保留一位小数点
			if(value<10)
			{
				value = Math.round(parseFloat(value) * 10) / 10;
				if (value.toString().indexOf(".") < 0)
				value = value.toString() + ".0";
			}
			return value;
		}
		container.find('.studyplay_starBg').append(ListArray).hover(function(){$("#studyplay_current").hide();$(".Goldtitle").show()},function(){$(".Goldtitle").hide();$(".studyplay_starovering").removeClass('studyplay_starovering');$("#studyplay_current").addClass("studyplay_starovering").show();});
		container.find('.studyplay_starON').hover(
            function(){
                $strsobj = $(".studyplay_starovering");
                $(this).addClass("studyplay_starovering");
                var studyplay_count = settings.MaxStar - $(this).attr("bsn")+1;
                var goldn = studyplay_count/2;
                $(".Goldtitle").html('<span class="artglod">'+returnFloat1(goldn)+'</span><span class="arttxt">'+stv(goldn)+'</span>');
                $strsobj.removeClass('studyplay_starovering');
            },
            function(){
                /*$(this).removeClass('studyplay_starovering');*/
            }).click(
            function(){
                var studyplay_count = settings.MaxStar - $(this).attr("bsn")+1;
                $.ajax({
                    type: 'get',
                    url: settings.Ajaxurl+'/'+(studyplay_count/2),
                    timeout: 5000,
                    dataType:'json',
                    error: function(){
                        //$(".Gold").html('评分加载失败');
                    },
                    success: function($html){
                        //$html.info
                        //$html.status
                        //$html.data.split(':')[0]
                        //$html.data.split(':')[1]
                        if($html.status==1)
                        {
                            $("#studyplay_current").width($html.data.split(':')[0]*settings.StarWidth);
                            $goldn = $html.data.split(':')[0];
                            $goldn = "<span class='gol_x'>"+$goldn.split('.')[0]+"</span><span class='gol_n'>."+$goldn.split('.')[1]+"</span>";
                            $(".Goldnum").html($goldn);
                            $("#golder").html($html.data.split(':')[1]);
                            $(".Goldtitle").html('<span class="artglod">'+$html.data.split(':')[0]+'</span><span class="arttxt">'+$html.info+'</span>');
                            $("#zgoldtxtbox").html(stv($html.data.split(':')[0]));
                        }
                        else
                        {
                            $(".Goldtitle").html('<span class="artglod">0</span><span class="arttxt">'+$html.info+'</span>');
                        }
                    }
                });
                //$("#studyplay_current").width(studyplay_count*settings.StarWidth/2);
                //回调函数
                if (typeof callback == 'function') {
                    callback(studyplay_count/2);
                    return;
                }
            });
	}
};


$.fn.ItemScroll=function(options,callback){
	var settings ={
		BoxObjID      :"",/*盒子ID*/
		ItemConID     :"",/*内容盒子ID*/
		ItemConItem   :"",/*内容项目元素*/
		ItemTabID     :"",/*按钮盒子ID*/
		ItemTabItem   :"",/*内容项目元素*/
		Timer         :3000,
		Optrue        :true,
		Rfunction     :function(){}
	};
	if(options){jQuery.extend(settings,options);};
	var sWidth = $(settings.BoxObjID).width();
	var len = $(settings.ItemConID).find(settings.ItemConItem).length;
	var index = 0;
	var picTimer;
	var showPics = function(index) {
		var nowLeft = -index*sWidth;
		$(settings.BoxObjID).find(settings.ItemConID).stop(true,false).animate({"left":nowLeft},300,function(){settings.Rfunction($(settings.BoxObjID).find(settings.ItemConID).find("li:eq("+index+")"));});
		$(settings.BoxObjID).find(settings.ItemTabID).find(settings.ItemTabItem).removeClass("current").eq(index).addClass("current");
		if(settings.Optrue)
		$(settings.BoxObjID).find(settings.ItemTabID).find(settings.ItemTabItem).stop(true,false).animate({"opacity":"0.5"},300).eq(index).stop(true,false).animate({"opacity":"1"},300);

	}
	$(settings.BoxObjID).find(settings.ItemTabID).find(settings.ItemTabItem).mouseenter(function() {
		index = $(settings.BoxObjID).find(settings.ItemTabID).find(settings.ItemTabItem).index(this);
		showPics(index);
	}).eq(0).trigger("mouseenter");
	if(settings.Optrue)
	{
		$(settings.BoxObjID).find('a.prev,a.next').hover(function(){
			$(this).stop().animate({opacity:0.6});
		},function() {
			$(this).stop().animate({opacity:0.2});
		});
	}
	// Prev
	$(settings.BoxObjID).find('a.prev').click(function() {
		index -= 1;
		if(index == -1) {index = len - 1;}
		showPics(index);
	});
	// Next
	$(settings.BoxObjID).find('a.next').click(function() {
		index += 1;
		if(index == len) {index = 0;}
		showPics(index);
	});
	$(settings.BoxObjID).find(settings.ItemConID).css("width",sWidth * (len));
	// mouse
	$(settings.BoxObjID).hover(function() {
		clearInterval(picTimer);
	},function() {
		picTimer = setInterval(function() {
			showPics(index);
			index++;
			if(index == len) {index = 0;}
		},settings.Timer);
	}).trigger("mouseleave");
};

$.fn.ItemScroll_h = function(options,callback){
	var settings = {
		BoxObjID      : "",/*盒子ID*/
		ItemConID     : "",/*内容盒子ID*/
		ItemConItem   : "",/*内容项目元素*/
		ItemTabID     : "",/*按钮盒子ID*/
		ItemTabItem   : "",/*内容项目元素*/
		Timer         : 3000,
		Optrue        : true,
		Rfunction     : function(){}
	};
	if(options){jQuery.extend(settings,options);};
	var sHeight = $(settings.BoxObjID).height();
	var len = $(settings.ItemConID).find(settings.ItemConItem).length;
	var index = 0;
	var picTimer;
	var showPics = function(index) {
		var nowTop = -index*sHeight;
		$(settings.BoxObjID).find(settings.ItemConID).stop(true,false).animate({"top":nowTop},300,function(){settings.Rfunction($(settings.BoxObjID).find(settings.ItemConID).find("li:eq("+index+")"));});
		$(settings.BoxObjID).find(settings.ItemTabID).find(settings.ItemTabItem).removeClass("current").eq(index).addClass("current");
		if(settings.Optrue)
		$(settings.BoxObjID).find(settings.ItemTabID).find(settings.ItemTabItem).stop(true,false).animate({"opacity":"0.5"},300).eq(index).stop(true,false).animate({"opacity":"1"},300);

	}
	$(settings.BoxObjID).find(settings.ItemTabID).find(settings.ItemTabItem).mouseenter(function() {
		index = $(settings.BoxObjID).find(settings.ItemTabID).find(settings.ItemTabItem).index(this);
		showPics(index);
	}).eq(0).trigger("mouseenter");

	if(settings.Optrue)
	{
		$(settings.BoxObjID).find('a.prev,a.next').hover(function(){
			$(this).stop().animate({opacity:0.6});
		},function() {
			$(this).stop().animate({opacity:0.2});
		});
	}
	// Prev
	$(settings.BoxObjID).find('a.prev').click(function() {
		index -= 1;
		if(index == -1) {index = len - 1;}
		showPics(index);
	});
	// Next
	$(settings.BoxObjID).find('a.next').click(function() {
		index += 1;
		if(index == len) {index = 0;}
		showPics(index);
	});
	$(settings.BoxObjID).find(settings.ItemConID).css("height",sHeight * (len));
	// mouse

	var stvtimer = function(){
		return window.setInterval(function() {
			showPics(index);
			index++;
			if(index == len) {index = 0;}
		},settings.Timer);
	}

	$(settings.BoxObjID).hover(function() {
		window.clearInterval(picTimer);
	},function() {
		picTimer = stvtimer();
	}).trigger("mouseleave");
};

$(document).ready(function(){
	//系统初始化
	FF.Home.Js();
	FF.Home.searchInput($("#wd"),$('#ffsearch'));
	FF.Home.Sc($("#fav"));

	//延时加载
	// FF.Lazyload.Show();
	if($("#bdhddown").length > 0)
	{
		FF.Bdhddown.Info('bdhddown');
	}
	//搜索联想)
	FF.Suggest.Show('wd',12,Root+'index.php?s=plus-search-vod',Root+'index.php?s=vod-search-wd-');
	//历史记录
	if($("#history").length > 0)
	{
		FF.History.List('history');
	}
	if($("#smallhistory").length > 0)
	{
		FF.History.SmallMenuHistoryList('smallhistory');;
	}

	//影视顶踩初始化
	FF.UpDown.Vod(Root+'vote/updown/'+Id);

	//新闻顶踩初始化
	FF.UpDown.News(Root+'vote/updown/'+Cid+'/'+Id);

	//评论初始化
	/*FF.Comment.Show(Root+"index.php?s=Cm-Show-sid-"+Sid+"-id-"+Id+"-p-1");
	<div class="box2 player_l">
		<h3><div><a href="{$vod_readurl}">我来说两句</a></div></h3>
		<div id="Comment" class="Comment">评论加载中...</div>
	</div>*/
	/*alert($("#yybox").height());*/
	if($("#yybox").length > 0)
	{
		if($("#yybox")[0].scrollHeight>25)
		{
			$("#yymoerbtn").show();
			$("#yybox").width(305);
			$("#yymoerbtn").click(function(e){
				if($("#yybox").height()>25)
				{
					$("#yybox").height(25);
					$("#movtxtbox").height(318);
				}
				else
				{
					var h = $("#yybox")[0].scrollHeight;
					$("#yybox").height(h);
					$("#movtxtbox").height(318+(h-25));

				}
				e.preventDefault();
			});
		}
	}

	if($("#gold").length > 0)
		$("#gold").studyplay_star({MaxStar:10,CurrentStar:0,Enabled:true,Ajaxurl:Root+'vote/gold/'+Cid+'/'+Id},function(value){});

	//积分初始化
	// FF.Gold.Default(Root+'vote/gold/'+Cid+'/'+Id);
});

//$.extend({
//     includePath: '',
//     include: function(file) {
//        var files = typeof file == "string" ? [file]:file;
//        for (var i = 0; i < files.length; i++) {
//            var name = files[i].replace(/^\s|\s$/g, "");
//            var att = name.split('.');
//            var ext = att[att.length - 1].toLowerCase();
//            var isCSS = ext == "css";
//            var tag = isCSS ? "link" : "script";
//            var attr = isCSS ? " type='text/css' rel='stylesheet' " : " language='javascript' type='text/javascript' ";
//            var link = (isCSS ? "href" : "src") + "='" + $.includePath + name + "'";
//            if ($(tag + "[" + link + "]").length == 0) document.write("<" + tag + attr + link + "></" + tag + ">");
//        }
//   }
//});

//使用方法
//$.includePath = 'http://hi.baidu.com/javascript/';
//$.include(['json2.js', 'jquery.tree.js', 'jquery.tree.css']);