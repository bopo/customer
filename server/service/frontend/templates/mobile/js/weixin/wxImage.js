var isUpload = false;
var isImgExist = false;
//var lenImage = wxJSSDK.wxImageList.length;
wxJSSDK.createImage = function(res, imgDiv, imgWidth, imgHeight) {
		var div = document.getElementById(imgDiv);
		for (var i = 0; i < res.localIds.length; i++) {
			wxJSSDK.wxImageList.push(res.localIds[i]);
			var img = document.createElement("img");
			img.setAttribute("height", imgHeight);
			img.setAttribute("width", imgWidth);
			//img.setAttribute("height","100rem");
			img.src = res.localIds[i];

			img.setAttribute("onclick", "wxJSSDK.showImage('" + res.localIds[i] + "')");
			//img.onclick = "showImage('" + img.src + "',localIds);";
			div.appendChild(img);
		}
	}
	/**
	 * 微信图片处理函数(1):选择图片
	 */
wxJSSDK.chooseImage = function(imageCount, call) {
	if (wxJSSDK.checkWX("chooseImage")) {
		wx.chooseImage({
			count: imageCount, // 默认9
			sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
			sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
			success: function(res) {
				call && call(res);
			}
		});
		//异步操作
	}

}

wxJSSDK.chooseImageWithCall2 = function(imageCount, imgDiv,imgPath) {
        
//  	if(lenImage==5){
//			alert("上传图片超过最大限制！");
//			document.getElementById("ChoosingImage").disabled=true;
//		}else{
    var imageNewCount=imageCount-wxJSSDK.wxImageList.length;
   // alert(wxJSSDK.wxImageList.length+"***");
    //alert(imageNewCount);

    if(imageNewCount<=0)
    {
    	$.toast('最多上传'+imageCount+'张图片');
    	return ;
    }
	wxJSSDK.chooseImage(imageNewCount, function(res) {
		var list = res.localIds.join(',');
		var div = document.getElementById(imgDiv);

		for (var i = 0; i < res.localIds.length; i++) {
			
			//wxJSSDK.wxImageList.push(res.localIds[i]);
			wxJSSDK.wxUploadImageList.push(res.localIds[i]);
			var liEl = document.createElement("li");
			liEl.setAttribute("id", "img_" + res.localIds[i]);
			liEl.setAttribute("class", "dn_uploader_file");
			
			var child1 = document.createElement("div");
			child1.setAttribute("class", "dn_uploader_file_img");
			child1.setAttribute("style","background-image:url("+res.localIds[i]+")");
			child1.setAttribute("onclick", "wxJSSDK.showImage2('" + res.localIds[i] + "','"+imgPath+"')");

			var child2 = document.createElement("i");
			child2.setAttribute("class", "icon icon-dn-minus icon-dn-tr");
			child2.setAttribute("onclick", "wxJSSDK.deleteFaultImage('" + imgDiv + "','img_" + res.localIds[i] + "','" + res.localIds[i] + "')");
			
			liEl.appendChild(child1);
			liEl.appendChild(child2);
			div.appendChild(liEl);
		}
	});
}

/**
 * 带回调的图片选择方法
 * @param {Object} imageCount
 * @param {Object} imgDiv
 * @param {Object} imgWidth
 * @param {Object} imgHeight
 */
