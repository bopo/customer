// 初始化界面
$(document).on("pageInit", ".page", function(e, pageId, $page) {
	var isTest = window.sessionStorage.getItem("istest") || 1;
	if(isTest - 0 == 0) {
		console.log('付费用户');
		var dealer = $('#report4Dealer'),
			profit = $('#report4Profit');
		profit.removeClass('dn-unlink');
		profit.attr('href', 'report4Profit.html');
		dealer.removeClass('dn-unlink');
		dealer.attr('href', 'report4Dealer.html');
	}
});

function forbidden() {
	$.toast('请先在【我的】进行会员充值');
}