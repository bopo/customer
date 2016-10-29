islogin=0;
syndomain='http://ajax.qire123.com';
function checkcookie(){
	if(document.cookie.indexOf('qr_u=')>0){
	islogin=1;
	return true;
	}
	return false;
}
checkcookie();

$(document).ready(function(){
			
	// his-tip-show
	$(".hisBox").hover(function(){
		$(this).find(".looked-box").show();
		$(this).find(".his-tip-show").hide();
	},function(){		
		$(this).find(".looked-box").hide();
		$(this).find(".his-tip-show").show();
	});
	
	$(".close-his").click(function(){
		$(".his-tip-show").show();
		$(".looked-box").hide();
	});
	
	// user-dropbox
	$(".user-dropbox").hover(function(){
		$(this).find(".user-combo").show();
		$(this).find(".user-panel").addClass("user-panel-active");
	},function(){		
		$(this).find(".user-combo").hide();
		$(this).find(".user-panel").removeClass("user-panel-active");
	});
	
	// show-tipinfo
	$(".show-tipinfo a").hover(function(){
		$(this).parent().parent().find(".tipInfo").show();
	},function(){		
		$(this).parent().parent().find(".tipInfo").hide();
	});	
	
	$("#wish").trigger('click');
	
	// Input Text Focus
	$(".ui-input").focus(function(){
		$(this).parent().addClass("ui-form-field-active");
	}).hover(function(){
		$(this).parent().addClass("ui-form-field-hover");
	},function(){
		$(this).parent().removeClass("ui-form-field-hover");
	});
	$(".ui-input").blur(function(){
		$(this).parent().removeClass("ui-form-field-active");
	});	
	
	// timeinfo
	$(".timeinfo").hover(function(){
		$(this).addClass("timeinfo-active");
	},function(){
		$(this).removeClass("timeinfo-active");
	});	
	
	// Date List Jquery
	$(".date-list").each(function(){
		$lis = $(this).find("li:last").index();		
		if($lis > 5){
			$(this).addClass("date-long");
		}	
	});
	
	
});

// Tab Menu JS Common
function setTab(name,cursel,n){
	for(i=1;i<=n;i++){
		var menu=document.getElementById(name+i);
		var con=document.getElementById("con_"+name+"_"+i);
		menu.className=i==cursel?"active":"";
		con.style.display=i==cursel?"block":"none";
	}
}
function qrsearch(){
	if($("#kw").val()=='请在此处输入影片片名或演员名称。'||$("#kw").val()==''){
		$("#kw").val('');
		$("#kw").focus();
		return false;
	}
}

//直接调用人气数据
function getVideoHit(vid){	
	$.post("/"+sitePath+"inc/ajax.asp?action=hit&id="+vid,function (obj){														
			var result=obj;
			if(result=="err"){
				set(document.getElementById("hit"),'发生错误');}
			else{				
				set(document.getElementById("hit"),result);}
		}
	);				
}
function set(viewid,v){viewid.innerHTML=v;}

function getNewsHit(nid){	
	$.post("/"+sitePath+"inc/ajax.asp?action=hitnews&id="+nid,function (obj){														
			var result=obj;
			if(result=="err"){
				set(document.getElementById("hit"),'发生错误');}
			else{				
				set(document.getElementById("hit"),result);}
		}
	);				
}
function set(viewid,n){viewid.innerHTML=n;}