wxJSSDK.chooseImageWithCall = function(imageCount, imgDiv, imgWidth, imgHeight) {
        
//  	if(lenImage==5){
//			alert("上传图片超过最大限制！");
//			document.getElementById("ChoosingImage").disabled=true;
//		}else{
    var imageNewCount=imageCount-wxJSSDK.wxImageList.length;
   // alert(wxJSSDK.wxImageList.length+"***");
    //alert(imageNewCount);

    if(imageNewCount<=0)
    {
    	$.alert('最多上传'+imageCount+'张图片');
    	return ;
    }
	wxJSSDK.chooseImage(imageNewCount, function(res) {
		var list = res.localIds.join(',');
		var div = document.getElementById(imgDiv);

		for (var i = 0; i < res.localIds.length; i++) {
			
			wxJSSDK.wxImageList.push(res.localIds[i]);
			var subDiv = document.createElement("div");
			subDiv.setAttribute("id", "img_" + res.localIds[i]);
			subDiv.setAttribute("style", "float:left;align-content: center;vertical-align: middle;margin-left: 0.2rem;");

			var img = document.createElement("img");
			img.setAttribute("height", imgHeight); 
			img.setAttribute("width",imgWidth);
			img.src = res.localIds[i];

			img.setAttribute("onclick", "wxJSSDK.showImage2('" + res.localIds[i] + "')");
			//img.onclick = "showImage('" + img.src + "',localIds);";
			subDiv.appendChild(img);

			var button = document.createElement("button");
			button.setAttribute("style", "margin-left: 0.6rem;margin-bottom: 0.2rem;")
			button.setAttribute("class", "button button-fill button-danger");
			button.innerText = "删除";
			button.setAttribute("onclick", "wxJSSDK.deleteFaultImage('" + imgDiv + "','img_" + res.localIds[i] + "','" + res.localIds[i] + "')");
			subDiv.appendChild(button);

			div.appendChild(subDiv);
		}
	});
}
wxJSSDK.chooseInvoiceImageWithCall = function(imageCount, imgDiv, imgWidth, imgHeight) {
        
//  	if(lenImage==5){
//			alert("上传图片超过最大限制！");
//			document.getElementById("ChoosingImage").disabled=true;
//		}else{
    var imageNewCount=imageCount-wxJSSDK.wxImageList.length;

   // alert(wxJSSDK.wxImageList.length+"***");
    //alert(imageNewCount);

    if(imageNewCount<=0)
    {
    	$.alert('最多上传'+imageCount+'张图片');
    	return ;
    }
	wxJSSDK.chooseImage(imageNewCount, function(res) {
		var list = res.localIds.join(',');
		var div = document.getElementById(imgDiv);

		for (var i = 0; i < res.localIds.length; i++) {
			
			wxJSSDK.wxImageList.push(res.localIds[i]);
			var subDiv = document.createElement("div");
			subDiv.setAttribute("id", "img_" + res.localIds[i]);
			subDiv.setAttribute("style", "float:left;align-content: center;vertical-align: middle;margin:0.5rem 0 0 1.2rem;");

			var img = document.createElement("img");
			img.setAttribute("height", imgHeight); 
			img.setAttribute("width",imgWidth);
			img.src = res.localIds[i];

			img.setAttribute("onclick", "wxJSSDK.showImage2('" + res.localIds[i] + "')");
			//img.onclick = "showImage('" + img.src + "',localIds);";
			subDiv.appendChild(img);

			var button = document.createElement("button");
			button.setAttribute("style", "margin-left: 4.5rem;margin-bottom: 0.2rem;width:5rem;height:1.5rem;font-size:0.8rem")
			button.setAttribute("class", "button button-fill button-danger");
			button.innerText = "删除";
			button.setAttribute("onclick", "wxJSSDK.deleteInvoiceImage('" + imgDiv + "','img_" + res.localIds[i] + "','" + res.localIds[i] + "')");
			subDiv.appendChild(button);
			div.appendChild(subDiv);
			isImgExist = true;
			document.getElementById("addpicture").style.display="none";
			document.getElementById("old_img").style.display="none";
		}
	});
}
wxJSSDK.chooseRegImageWithCall = function(imageCount, imgDiv, imgWidth, imgHeight) {
//  	if(lenImage==5){
//			alert("上传图片超过最大限制！");
//			document.getElementById("ChoosingImage").disabled=true;
//		}else{
    var imageNewCount=imageCount-wxJSSDK.wxImageList.length;
//  alert(wxJSSDK.wxImageList.length+"***");
//  alert(imageNewCount);
    if(imageNewCount<=0)
    {
    	alert('最多上传'+imageCount+'张图片');
    	return ;
    }
	wxJSSDK.chooseImage(imageNewCount, function(res) {
		var list = res.localIds.join(',');
		var div = document.getElementById(imgDiv);

		for (var i = 0; i < res.localIds.length; i++) {
			wxJSSDK.wxImageList.push(res.localIds[i]);
			var subDiv = document.createElement("div");
			subDiv.setAttribute("id", "img_" + res.localIds[i]);
			subDiv.setAttribute("style", "float:left;width:110px;align-content: center;vertical-align: middle;margin:4px auto 8px auto;");
			var img = document.createElement("img");
			img.setAttribute("height", imgHeight);
			img.setAttribute("width", imgWidth);
			//img.setAttribute("height","100rem");
			img.src = res.localIds[i];

			img.setAttribute("onclick", "wxJSSDK.showImage2('" + res.localIds[i] + "')");
			//img.onclick = "showImage('" + img.src + "',localIds);";
			subDiv.appendChild(img);

			var button = document.createElement("button");
			button.setAttribute("type", "button");
			button.setAttribute("style", "margin-left: 20px;text-align:center;padding:0px;height:26px;line-height:22px;width:60px")
			button.setAttribute("class", "mui-btn mui-btn-danger");
			button.innerText = "删除";
			button.setAttribute("onclick", "wxJSSDK.deleteRegImage('" + imgDiv + "','img_" + res.localIds[i] + "','" + res.localIds[i] + "')");
			subDiv.appendChild(button);

			div.appendChild(subDiv);
		}
	});
}

