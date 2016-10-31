var loading = false;
//初始化界面
$(document).on("pageInit", '.page', function() {
	initHistoryList(1, 0);
	initPushDown();
	initpullDown();
});

function initpullDown() {
	testInit("pull_history", "monthIndex", "preloader_1");
}

function initPushDown() {
	//$.initPullToRefresh('#pull_history');
	$("#pull_history").scroller({
		type: 'js'
	});
	$(document).on('refresh', '#pull_history', function(e) {
		// 模拟2s的加载过程
		setTimeout(function() {
			initHistoryList(1, 0);
			// 加载完毕需要重置
			$.toast('数据已刷新');
			$.pullToRefreshDone('#pull_history');
			$.initPullToRefresh('#pull_history');
		}, 1000);
	});
}

function testInit(domId, orderId, preLoader) {
	$("#" + domId).scroller({
		type: 'js'
	});
	$.initInfiniteScroll("#" + domId);
	$(document).on('infinite', "#" + domId, function() {
		if(loading) return;
		loading = true;
		// 每次加载添加多少条目
		var itemsPerLoad = 1;
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
			} else {
				lastIndex = parseInt(document.getElementById(orderId).value);
			}
			//if (tabId == "tab1")
			//	total = total_DQ;
			//else if (tabId == "tab4")
			//	total = total_Complete;
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
			initHistoryList(itemsPerLoad, lastIndex);
			// 更新最后加载的序号
			//lastIndex =  $('#order_complete').find('li').length;
			$.pullToRefreshDone('#' + domId);
		}, 1000);
	});
}

function initHistoryList(number, lastIndex) {
	var userId = window.sessionStorage.getItem("userId");
	if(userId != null && typeof(userId) != "undefined") {
		$.ajax({
			url: '../servlet/HistoryServlet',
			type: 'get',
			dataType: 'json',
			data: {
				action: 'getHistoryList',
				userId: userId,
				number: number,
				lastIndex: lastIndex
			},
			contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
			success: function(data, status) {
				var tpl = document.getElementById('tpl_history').innerHTML;
				laytpl(tpl).render(data, function(render) {
					if(lastIndex == 0) {
						document.getElementById('history_list').innerHTML = render;
					} else {
						$('#history_list').append(render);
					}
					//document.getElementById("history_list").innerHTML=render;
				});
				$("#pull_history").scroller('refresh');
				$.hideIndicator();
				$.initPullToRefresh('#pull_history');
				if(data.length > 0) {
					document.getElementById("monthIndex").value = data[0].number;
					if(data.length > 0) {
						document.getElementById("totalnumber").value = data[0].totalnumber;
					} else {
						document.getElementById("totalnumber").value = lastIndex;
					}
					//$('#preloader_1').hide();
					//if (tabId == "tab1")
					//	total = total_DQ;
					//else if (tabId == "tab4")
					//	total = total_Complete;
					if(data[0].number >= data[0].totalnumber) {
						// 加载完毕，则注销无限加载事件，以防不必要的加载:$.detachInfiniteScroll($('.infinite-scroll').eq(tabIndex));多个无线滚动请自行根据自己代码逻辑判断注销时机
						// 删除加载提示符
						//$.detachInfiniteScroll($('#'+domId));
						$('#preloader_1').hide();
						$.hideIndicator();
						//$.toast("没有更多的数据了");
					}
				} else {
					var tpl2 = document.getElementById('tpl_nodata').innerHTML;
					laytpl(tpl2).render(buildNormalData(), function(render) {
						$('#history_list').append(render);
					});
					$('#preloader_1').hide();
					$.hideIndicator();
				}
			},
			failure: function(response) {
				var tpl2 = document.getElementById('tpl_nodata').innerHTML;
				laytpl(tpl2).render(buildNormalData(), function(render) {
					$('#history_list').append(render);
				});
				$('#preloader_1').hide();
				$.hideIndicator();
				$.toast("加载数据失败");
			}
		});
	}
}

function buildNormalData() {
	var now = new Date();
	var y = now.getFullYear();
	var m = now.getMonth() + 1;
	var data = [];
	for(var i = m; i > 0; i--) {
		data.push({
			year: y,
			month: i
		});
	}
	return data;
}