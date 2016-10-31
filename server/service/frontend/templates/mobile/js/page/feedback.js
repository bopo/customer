$(document).on("pageInit", function() {
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

$(document).on('click', '.button-success', function() {
	saveFeedback();
});

function saveFeedback() {
	var form = document.getElementsByTagName('form')[0];
	if($.fn.validateForm(form)) {
		$.toast('请检查输入的数据');
		return false;
	}
	//TODO 最多三张图片
	wxJSSDK.uploadImageWithCall("uploadfile/feedbackimg", "0", function(data) {
		var values = $.fn.getFormValues(form);
		values.userId = window.sessionStorage.getItem("userId");
		values.action = 'saveFeedback';
//		var oldPictures = wxJSSDK.wxImageList;
//		var oldPictureStr = "";
//		for(var j = 0; j < oldPictures.length; j++) {
//			oldPictureStr = oldPictureStr + oldPictures[j] + "|";
//		}
		values.picture = data.fileName;
		$.ajax({
			type: 'POST',
			url: '../servlet/FeedbackServlet',
			contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
			data: values,
			success: function(data, textStatus) {
				var obj = $.parseJSON(data);
				if(obj.success == 0) {
					$.toast(obj.msg);
				} else {
					$.toast('提交成功');
					setTimeout(function() {
						document.location.href = 'me.html';
					}, 2000);
				}
			},
			error: function(xhr, type) {
				$.toast('提交失败，错误代码: ' + xhr.status);
			}
		});
	});
}