wxJSSDK.shopheadimgchooseImageWithCall = function(imageCount, imgDiv, imgWidth, imgHeight) {
//  	if(lenImage==5){
//			alert("上传图片超过最大限制！");
//			document.getElementById("ChoosingImage").disabled=true;
//		}else{
    var imageNewCount=imageCount-wxJSSDK.wxImageList.length;
//  alert(wxJSSDK.wxImageList.length+"***");
//  alert(imageNewCount);
    if(imageNewCount<=0)
    {
    	alert('最多上传'+imageCount+'张图片');
    	return ;
    }
	wxJSSDK.chooseImage(imageNewCount, function(res) {
		var list = res.localIds.join(',');
		var img = document.getElementById(imgDiv);
		
		for (var i = 0; i < res.localIds.length; i++) {
			wxJSSDK.wxImageList.push(res.localIds[i]);
			//var subDiv = document.createElement("div");
			//subDiv.setAttribute("id", "img_" + res.localIds[i]);
			//subDiv.setAttribute("style", "position:absolute; width:48%;height:100%; left:28%; top:0px;border:red solid 1px;");
			//var img = document.createElement("img");
			//img.setAttribute("height", "100%");
			//img.setAttribute("width", "100%");
			//img.setAttribute("height","100rem");
			img.src = res.localIds[i];
			//alert(img.src);
			img.setAttribute("onclick", "wxJSSDK.showImage2('" + res.localIds[i] + "')");
			//img.onclick = "showImage('" + img.src + "',localIds);";
			//subDiv.appendChild(img);

			//var button = document.createElement("button");
			//button.setAttribute("type", "button");
			//button.setAttribute("style", "margin-left: 20px;text-align:center;padding:0px;height:26px;line-height:22px;width:60px")
			//button.setAttribute("class", "mui-btn mui-btn-danger");
			//button.innerText = "删除";
			//button.setAttribute("onclick", "wxJSSDK.deleteRegImage('" + imgDiv + "','img_" + res.localIds[i] + "','" + res.localIds[i] + "')");
			//subDiv.appendChild(button);

			//div.appendChild(subDiv);
		}
	});
}

wxJSSDK.deleteFaultImage = function(imgDiv, imgId, src) {
	var div = document.getElementById(imgDiv);
	var img = document.getElementById(imgId);
	var arr = wxJSSDK.wxImageList;
	var arr2=wxJSSDK.wxUploadImageList;
	wxJSSDK.wxImageList = [];
	wxJSSDK.wxUploadImageList=[];
	var temp = "";
	if (isUpload) {
		$.alert("您已上传图片，不能删除！");
	} else {
		div.removeChild(img);
		for (var i = 0; i < arr.length; i++) {
			if (!(arr[i] == src)) {
				wxJSSDK.wxImageList.push(arr[i]);
			}
			
		}
		for(var j=0;j<arr2.length;j++)
		{
		    if(!(arr2[j]==src))
		    {
		       wxJSSDK.wxUploadImageList.push(arr2[j]);
		    }
		}
	}
}

