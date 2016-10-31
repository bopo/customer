// 初始化界面
$(document).on("pageInit", ".page", function(e, pageId, $page) {
	var userName = window.sessionStorage.getItem("name");
	var userHeaderImg = window.sessionStorage.getItem("picture");
	var userTelphone = window.sessionStorage.getItem("telnum");
	var limitdate = window.sessionStorage.getItem("limitdate");
	var productNum=window.sessionStorage.getItem("productnum");
	var salernum=window.sessionStorage.getItem("salernum");
	var levelnum=window.sessionStorage.getItem("levelnum");
	if($.fn.isNotBlank(userName)) {
		$("#lbl_nickname").html(userName);
	}
	if($.fn.isNotBlank(userHeaderImg)) {
		$("#img_headerImg").attr("src", userHeaderImg);
	}
	if($.fn.isNotBlank(productNum)) {
		$("#lbl_goods").html(productNum);
	}
	if($.fn.isNotBlank(salernum)) {
		$("#lbl_dealer").html(salernum);
	}
	if($.fn.isNotBlank(levelnum)) {
		$("#lbl_level").html(levelnum);
	}
	if($.fn.isNotBlank(userTelphone)) {
		$("#lbl_telphone").html(userTelphone);
	}
	$("#lbl_limitdate").html(limitdate);
	//initData();
});
//获取商品、代理、等级数据
function initData() {
	$.ajax({
		type: "get",
		url: "",
		data: {
			action: ""
		},
		success: function(data, textStatus) {
			var obj = $.parseJSON(data);
			$("#lbl_goods").html(obj.productNum);
			$("#lbl_dealer").html(obj.dealerNum);
			$("#lbl_level").html(obj.dealerNum);
		}
	});
}