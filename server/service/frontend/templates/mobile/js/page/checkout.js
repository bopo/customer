$(document).on("pageInit", function() {
	initPage();
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
	wxJSSDK.init();
});

function initPage() {
	var id = $.fn.getUrlParam('id');
	if($.fn.isNotBlank(id)) {
		$.ajax({
			type: 'get',
			url: '../servlet/RecordServlet',
			data: {
				action: 'getCheckOutDetail',
				id: id
			},
			dataType: 'json',
			contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
			success: function(data, status) {
				var form = document.getElementsByTagName('form')[0];
				$.fn.setFormValues(form, data);
				var salerList = document.getElementById("li_saler");
				var shouhuo = document.getElementById("li_person");
				var type = data.outtype;
				if(type == "分销") { //分销
					salerList.style.display = "";
					shouhuo.style.display = "none";
				} else {
					salerList.style.display = "none";
					shouhuo.style.display = "";
				}
				document.getElementById("outunit").innerHTML = data.unit;
				$('#delete_btn').show();
				if($.fn.isNotBlank(data.pictures)) {
					var imagelist = data.imagelist;
					var urls = imagelist.split('|');
					for(var j = 0; j < urls.length; j++) {
						if(urls[j] != "")
							wxJSSDK.wxImageList.push(urls[j]);
					}
					var tpl = document.getElementById('tpl_pictures').innerHTML;
					laytpl(tpl).render(data.pictures, function(render) {
						document.getElementById("out_imagelist").innerHTML = render;
					});
				}
			}
		});

	}
};

function saveInInfo() {
	var id = $.fn.getUrlParam('id');
	var source = $.fn.getUrlParam('source');
	if($.fn.isNotBlank(id)) {
		var form = document.getElementsByTagName('form')[0];
		if($.fn.validateForm(form)) {
			$.toast('请检查输入的数据');
			return false;
		}
		var num = parseInt(document.getElementById("outnumber").value);
		var kucun = parseInt(document.getElementById("kucun").value);
		if(num > kucun) {
			$.toast("商品库存不够");
			return false;
		}
		wxJSSDK.uploadImageWithCall("uploadfile/outimg", "0", function(data) {
			var values = $.fn.getFormValues(form);
			values.action = 'updateOutInfo';
			values.id = id;
			var oldPictures = wxJSSDK.wxImageList;
			var oldPictureStr = "";
			for(var j = 0; j < oldPictures.length; j++) {
				oldPictureStr = oldPictureStr + oldPictures[j] + "|";
			}
			values.picture = oldPictureStr + data.fileName;
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
						if(source === 'home') {
							document.location.href = 'homeGroup.html?type=' + $.fn.getUrlParam('type');
						} else {
							document.location.href = 'history.html';
						}
					}
				}
			});
		});
	} else {
		$.toast('id不存在');
	}
}

function computeMoney(domMoney, domNum, targetDom) {
	var money = document.getElementById(domMoney).value;
	var num = parseInt(document.getElementById(domNum).value);

	if(money != "" && num != "")
		var totalnum = money * num;
	document.getElementById(targetDom).value = totalnum.toFixed(2);
}

function deleteCheckOut() {
	var id = $.fn.getUrlParam('id');
	var source = $.fn.getUrlParam('source');
	if($.fn.isNotBlank(id)) {
		$.confirm('确定要删除吗？', function() {
			$.ajax({
				url: '../servlet/HistoryServlet',
				type: 'post',
				data: {
					action: 'deleteOutInfo',
					id: id
				},
				dataType: 'json',
				contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
				success: function(data, status) {
					if(data.success == 1) {
						if(source === 'home') {
							document.location.href = 'homeGroup.html?type=' + $.fn.getUrlParam('type');
						} else {
							document.location.href = 'history.html';
						}
					} else {
						$.toast(data.msg);
					}
				}
			});
		});
	}
}

// 保存商品信息
$(document).on("click", "#btn_updateInInfo", function() {
	saveInInfo();
});