wxJSSDK.deleteRegImage = function(imgDiv, imgId, src) {
	var div = document.getElementById(imgDiv);
	var img = document.getElementById(imgId);
	var arr = wxJSSDK.wxImageList;
	wxJSSDK.wxImageList = [];
	var temp = "";
	if (isUpload) {
		mui.toast("您已上传图片，不能删除！");
	} else {
		div.removeChild(img);
		for (var i = 0; i < arr.length; i++) {
			if (!(arr[i] == src)) {
				wxJSSDK.wxImageList.push(arr[i]);
			}
		}
	}
}
wxJSSDK.deleteInvoiceImage = function(imgDiv, imgId, src) {
	var div = document.getElementById(imgDiv);
	var img = document.getElementById(imgId);
	var arr = wxJSSDK.wxImageList;
	wxJSSDK.wxImageList = [];
	var temp = "";
	if (isUpload) {
		$.alert("您已上传图片，不能删除！");
	} else {
		div.removeChild(img);
		document.getElementById("addpicture").style.display="block";
		document.getElementById("old_img").style.display="";
		for (var i = 0; i < arr.length; i++) {
			if (!(arr[i] == src)) {
				wxJSSDK.wxImageList.push(arr[i]);
				isImgExist = false;
			}
		}
	}
}


wxJSSDK.deleteImage = function(imgDiv, imgId, src) {
	var div = document.getElementById(imgDiv);
	var img = document.getElementById(imgId);
	div.removeChild(img);

	//	wxJSSDK.wxImageList.remove(src);
	//  wxJSSDK.wxImageList.splice(src,1);
	//  var temp="";
	//  for(var i=0;i<wxJSSDK.wxImageList.length;i++)
	//  	{
	//  	temp=temp+wxJSSDK.wxImageList[i]+",";
	//  	}
	//  alert(temp);

}

wxJSSDK.lookImage=function(current,imgList,imgPath)
{
	wxJSSDK.showImage2(current,imgPath);
			  
//				var urls=wxJSSDK.wxImageList;
//				urls=urls.concat(wxJSSDK.wxUploadImageList);
//				//var current=urls[0];
//				//alert(urls);
//				if(imgList.length==0){
//					$.alert("暂无图片")
//				}
//               // alert(current);
//				current=imgPath+current;
//				var temp="";
//				for(var i=0;i<urls.length-1;i++)
//				   {
//				   	 if(urls[i]!="")
//				   	   temp=temp+imgPath+urls[i]+","
//				   }
//				   if(urls[urls.length-1]!="")
//				 temp=temp+imgPath+urls[urls.length-1];
//				   //alert(current);
//				    //alert(temp);
//				//imgList= imgList.replace('|',',');
//				//alert(imgList);
//				wxJSSDK.showImage(current,temp);
}		
wxJSSDK.showImage = function(currentId, urldStr) {

	if (wxJSSDK.checkWX("imagePreview")) {
		//				alert(currentId);
		//				alert(urlds);
		var urlds = urldStr.split(',');
        var currentPath=wxJSSDK.imagePath+currentId;
        var urls=[];
        for(var i=0;i<urlds.length;i++)
        { 
        	//alert(wxJSSDK.imagePath+urlds[i]);
        	if(urlds[i]!="")
        	{
        	urls.push(wxJSSDK.imagePath+urlds[i]);
        	}
        }
		wx.previewImage({
			current: currentPath, // 当前显示图片的http链接
			urls: urls// 需要预览的图片http链接列表
		});

	}

}

