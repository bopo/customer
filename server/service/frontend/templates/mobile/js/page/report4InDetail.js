// 初始化界面
$(document).on("pageInit", ".page", function(e, pageId, $page) {
	initPage();
});

function initPage() {
	var userId = window.sessionStorage.getItem("userId");
	var productId = $.fn.getUrlParam('id');
	var startDate = $.fn.getUrlParam('sd');
	var endDate = $.fn.getUrlParam('ed');
	$.ajax({
		url: '../servlet/ReportServlet',
		dataType: 'json',
		type: 'get',
		data: {
			action: 'report4InDetail',
			userId: userId,
			productId: productId,
			startDate: startDate,
			endDate: endDate
		},
		contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
		success: function(data, status) {
			if(data.success == 1) {
				$('nav h1.title').text(data.name + '进货明细');
				renderPage(data.list);
			} else {
				$.toast(data.msg);
			}
		}
	});
}

function renderPage(data) {
	var tpl = document.getElementById('tpl_report4InDetail').innerHTML;
	laytpl(tpl).render(data, function(render) {
		$('#report_in_detail').html(render);
	});
}