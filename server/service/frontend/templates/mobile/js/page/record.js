/**
 * 初始化出货页面
 */
$(document).on("pageInit", '#out_record', function(e, pageId, $page) {
	if(wxJSSDK.config.debug) {
		console.log('on ' + pageId + ' page init');
	}
	initOutType();
	//initOutGoodsList();
});

/**
 * 初始化进货页面
 */
$(document).on("pageInit", '#in_record', function(e, pageId, $page) {
	if(wxJSSDK.config.debug) {
		console.log('on ' + pageId + ' page init');
	}
	initInGoodsList();
});

/**
 * 当选择分销时，系统显示代理商列表，隐藏收货人
 * 当选择零售时，系统显示收货人，隐藏代理商列表
 */
function displaySalerList() {
	var type = document.getElementById("out_type").value;
	var salerList = document.getElementById("li_daili");
	var shouhuo = document.getElementById("li_shouhuo");
	if(type == "010002") { //分销

		salerList.style.display = "";
		shouhuo.style.display = "none";
		document.getElementById("inp_outperson").removeAttribute("required");
		document.getElementById("daili_list").setAttribute("required", "required");
	} else {
		salerList.style.display = "none";
		shouhuo.style.display = "";
		document.getElementById("inp_outperson").setAttribute("required", "required");
		document.getElementById("daili_list").removeAttribute("required");
	}
}

/**
 * 保存进货信息
 */
function saveInInfo() {
	var form = document.getElementsByTagName('form')[1];
	if($.fn.validateForm(form)) {
		$.toast('请检查输入的数据');
		return false;
	}
	wxJSSDK.uploadImageWithCall("uploadfile/inimg", "0", function(data) {
		var values = $.fn.getFormValues(form);
		values.userId = window.sessionStorage.getItem("userId");
		values.action = 'saveInInfo';
		values.picture = data.fileName;
		//alert(values.picture);
		$.ajax({
			type: 'POST',
			url: '../servlet/RecordServlet',
			contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
			data: values,
			success: function(data, textStatus) {
				var obj = $.parseJSON(data);
				if(obj.success == 0) {
					$.toast(obj.msg);
				} else {
					document.location.href = 'home.html';
				}
			}
		});
	});
}

/**
 * 初始化进货产品列表
 */
function initInGoodsList() {
	var userId = window.sessionStorage.getItem("userId");
	if(userId != null && typeof(userId) != 'undefined') {
		$.ajax({
			type: 'get',
			url: '../servlet/RecordServlet',
			data: {
				action: 'initGoodsList',
				userId: userId
			},
			dataType: 'json',
			contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
			success: function(data, textStatus) {
				var tpl = document.getElementById('tpl_goodslist').innerHTML;
				laytpl(tpl).render(data, function(render) {
					document.getElementById("product_list_2").innerHTML = render;

				});
			}
		});
	}
}

/**
 * 初始化微信接口
 */
function initWeiXin() {
	wxJSSDK.config.jsApiList = ['chooseImage',
		'openLocation',
		'scanQRCode',
		'uploadImage', 'startRecord',
		'stopRecord',
		'onVoiceRecordEnd',
		'playVoice',
		'pauseVoice',
		'stopVoice',
		'onVoicePlayEnd', 'uploadVoice', 'previewImage', 'getLocation'
	];
	//wxJSSDK.Del(Cookie);
	wxJSSDK.init();

}
/**
 * 初始化出货方式
 */
function initOutType() {
	$.ajax({
		type: 'get',
		url: '../servlet/RecordServlet',
		data: {
			action: 'initOutType'
		},
		dataType: 'json',
		contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
		success: function(data, textStatus) {
			var tpl = document.getElementById('tpl_outtype').innerHTML;
			laytpl(tpl).render(data, function(render) {
				document.getElementById("out_type").innerHTML = render;
			});
			initOutGoodsList();
		}
	});

};

/*
 * 计算合计价格
 */
function computeMoney(domMoney, domNum, targetDom) {
	var money = document.getElementById(domMoney).value;
	var num = document.getElementById(domNum).value;
	if(money != "" && num != "")
		var totalnum = money * num;
	document.getElementById(targetDom).value = totalnum.toFixed(2);
}

/**
 * 当选择某个商品时设置单位和价格以及代理商
 * @param {} domId
 * @param {} targetDomId
 * @param {} targetDomId2
 */
function setUnit(domId, targetDomId, targetDomId2, priceType) {
	var dom = document.getElementById(domId);
	var index = dom.selectedIndex;
	var unit = dom.options[index].getAttribute("unit");
	var outprice = dom.options[index].getAttribute(priceType);
	var kucun = dom.options[index].getAttribute("kucun");
	document.getElementById("hidden_kucun").value = kucun;
	document.getElementById(targetDomId).innerHTML = unit;
	document.getElementById(targetDomId2).value = outprice;
	var goodsId = dom.value;

	var userId = window.sessionStorage.getItem("userId");
	$.ajax({
		url: '../servlet/RecordServlet',
		contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
		type: 'get',
		data: {
			action: 'getSalerList',
			userId: userId,
			goodsId: goodsId
		},
		dataType: 'json',
		success: function(data, status) {
			var tpl = document.getElementById('tpl_daili').innerHTML;
			laytpl(tpl).render(data, function(render) {
				document.getElementById("daili_list").innerHTML = render;
			});
		}
	});
}

/**
 * 保存出货记录
 * @return {Boolean}
 */
function saveOutInfo() {
	var form = document.getElementsByTagName('form')[0];
	if($.fn.validateForm(form)) {
		$.toast('请检查输入的数据');
		return false;
	}
	var outnumber = parseInt(document.getElementById("inp_number").value);
	var kucun = parseInt(document.getElementById("hidden_kucun").value);

	if(outnumber > kucun) {
		$.toast('出货量不能大于库存量');
		return false;
	}
	var values = $.fn.getFormValues(form);
	values.userId = window.sessionStorage.getItem("userId");
	values.action = 'saveOutInfo';

	wxJSSDK.uploadImageWithCall("uploadfile/outimg", "0", function(data) {
		values.picture = data.fileName;
		doSaveOutInfo(values);
	});
	//	if(wxJSSDK.wxImageList.length > 0) {
	//		wxJSSDK.uploadImageWithCall("uploadfile/outimg", "0", function(data) {
	//			values.picture = data.fileName;
	//			doSaveOutInfo(values);
	//		});
	//	} else {
	//		doSaveOutInfo(values);
	//	}
}

function doSaveOutInfo(values) {
	$.ajax({
		type: 'POST',
		url: '../servlet/RecordServlet',
		contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
		data: values,
		success: function(data, textStatus) {
			var obj = $.parseJSON(data);
			if(obj.success == 0) {
				$.toast(obj.msg);
			} else {
				document.location.href = 'home.html';
			}
		}
	});
}

/**
 * 初始化出货商品列表
 */
function initOutGoodsList() {
	var userId = window.sessionStorage.getItem("userId");
	if(userId != null && typeof(userId) != 'undefined') {
		$.ajax({
			type: 'get',
			url: '../servlet/RecordServlet',
			data: {
				action: 'initGoodsList',
				userId: userId
			},
			dataType: 'json',
			contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
			success: function(data, textStatus) {
				var tpl = document.getElementById('tpl_goodslist').innerHTML;
				laytpl(tpl).render(data, function(render) {
					document.getElementById("product_list_1").innerHTML = render;
				});
				initWeiXin();
			}
		});
	}
}