wxJSSDK.showImage2 = function(currentId,imgPath) {

	if (wxJSSDK.checkWX("imagePreview")) {
		//				alert(currentId);
		//				alert(urlds);
		//var urlds =urldStr.split(',');
        var urls=[];
        for(var i=0;i<wxJSSDK.wxImageList.length;i++)
        {
           urls.push(wxJSSDK.imagePath+imgPath+wxJSSDK.wxImageList[i]);
        }
        for(var j=0;j<wxJSSDK.wxUploadImageList.length;j++)
        {
        	urls.push(wxJSSDK.wxUploadImageList[j])
        }
        //urls= urls.contact(wxJSSDK.wxUploadImageList);
        
        
		wx.previewImage({
			current: currentId, // 当前显示图片的http链接
			urls: urls // 需要预览的图片http链接列表
		});

	}

}

wxJSSDK.uploadImageWithCall = function(savefilepath,isCut,call) {
	var tempCount = 0;
	var tempImg = "";
	var imageList = wxJSSDK.wxUploadImageList;
	if(imageList.length==0)
	{
      var data={
      fileName:''
      };
	  call&&call(data);
	}
	else
	{
	wxJSSDK.uploadImageNew(imageList,0, function(res) {
		tempCount++;
		if (!savefilepath || savefilepath == "")
			savefilepath = "uploadfile";
		var serverId = res.serverId; // 返回图片的服务器端ID
		//console.log(serverId);
		tempImg = tempImg + serverId + ',';
		if (tempCount >= imageList.length) {

			//alert(tempImg);

			$.ajax({
				type: "get",
				url: "../servlet/WXServlet?action=downloadImage&isCut="+isCut+"&serverIds=" + tempImg + "&savePath=" + savefilepath,
				async: true,
				dataType: 'json',
				success: function(data, textStuatus, jqXHR) {
					//return "{success:1,data:'"+data.fileName+"'}";
					//alert('已将如下文件成功下载到服务器：' + data.fileName);
					window.sessionStorage.setItem('fileName', data.fileName);
					
					call && call(data);
					wxJSSDK.wxUploadImageList=[];

				}
			});
		}

	});
	}

}

//wxJSSDK.uploadFaultImageWithCall = function(savefilepath, call) {
//
//	if (isUpload == false) {
//		layer.open({
//			content: '上传图片后将不能删除和重新选择，确认上传吗？',
//			btn: ['确认', '取消'],
//			shadeClose: false,
//			yes: function(index) {
//				layer.close(index);
//				if (wxJSSDK.wxImageList.length == 0) {
//					alert("没有要上传的图片");
//					return;
//				} else {
//					document.getElementById("ChoosingImage").disabled = true;
//					var tempCount = 0;
//					var tempImg = "";
//					var imageList = wxJSSDK.wxImageList;
//					wxJSSDK.uploadImage(imageList, function(res) {
//						tempCount++;
//						if (!savefilepath || savefilepath == "")
//							savefilepath = "uploadfile";
//						var serverId = res.serverId; // 返回图片的服务器端ID
//						//console.log(serverId);
//						tempImg = tempImg + serverId + ',';
//						if (tempCount >= imageList.length) {
//							alert(tempImg);
//							$.ajax({
//								type: "get",
//								url: "../../servlet/WXServlet?action=downloadImage&serverIds=" + tempImg + "&savePath=" + savefilepath,
//								async: true,
//								dataType: 'json',
//								success: function(data, textStuatus, jqXHR) {
//									//return "{success:1,data:'"+data.fileName+"'}";
//									alert('已将如下文件成功下载到服务器：' + data.fileName);
//									window.sessionStorage.setItem('fileName', data.fileName);
//									call && call(data);
//									isUpload = true;
//									//					alert(isUpload);
//								}
//							});
//						}
//
//					});
//				}
//
//			},
//			no: function(index) {
//				layer.close(index);
//				alert("您已取消上传图片！");
//			}
//		});
//	}
//}

