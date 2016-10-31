

function pay() {

	var obj=document.getElementById("pay_type");
	var index = obj.selectedIndex; 
	var text = obj.options[index].text; // 选中文本
    var value = obj.options[index].value; // 选中值
	var money = parseInt(value * 100);
	document.getElementById("moneyType").value=value;
	document.getElementById("payMoney").value = money;
	
	document.getElementById("orderTitle").value ="微商记账助手充值套餐【"+text+"】";
	//alert(money);
	//var openid = window.sessionStorage.getItem("openId");
	//var openid ="oY-sIs7a06KbI_6KdhqVTpd9bC5k";

	if (typeof WeixinJSBridge == "undefined") {
		if (document.addEventListener) {
			document.addEventListener('WeixinJSBridgeReady', jsApiCall, false);
		} else if (document.attachEvent) {
			document.attachEvent('WeixinJSBridgeReady', jsApiCall);
			document.attachEvent('onWeixinJSBridgeReady', jsApiCall);
		}
	} else {
		jsApiCall();
	}

};

function GetRequest() 
{
				var url = location.search; //获取url中"?"符后的字串   
				url = unescape(url);

				var theRequest = new Object();
				if(url.indexOf("?") != -1) {
					var str = url.substr(1);
					var strs = str.split("&");
					for(var i = 0; i < strs.length; i++) {
						theRequest[strs[i].split("=")[0]] = strs[i].split("=")[1];
					}
				}
				return theRequest;
			}

function initPage()
{
	 var request=GetRequest();
	 if(request['openId'])
	 {
	   window.sessionStorage.setItem("limitdate",request['limitdate']);
	   window.sessionStorage.setItem("openId",request['openId']);
	   window.sessionStorage.setItem("isTemplate",1);
	 }
	 else
	 {
	    window.sessionStorage.setItem("isTemplate",0);
	 }
	 var limitdate=window.sessionStorage.getItem("limitdate");
	 document.getElementById("vip_limitdate").value=limitdate;
	 
	 $.ajax({
	   url:'../servlet/UserServlet',
	   type:'get',
	   data:{
	     action:'getPayList'
	   },
	   dataType:'json',
	   	contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
	   	success:function(data,statusx)
	   	{
	   	   var tpl = document.getElementById('tpl_payType').innerHTML;
			laytpl(tpl).render(data, function(render) {
				document.getElementById("pay_type").innerHTML = render;
			});
	   	}
	 });
	 
	
}

function jsApiCall() {
	var total = document.getElementById("payMoney").value;
	var moneyType = document.getElementById("moneyType").value;
	var orderTitle = document.getElementById("orderTitle").value;
	var openId = window.sessionStorage.getItem("openId");
	$.showIndicator();
	//alert("openId:"+openId);
	$.ajax({
		type: 'post',
		url: '../servlet/PayServlet?action=unifiedorder',
		dataType: 'json',
		data: {
			openid: openId,
			body: orderTitle,
			moneytype:moneyType,
			totalfee: total
		},
		success: function(data, textStuatus, jqXHR) {
			$.hideIndicator();
			if (data.msg == null) {
				WeixinJSBridge.invoke('getBrandWCPayRequest', {
						'appId': data.appId,
						'timeStamp': data.timeStamp,
						'nonceStr': data.nonceStr,
						'package': data.packageStr,
						'signType': data.signType,
						'paySign': data.paySign
					},
					function(res) {
						//alert(res.err_code+res.err_desc+res.err_msg);
						if (res.err_msg == "get_brand_wcpay_request:ok") {

							//alert('支付成功');
							var isTemplate= window.sessionStorage.getItem("isTemplate");
							//var istest= window.sessionStorage.getItem("istest");
							window.sessionStorage.setItem("istest",0);
							var title = '支付成功';
						var pageContent = orderTitle+'已经充值成功，平台将在收到支付成功通知后更新您的账户有效期！';
						title = encodeURI(encodeURI(title));
						pageContent = encodeURI(encodeURI(pageContent));
						if(isTemplate==1)
							window.location.href = "MsgResult.html?pageContent=" +
							pageContent + "&pageTitle=" + title ;
						else 
							
						window.location.href = "MsgResult.html?pageContent=" +
							pageContent + "&pageTitle=" + title + "&okUrl=" + "me.html";
							//window.sessionStorage.setItem("limitd",data)
						}
						// 使用以上方式判断前端返回,微信团队郑重提示：res.err_msg将在用户支付成功后返回    ok，但并不保证它绝对可靠。 
						else {
							var prepayId = data.prepayId;
							$.ajax({
								type: 'post',
								url: '../servlet/PayServlet?action=cancelOrder',
								dataType: 'json',
								data: {
									prepayId: prepayId
								},
								success: function(data, textStuatus, jqXHR) {
									alert('支付取消:' + data.msg);
								}
							})

						}

					}
				);
			} else {
				alert(data.msg);
			}
		}

	});

};