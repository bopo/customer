var id = "";
// 初始化列表界面
$(document).on("pageInit", "#page_dealer", function(e, pageId, $page) {
	initDealerList();
});
// 初始化详情界面
$(document).on("pageInit", "#page_dealerdetail", function(e, pageId, $page) {
	initDetailPage();
});

function initDealerList() {
	var userId = window.sessionStorage.getItem("userId");
	if(userId != null && typeof(userId) != "undefined") {
		$.ajax({
			type: 'get',
			url: '../servlet/DealerServlet',
			data: {
				action: 'initDealerList',
				userId: userId
			},
			dataType: 'json',
			contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
			success: function(data, status) {
				var tpl = document.getElementById('tpl_dealerlist').innerHTML;
				laytpl(tpl).render(data, function(render) {
					document.getElementById("dom_dealerlist").innerHTML = render;
				});
			}

		});
	}

}

function saveInfo() {
	var id = $.fn.getUrlParam('id');
	if(id == null || id == "") {
		saveAddInfo();
	} else {
		saveEditInfo(id);
	}

}

function saveEditInfo(salerId) {
	var userId = window.sessionStorage.getItem("userId");
	var userName = document.getElementById("inp_username").value;
	var selects = $("select");
	var data = "";
	for(var i = 0; i < selects.length; i++) {
		var value = $(selects[i]).val();
		if(value != "") {
			var id = $(selects[i]).attr("id").substring(4);
			// var id=selects[i].attr("id").substring(4);
			data = data + id + "," + value + "|";
		}
	}
	if($.fn.isBlank(data)) {
		$.toast('至少设置一款产品的代理级别');
		return false;
	}
	$.ajax({
		url: '../servlet/DealerServlet',
		type: 'post',
		data: {
			action: 'saveEditInfo',
			userId: userId,
			params: data,
			salerId: salerId,
			userName: userName
		},
		dataType: 'json',
		contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
		success: function(data, status) {
			if(data.success == 1)
				window.location.href = "dealerList.html";
			else
				$.toast(data.msg);
		}

	});
}

function saveAddInfo() {
	var userId = window.sessionStorage.getItem("userId");
	var userName = document.getElementById("inp_username").value;
	var selects = $("select");
	var data = "";
	for(var i = 0; i < selects.length; i++) {
		var value = $(selects[i]).val();
		if(value != "") {
			var id = $(selects[i]).attr("id").substring(4);
			// var id=selects[i].attr("id").substring(4);
			data = data + id + "," + value + "|";
		}
	}
	if($.fn.isBlank(data)) {
		$.toast('至少设置一款产品的代理级别');
		return false;
	}
	$.ajax({
		url: '../servlet/DealerServlet',
		type: 'post',
		data: {
			action: 'saveAddInfo',
			userId: userId,
			params: data,
			userName: userName
		},
		dataType: 'json',
		contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
		success: function(data, status) {
			if(data.success == 1) {
				window.location.href = "dealerList.html";
				var temp = parseInt(window.sessionStorage.getItem("salernum"));
				temp = temp + 1;
				window.sessionStorage.setItem("salernum", temp);
			} else{
				$.toast(data.msg);
			}
		}
	});
}

function deleteDealer() {
	var id = $.fn.getUrlParam('id');
	if(id == null || id == "") {
		$.toast("新增不能删除");
	} else {
		$.confirm('确定要删除吗？', function() {
			$.ajax({
				url: '../servlet/DealerServlet',
				type: 'post',
				data: {
					action: 'deleteDealer',
					id: id
				},
				dataType: 'json',
				contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
				success: function(data, status) {
					if(data.success == 1) {
						window.location.href = "dealerList.html";
						var temp = parseInt(window.sessionStorage.getItem("salernum"));
						temp = temp - 1;
						window.sessionStorage.setItem("salernum", temp);
					} else
						$.toast(data.msg);
				}

			});
		})
	}
}

function initDetailPage() {
	id = $.fn.getUrlParam('id');
	var dealerName = $.fn.getUrlParam('dealerName');
	if($.fn.isNotBlank(id)) {
		initEditPage(id, dealerName);
	} else {
		initAddPage();
	}
}

function initEditPage(salerId, salerName) {
	document.getElementById("inp_username").value = decodeURI(salerName);
	var userId = window.sessionStorage.getItem("userId");
	if(userId != null && typeof(userId) != "undefined") {
		$.ajax({
			type: 'get',
			url: '../servlet/DealerServlet',
			data: {
				action: 'initEditPage',
				salerId: salerId,
				salerName: salerName,
				userId: userId
			},
			dataType: 'json',
			contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
			success: function(data, status) {
				var tpl = document.getElementById('tpl_dealerdetail').innerHTML;
				laytpl(tpl).render(data, function(render) {
					document.getElementById("dom_dealerdetail").innerHTML = render;
					$('.pull-right').show();
				});
			}

		});
	}
}

function initAddPage() {
	$('.pull-right').hide();
	var userId = window.sessionStorage.getItem("userId");
	if(userId != null && typeof(userId) != "undefined") {
		$.ajax({
			type: 'get',
			url: '../servlet/DealerServlet',
			data: {
				action: 'initAddPage',
				userId: userId
			},
			dataType: 'json',
			contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
			success: function(data, status) {
				var tpl = document.getElementById('tpl_dealerdetail').innerHTML;
				laytpl(tpl).render(data, function(render) {
					document.getElementById("dom_dealerdetail").innerHTML = render;
				});
			}
		});
	}
}