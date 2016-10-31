// 初始化界面
$(document).on("pageInit", ".page", function(e, pageId, $page) {
	// for local test start
//	var data = [
//		{id: 1, picture: "images/cp01.png", name: "初黛", unit: "套", inprice: 40.00, outprice: 98.00},
//		{id: 2, picture: "images/cp04.png", name: "初黛玉", unit: "瓶", inprice: 20.00, outprice: 68.00},
//		{id: 3, picture: "images/cp02.png", name: "深海纯净", unit: "套", inprice: 80.00, outprice: 168.00},
//		{id: 4, picture: "images/cp03.png", name: "小绿澳", unit: "瓶", inprice: 48.00, outprice: 68.00}
//	];
//	
//	renderPage(data);
	// for local test end
	
	// TODO
	initList();
});

//获取所以商品
function initList() {
	var userId = window.sessionStorage.getItem("userId");
	if(userId == null) {
		userId = "73e62a2f4c0411e6bce900163e00209a";
	}
	//alert("测试信息:"+userId);
	$.ajax({
		type: "POST",
		url: "../servlet/UserServlet",
		data: {
			action: "getGoodList",
			userId: userId
		},
		contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
		dataType : 'json',
		 scriptCharset: 'utf-8',
		success: function(data, textStatus) {
			//var obj = eval('(' + data + ')');
			
			renderPage(data);
			
			}
	});
}
//渲染界面
function renderPage(data){
	var tpl = document.getElementById('tpl_goods').innerHTML;
	laytpl(tpl).render(data, function(render) {
		$('#goods_list').html(render);
	});
}