wxJSSDK.uploadFaultImage = function(savefilepath,call) {

	if (isUpload == false) {
		if (wxJSSDK.wxImageList.length == 0) {
			$.alert('没有要上传的图片!');
		} else {

			$.confirm('上传图片后将不能删除和重新选择，确认上传吗？', '信息提示',
				function() {
//					$.alert('您已选择上传图片！');
                    //$.closeModal(confirm('您已选择上传照片！'));
					document.getElementById("ChoosingImage").disabled = true;
					var tempCount = 0;
					var tempImg = "";
					var imageList = wxJSSDK.wxImageList;
					wxJSSDK.uploadImage(imageList, function(res) {
						tempCount++;
						if (!savefilepath || savefilepath == "")
							savefilepath = "uploadfile";
						var serverId = res.serverId; // 返回图片的服务器端ID
						//console.log(serverId);
						tempImg = tempImg + serverId + ',';
						if (tempCount >= imageList.length) {

							//alert(tempImg);

							$.ajax({
								type: "get",
								url: "../../servlet/WXServlet?action=downloadImage&serverIds=" + tempImg + "&savePath=" + savefilepath,
								async: true,
								dataType: 'json',
								success: function(data, textStuatus, jqXHR) {
									//return "{success:1,data:'"+data.fileName+"'}";
									//alert('已将如下文件成功下载到服务器：' + data.fileName);
									window.sessionStorage.setItem('fileName', data.fileName);
									call && call(data);
									isUpload = true;
									//					alert(isUpload);
								}
							});
						}
					});


				},
				function() {
					$.alert('您已取消上传图片！');
				}
			);
		}
	} else {
		$.alert("您已上传照片，无法再上传！");
	}
}

wxJSSDK.uploadRegImage = function(savefilepath, call) {
	if (isUpload == false) {
		if (wxJSSDK.wxImageList.length == 0) {
			mui.toast('没有要上传的图片!');
		} else {
			//var btnArray = ['是', '否'];
			//mui.confirm('上传图片后将不能删除和重新选择，确认上传吗？', '信息提示', btnArray, function(e) {
				if (confirm('上传图片后将不能删除和重新选择，确认上传吗？')) {
					document.getElementById("ChoosingImage").disabled = true;
					var tempCount = 0;
					var tempImg = "";
					var imageList = wxJSSDK.wxImageList;
					wxJSSDK.uploadImage(imageList, function(res) {
						tempCount++;
						if (!savefilepath || savefilepath == "")
							savefilepath = "uploadfile/shopImg";
						var serverId = res.serverId; // 返回图片的服务器端ID
						//console.log(serverId);
						tempImg = tempImg + serverId + ',';
						if (tempCount >= imageList.length) {
							//alert(tempImg);
							$.ajax({
								type: "get",
								url: "servlet/WXServlet?action=downloadImage&serverIds=" + tempImg + "&savePath=" + savefilepath,
								async: true,
								dataType: 'json',
								success: function(data, textStuatus, jqXHR) {
									//return "{success:1,data:'"+data.fileName+"'}";
									//alert('已将如下文件成功下载到服务器：' + data.fileName);
									window.sessionStorage.setItem('regfileName', data.fileName);
									call && call(data);
									isUpload = true;
									//					alert(isUpload);
								}
							});
						}
					});
				} else {
					mui.toast('您已取消上传图片！');
				}
			//})
		}
	} else {
		mui.toast("您已上传照片，无法再上传！");
	}
}
wxJSSDK.uploadInvoiceImage = function(savefilepath, call) {
	if (isUpload == false) {
		if (wxJSSDK.wxImageList.length == 0) {
			$.alert("没有要上传的图片！");
		} else {

			$.confirm('上传图片后将不能删除和重新选择，确认上传吗？', '信息提示',
				function() {
//					$.alert('您已选择上传图片！');
                    //$.closeModal(confirm('您已选择上传照片！'));
					document.getElementById("ChoosingImage").disabled = true;
					var tempCount = 0;
					var tempImg = "";
					var imageList = wxJSSDK.wxImageList;
					wxJSSDK.uploadImage(imageList, function(res) {
						tempCount++;
						if (!savefilepath || savefilepath == "")
							savefilepath = "uploadfile/equipInvoice";
						var serverId = res.serverId; // 返回图片的服务器端ID
						//console.log(serverId);
						tempImg = tempImg + serverId + ',';
						if (tempCount >= imageList.length) {

							//alert(tempImg);

							$.ajax({
								type: "get",
								url: "../../servlet/WXServlet?action=downloadImage&serverIds=" + tempImg + "&savePath=" + savefilepath,
								async: true,
								dataType: 'json',
								success: function(data, textStuatus, jqXHR) {
									//return "{success:1,data:'"+data.fileName+"'}";
									//alert('已将如下文件成功下载到服务器：' + data.fileName);
									window.sessionStorage.setItem('invoice_pic', data.fileName);
									call && call(data);
									isUpload = true;
									//					alert(isUpload);
								}
							});
						}
					});


				},
				function() {
					$.alert('您已取消上传图片！');
				}
			);
		}
	} else {
		$.alert("您已上传照片，无法再上传！");
	}
}

