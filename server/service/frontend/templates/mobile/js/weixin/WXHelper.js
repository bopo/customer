function getWeiXinSign(url)
{
	//if(Cookie.Get("ticket")==null)
	if(1==1)
	{
		$.ajax({
					type:"get",
					url:"../../servlet/WXServlet?action=getSign&url="+url,
					async:false,
					dataType:'json',
					success:function(data,statusString,xhrquery)
					{
						Cookie.Set("appId",data.appId);
						Cookie.Set("timestamp",data.timestamp);
						Cookie.Set("noncestr",data.noncestr);
						Cookie.Set("ticket",data.signature,3600);
						return data.signature;
		             
						
					},
					error:function(request,textStatus,errorThrow){
						console.log("获取令牌失败:"+textStatus);
					   return "";
					}
				});
	}
	else{
		
		var s="jsapi_ticket=" + Cookie.Get("ticket") +
                  "&noncestr=" + Cookie.Get("noncestr") +
                  "&timestamp=" + Cookie.Get("timestamp") +
                  "&url=" + url;
		return hex_sha1(s);
	}
	
	
		
}
