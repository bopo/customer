var id = "";
// 初始化列表界面
$(document).on("pageInit", "#page_help", function(e, pageId, $page) {
	console.log('on help list page init');
	initHelpList();
});
// 初始化详情界面
$(document).on("pageInit", "#page_helpdetail", function(e, pageId, $page) {
	console.log('on help detail page init');
	var id = $.fn.getUrlParam('id');
	initHelpDetail(id);
});

function initHelpList() {
	$.ajax({
		type: 'get',
		url: '../servlet/HelpServlet',
		data: {
			action: 'initHelpList'
		},
		dataType: 'json',
		contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
		success: function(data, status) {
			var tpl = document.getElementById('tpl_helplist').innerHTML;
			laytpl(tpl).render(data, function(render) {
				document.getElementById("help_list").innerHTML = render;
			});
		}
	});
}

function initHelpDetail(id) {
	$.ajax({
		type: 'get',
		url: '../servlet/HelpServlet',
		data: {
			action: 'initHelpDetail',
			id: id
		},
		dataType: 'json',
		contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
		success: function(data, status) {
			if(data.success==1)
			{
				
			document.getElementById("help_title").innerHTML=data.title;	
			var tpl = document.getElementById('tpl_helpdetail').innerHTML;
			laytpl(tpl).render(data, function(render) {
				document.getElementById("help_detail").innerHTML = render;
			});
			}
			else
			{
			  $.toast(data.msg);
			}
		}
	});
}