wxJSSDK.uploadshopheadImage = function(savefilepath, call) {
	if (isUpload == false) {
		if (wxJSSDK.wxImageList.length == 0) {
			mui.toast('没有要上传的图片!');
		} else {
			//var btnArray = ['是', '否'];
			//mui.confirm('上传图片后将不能删除和重新选择，确认上传吗？', '信息提示', btnArray, function(e) {
				if (confirm('确认上传吗？')) {
					document.getElementById("ChoosingImage").disabled = true;
					var tempCount = 0;
					var tempImg = "";
					var imageList = wxJSSDK.wxImageList;
					wxJSSDK.uploadImage(imageList, function(res) {
						tempCount++;
						if (!savefilepath || savefilepath == "")
							savefilepath = "uploadfile/shopHeaderImg";
						var serverId = res.serverId; // 返回图片的服务器端ID
						//console.log(serverId);
						tempImg = tempImg + serverId + ',';
						if (tempCount >= imageList.length) {
							//alert(tempImg);
							$.ajax({
								type: "get",
								url: "../servlet/WXServlet?action=downloadImage&serverIds=" + tempImg + "&savePath=" + savefilepath,
								async: true,
								dataType: 'json',
								success: function(data, textStuatus, jqXHR) {
									//return "{success:1,data:'"+data.fileName+"'}";
									//alert('已将如下文件成功下载到服务器：' + data.fileName);
									window.sessionStorage.setItem('headimgName', data.fileName);
									call && call(data);
									isUpload = true;
									//alert(data.fileName);
									var shopid = window.sessionStorage.getItem('shop_id');
									var headimgName = window.sessionStorage.getItem('headimgName');
									$.post('../servlet/shopCenterServlet',
			      	   				{
			      	   		   		 	action:'changeheadportrait',
			      	   		    		shopid:shopid,
			      	   		    		headimgName:headimgName
			      	        		},function(result){
			      	 				var obj=eval('('+result+')');
			      	 				if(obj.success){
			      	 				window.sessionStorage.removeItem('headimgName');
			      	 				}else{
			      	 					mui.toast(obj.msg);
			      	 				}
			      		 			},'text')
									//					alert(isUpload);
									window.location.href="Bussiness_Center_Info.html";
								}
							});
						}
					});
				} else {
					mui.toast('您已取消上传图片！');
				}
			//})
		}
	} else {
		mui.toast("您已上传照片，无法再上传！");
	}
}

