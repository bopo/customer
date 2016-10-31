// 初始化界面
$(document).on("pageInit", function() {
	initUnit();
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
});

function deleteGoods() {
	var id = $.fn.getUrlParam('id');
	if($.fn.isNotBlank(id)) {
		$.confirm('确定要删除吗？', function() {
			$.ajax({
				url: '../servlet/ProductMngServlet',
				type: 'post',
				data: {
					action: 'deleteProduct',
					id: id
				},
				dataType: 'json',
				contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
				success: function(data, status) {
					if(data.success == 1) {
						window.location.href = "goodsList.html";
						var temp = parseInt(window.sessionStorage.getItem("productnum"));
						temp = temp - 1;
						window.sessionStorage.setItem("productnum", temp);
					} else
						$.toast(data.msg);
				}
			});
		});
	}
}

function initUnit() {
	$.ajax({
		type: 'get',
		url: '../servlet/ProductMngServlet',
		data: {
			action: 'initUnit'
		},
		success: function(data, textStatus) {
			var obj = $.parseJSON(data);
			var tpl = document.getElementById('tpl_unit').innerHTML;
			laytpl(tpl).render(obj, function(render) {
				$('#unit').html(render);
				initDetailPage();
			});
		}
	});
}

function initDetailPage() {
	var id = $.fn.getUrlParam('id');
	if($.fn.isNotBlank(id)) {
		initEditPage(id);
	} else {
		initAddPage();
	}
}

function initEditPage(id) {
	var userId = window.sessionStorage.getItem("userId");
	if($.fn.isNotBlank(userId)) {
		$.ajax({
			type: 'get',
			url: '../servlet/ProductMngServlet',
			data: {
				action: 'getProductInfo',
				id: id,
				userId: userId
			},
			dataType: 'json',
			contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
			success: function(data, status) {
				var form = document.getElementsByTagName('form')[0];
				$.fn.setFormValues(form, data);
				$('.pull-right').show();
				if($.fn.isNotBlank(data.picture)) {
					var tpl = document.getElementById('tpl_image').innerHTML;
					laytpl(tpl).render(data, function(render) {
						document.getElementById("imageList").innerHTML = render;
					});
					wxJSSDK.wxImageList.push(data.picture);
				}
			}
		});
	}
}

function initAddPage() {
	$('.pull-right').hide();
}

function saveInfo() {
	var form = document.getElementsByTagName('form')[0];
	var values = $.fn.getFormValues(form);
	if($.fn.validateForm(form)) {
		$.toast('请检查输入的数据');
		return false;
	}
	//新增产品必须要有选择一张图片
	if($.fn.isBlank(values.id) && $('#imageList li').length == 0) {
		$.toast('请选择一张产品图片');
		return false;
	}
	values.userId = window.sessionStorage.getItem("userId");
	values.action = $.fn.isBlank(values.id) ? 'addProduct' : 'updateProduct';
	wxJSSDK.uploadImageWithCall("uploadfile/productimg", "1", function(data) {
		values.picture = data.fileName;
		console.log(values.picture);
		$.ajax({
			type: 'POST',
			url: '../servlet/ProductMngServlet',
			contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
			data: values,
			success: function(data, textStatus) {
				var obj = $.parseJSON(data);
				if(obj.success == 0) {
					$.toast(obj.msg);
				} else {
					window.location.href = "goodsList.html";
					if(values.action == "addProduct") {
						var temp = parseInt(window.sessionStorage.getItem("productnum"));
						temp = temp + 1;
						window.sessionStorage.setItem("productnum", temp);
					}
				}
			}
		});
	});
}
// 保存商品信息
$(document).on("click", "#saveGoods", function() {
	saveInfo();
});