function initPage() {
	// if(!wxJSSDK.isWeiXin()) {
	// 	window.location.href = "errorWX.html";
	// 	return;
	// }
	// userLogin();
	var userId = window.sessionStorage.getItem("userId");
	if(userId != null && typeof(userId) != 'undefined') {
		$.ajax({
			type: "get",
			url: "../servlet/IndexServlet",
			data: {
				action: "initPage",
				userId: userId
			},
			success: function(data, textStatus) {
				var obj = eval('(' + data + ')');
				if(obj.success == 0) {
					alert(obj.msg);
				} else {
					document.getElementById("lbl_currentMonth").innerHTML = obj.month;
					document.getElementById("lbl_currentYear").innerHTML = obj.year;
					document.getElementById("lbl_monthprofit").innerHTML = '¥' + obj.monthprofit;
					document.getElementById("lbl_dayprofit").innerHTML = '¥' + obj.dayprofit;
					document.getElementById("lbl_inmoney").innerHTML = '¥' + obj.inmoney;
					document.getElementById("lbl_outmoney").innerHTML = '¥' + obj.outmoney;
					document.getElementById("lbl_weekprofit").innerHTML = '¥' + obj.weekprofit;
					document.getElementById("lbl_yearprofit").innerHTML = '¥' + obj.yearprofit;
					document.getElementById("lbl_monthprofit2").innerHTML = '¥' + obj.monthprofit;
				}
				//alert(data);
			}
		});
	}
}

function userLogin() {
	var openId = window.sessionStorage.getItem("openId");
	var userId = window.sessionStorage.getItem("userId");
	if(openId == null || typeof(openId) == "undefined" || typeof(userId) == "undefined") {
		//if(true){
		openId = "oalKBwdYPH3pXvr4PC_4qs42EPJ0";
		$.ajax({
			url: '../servlet/IndexServlet',
			type: 'get',
			data: {
				action: 'getUserInfo',
				openId: openId
			},
			dataType: 'json',
			success: function(data, textStatus) {
				if(data != "") {
					var obj = data;
					window.sessionStorage.setItem('userId', obj.userId);

					window.sessionStorage.setItem('staffid', obj.staffid);

					window.sessionStorage.setItem('name', obj.name);

					window.sessionStorage.setItem('password', obj.password);

					window.sessionStorage.setItem('picture', obj.picture);

					window.sessionStorage.setItem('telnum', obj.telnum);

					window.sessionStorage.setItem('limitdate', obj.limitdate);

					window.sessionStorage.setItem('daynum', obj.daynum);

					window.sessionStorage.setItem('istest', obj.istest);

					window.sessionStorage.setItem('isinit', obj.isinit);

					window.sessionStorage.setItem('sex', obj.sex);

					window.sessionStorage.setItem('productnum', obj.productnum);

					window.sessionStorage.setItem('salernum', obj.salernum);

					window.sessionStorage.setItem('levelnum', obj.levelnum);

					window.sessionStorage.setItem('isLogin', 1);
					window.sessionStorage.setItem('openId', openId);

				} else {
					$.toast("该用户不存在");
				}
			}
		});
	}
}