wxJSSDK.downloadImageFromWXServer=function(savefilepath,call)
{
	var tempImage="";
  for(var j=0;j<wxJSSDK.wxImageServerList.length-1;j++)
  {
     tempImage=tempImage+wxJSSDK.wxImageServerList[j]+",";
  }
  tempImage=tempImage+wxJSSDK.wxImageServerList[wxJSSDK.wxImageServerList.length-1];
  //alert(tempImage);
  $.ajax({
								type: "get",
								url: "../../servlet/WXServlet",
								data:{
								  action:'downloadImage',
								  serverIds:tempImage,
								  savePath:savefilepath
								},
								async: true,
								dataType: 'json',
								success: function(data, textStuatus, jqXHR) {
									//return "{success:1,data:'"+data.fileName+"'}";
									//alert('已将如下文件成功下载到服务器：' + data.fileName);
									window.sessionStorage.setItem('fileName', data.fileName);
									call && call(data);
									isUpload = true;
									wxJSSDK.wxImageServerList=[];
									//					alert(isUpload);
								}
							});
  
}
wxJSSDK.uploadOneImage=function()
{
    var imageCount=wxJSSDK.wxImageList.length;
    if(wxJSSDK.wxImageIndex>=imageCount)
    {
    	//$.alert("count为零");
       return;
    }
    else
    {
       wx.uploadImage({
				localId: wxJSSDK.wxImageList[wxJSSDK.wxImageIndex], // 需要上传的图片的本地ID，由chooseImage接口获得
				isShowProgressTips: 1, // 默认为1，显示进度提示
				success: function(res) {
				     wxJSSDK.wxImageIndex++;
				     var imageCount2=wxJSSDK.wxImageList.length;
				    
				     wxJSSDK.wxImageServerList.push(res.serverId);
				     if(wxJSSDK.wxImageIndex==imageCount2)
				     {
				     	//alert("开始下载文件");
				     	var saveFilePath="";
				        wxJSSDK.downloadImageFromWXServer(saveFilePath,function(){
				          $.alert("已经成功上传"+wxJSSDK.wxImageServerList.length+"张图片");
				        });
				     }
				     else
				     {
				        wxJSSDK.uploadOneImage();
				     }
				}
			});
    }
}

wxJSSDK.uploadImageWithNew = function() {

	if (isUpload == false) {
		if (wxJSSDK.checkWX("uploadImage")) {
			
			$.confirm('上传图片后将不能删除和重新选择，确认上传吗？', '信息提示',
				function() {
//					$.alert('您已选择上传图片！');
                    //$.closeModal(confirm('您已选择上传照片！'));
					document.getElementById("ChoosingImage").disabled = true;
			var imageCount = wxJSSDK.wxImageList.length;
			if (imageCount <= 0) {

				alert("没有可以上传的图片");

				return;

			} else {

				wxJSSDK.uploadOneImage();
			}
				},function()
				{
				  $.alert('您已取消上传图片！');
				});
		} else {
			alert("不支持文件上传");
		}

	}
	else
	{
	   $.alert("您已上传照片，无法再上传！");
	}
}

wxJSSDK.uploadImageNew = function(imageList,i, call) {

	if (wxJSSDK.checkWX("uploadImage"))

	{
		
        // var imageNames='';
         wx.uploadImage({
				localId: imageList[i], // 需要上传的图片的本地ID，由chooseImage接口获得
				isShowProgressTips: 1, // 默认为1，显示进度提示
				success: function(res) {
				    call && call(res);
					i++;
					if(i<imageList.length)
					wxJSSDK.uploadImageNew(imageList,i,call);
				}
			});
		
	}


}


wxJSSDK.uploadImage = function(imageList, call) {

	if (wxJSSDK.checkWX("uploadImage"))

	{
		//		var tempImg = '';
		//		var tempCount = 0;
		//var imageList = wxJSSDK.wxImageList;
         var imageNames='';
		for (var i = 0; i < imageList.length; i++) {
			wx.uploadImage({
				localId: imageList[i], // 需要上传的图片的本地ID，由chooseImage接口获得
				isShowProgressTips: 1, // 默认为1，显示进度提示
				success: function(res) {
					//					tempCount++;
					//					var serverId = res.serverId; // 返回图片的服务器端ID
					//					//console.log(serverId);
					//					tempImg = tempImg + serverId + ',';
					//					if (tempCount >= imageList.length) {
					//						alert(tempImg);
					//						$.ajax({
					//							type: "get",
					//							url: "../../servlet/WXServlet?action=downloadImage&serverIds=" + tempImg + "&savePath=" + saveFilePath,
					//							async: true,
					//							dataType: 'json',
					//							success: function(data, textStuatus, jqXHR) {
					//								//return "{success:1,data:'"+data.fileName+"'}";
					//								alert('已将如下文件成功下载到服务器：' + data.fileName);
					//								window.sessionStorage.setItem('fileName', data.fileName);
					//							}
					//						});
					//					}
//					imageNames=res.ser
//					
//					if(i==imageList.length-1)
//					{
//					   call&&call(imageNames);
//					}
					call && call(res);
				}
			});
		}
	}


}