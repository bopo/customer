// 初始化界面
$(document).on("pageInit", ".page", function(e, pageId, $page) {
	var userName = window.sessionStorage.getItem("name");
	var userHeaderImg = window.sessionStorage.getItem("picture");
	var userTelphone = window.sessionStorage.getItem("telnum");
	var userSex = window.sessionStorage.getItem("sex");
	if($.fn.isBlank(userTelphone)) {
		userTelphone = '';
	}
	if($.fn.isBlank(userSex)) {
		userSex = "004003";
	}
	var values = {
		userName: userName,
		userTelphone: userTelphone,
		userSex: userSex
	};
	var form = document.getElementsByTagName('form')[0];
	$.fn.setFormValues(form, values);
	if($.fn.isNotBlank(userHeaderImg)) {
		$("#userInfo_img").attr("src", userHeaderImg);
	}
});
// 保存基本信息
$(document).on("click", "#saveUserInfo", function() {
	var form = document.getElementsByTagName('form')[0];
	if($.fn.validateForm(form)) {
		$.toast('请检查输入的数据');
		return false;
	}
	var values = $.fn.getFormValues(form);
	values.userId = window.sessionStorage.getItem("userId");
	values.action = 'saveUserInfo';
	$.ajax({
		type: 'POST',
		url: '../servlet/UserServlet',
		contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
		data: values,
		success: function(data, textStatus) {
			var obj = $.parseJSON(data);
			if(obj.success == 0) {
				$.toast(obj.msg);
			} else {
				$.toast("保存成功");
				window.sessionStorage.setItem("name", values.userName);
				window.sessionStorage.setItem("telnum", values.userTelphone);
				window.sessionStorage.setItem("sex", values.userSex);
			}
		}
	});
});