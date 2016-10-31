// 初始化界面
$(document).on("pageInit", function() {
	initPage(10, 0);
	initPushDown();
	initpullDown();
});

var loading = false;
var total_Complete = 100;
var total_DQ = 100;
var total_Price = 100;
var total_Dealing = 100;
var total_App = 100;

function testInit(domId, orderId, preLoader) {
	$("#" + domId).scroller({
		type: 'js'
	});
	$.initInfiniteScroll("#" + domId);
	$(document).on('infinite', "#" + domId, function() {
		if(loading) return;
		loading = true;

		// 每次加载添加多少条目
		var itemsPerLoad = 10;
		// 最多可加载的条目

		//var tabId="tab4";
		setTimeout(function() {
			// 重置加载flag
			loading = false;
			$.showIndicator();
			var total = document.getElementById("totalnumber").value;
			var lastIndexStr = document.getElementById(orderId).value;
			if(lastIndexStr == "") {
				lastIndex = 0;
			} else
				lastIndex = parseInt(document.getElementById(orderId).value);
			//			if (tabId == "tab1")
			//				total = total_DQ;
			//			else if (tabId == "tab4")
			//				total = total_Complete;
			if(lastIndex >= total) {
				// 加载完毕，则注销无限加载事件，以防不必要的加载:$.detachInfiniteScroll($('.infinite-scroll').eq(tabIndex));多个无线滚动请自行根据自己代码逻辑判断注销时机
				// 删除加载提示符
				//$.detachInfiniteScroll($('#'+domId));
				$('#' + preLoader).hide();

				$.hideIndicator();
				$.toast("没有更多的数据了");
				return;
			}
			//addItems(itemsPerLoad, lastIndex, tabId);
			initPage(itemsPerLoad, lastIndex);
			// 更新最后加载的序号
			//lastIndex =  $('#order_complete').find('li').length;
			$.pullToRefreshDone('#' + domId);
		}, 1000);
	});
}

function initPushDown() {
	$.initPullToRefresh('#pull_history');
	$("#pull_history").scroller({
		type: 'js'
	});
	$(document).on('refresh', '#pull_history', function(e) {
		// 模拟2s的加载过程
		setTimeout(function() {
			initPage(10, 0);
			// 加载完毕需要重置
			$.toast('数据已刷新');
			$.pullToRefreshDone('#pull_history');
			$.initPullToRefresh('#pull_history');
		}, 1000);
	});

}

function initpullDown() {
	testInit("pull_history", "monthIndex", "preloader_1");
}

function initPage(number, lastIndex) {
	var type = $.fn.getUrlParam('type') || 'd';
	var title = '今天';
	if(type == 'w') {
		title = '本周';
	} else if(type == 'm') {
		title = '本月';
	} else if(type == 'y') {
		title = '本年';
	}
	$('#bar_title').html(title + '流水');
	$('#lbl_title').html(title);
	initList(type, number, lastIndex);
}

//获取列表数据
//type值分为天、周、月、年
function initList(type, number, lastIndex) {
	var userId = window.sessionStorage.getItem("userId");
	if(userId != null && typeof(userId) != 'undefined') {
		$.ajax({
			type: "POST",
			url: "../servlet/HistoryServlet",
			data: {
				action: "getHistoryByDate",
				userId: userId,
				type: type,
				number: number,
				lastIndex: lastIndex
			},
			contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
			dataType: 'json',
			scriptCharset: 'utf-8',
			success: function(data, textStatus) {
				/*data包含汇总数据和明细列表,格式如下：
				 *{
				 * profit:xxx,利润 
				 * outmoney:xxx, 出货总额
				 * inmoney:xxx, 进货总额
				 * list:[
				 * 	{
				 * 		daynumber: xxx, 日格式为01-31
				 * 		monthnumber: xxx, 月格式为1-12
				 * 		title: xxx, 商品名称
				 * 		number: xxx, 数量
				 * 		unit: xxx, 单位
				 * 		type: xxx, 类型-出货|进货
				 * 		money: xxx，单笔金额
				 * 	}
				 * ]
				 * }
				 **/
				data.type = type;
				renderPage(data, number, lastIndex);
			}
		});
	}
}
//渲染界面
function renderPage(data, number, lastIndex) {
	document.getElementById('lbl_monthprofit').innerHTML = '￥' + data.profit;
	document.getElementById('lbl_inmoney').innerHTML = '￥' + data.inmoney;
	document.getElementById('lbl_outmoney').innerHTML = '￥' + data.outmoney;
	var orderNum1 = data.list.length;
	var tpl = document.getElementById('tpl_grouplist').innerHTML;
	laytpl(tpl).render(data, function(render) {
		if(lastIndex == 0) {
			document.getElementById('group_list').innerHTML = render;
		} else {
			$('#group_list').append(render);
		}
	});
	if(orderNum1 < 10) {
		$('#preloader_1').hide();
	}
	$("#pull_history").scroller('refresh');
	$.hideIndicator();
	$.initPullToRefresh('#pull_history');
	document.getElementById("monthIndex").value = lastIndex + number;
	if(data.totalnumber) {
		document.getElementById("totalnumber").value = data.totalnumber;
	} else {
		document.getElementById("totalnumber").value = lastIndex;
	}
}