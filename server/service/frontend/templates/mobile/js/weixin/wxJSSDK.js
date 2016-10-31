/**
 ************************************************************
 *@address lab.bigdatahnu.cn
 *@author liwenjie	
 *@Mail 573015869@qq.com
 *@ver version 1.1
 *@time 2016-02-24
 ************************************************************
 */
var wxJSSDK ={//声明微信全局变量，防止污染外部环境
    version:"1.0",//版本号
    appName:"微商记账助手", //使用当前库的开发者，可以配置应用名字
    isReady:false,//微信JS SDK是否初始化完毕
    access_token:"",//令牌
    ticket:"",//微信临时票据,
    wxImageList:[],//微信图片列表
    wxUploadImageList:[],//需要上传的微信图片列表
    wxImageServerList:[],//微信在数据库中的列表
    wxImageIndex:0,//
    wxVoiceList:[],//微信语音列表
    readySuccessCall:[],//微信初始化成功后的执行事务
    errorSuccessCall:[],//微信初始化失败后的执行事务
    imagePath:'http://ws.datanexus.cn/uploadfile/',
    servletUrl:"../servlet/WXServlet",//servletURL地址
    config:{
        debug: false, // 开启调试模式,调用的所有api的返回值会在客户端alert出来，若要查看传入的参数，可以在pc端打开，参数信息会通过log打出，仅在pc端时才会打印。
        appId: '', // 必填，公众号的唯一标识
        timestamp: '', // 必填，生成签名的时间戳
        nonceStr: '', // 必填，生成签名的随机串
        signature: '',// 必填，签名，见附录1
        jsApiList: [
            "onMenuShareTimeline"
        ] // 必填，需要使用的JS接口列表，所有JS接口列表见附录2
    },
    //删除所有JSApi操作
    removeAllJsApi:function(){
         this.config.jsApiList=[];
    
    },
    /**
     * 检查微信的相关设置
     * @param {Object} jsApi
     */
    checkWX:function(jsApi)
    {
    	if(this.isWeiXin())
    	{
    		if(!wx)
    		{
    			alert('未引用微信JS文件');
    			return false;
    		}
    		else if(!this.isReady)
    		{
    			alert('微信还未注册成功！');
    			return false;
    		}
    		else if(!this.checkJSApi(jsApi))
    		{
    		    alert('该JS API接口未加入到JSAPIList中');
    		    return false;
    		}
    		else
    		    return true;
    	}
    	else
    	{
    		alert('请在微信客户端中使用，谢谢！');
    		return false;
    	}
    },
    //判断是否在微信界面
    isWeiXin:function()
    {
    	var ua=window.navigator.userAgent.toLowerCase();
    	if(ua.match(/MicroMessenger/i)=='micromessenger')
    	{
    	  return true;
    	}
    	else
    	return false;
    },
    checkJSApi:function(jsApi)
    {
       for(var i=0;i<this.config.jsApiList.length;i++)
       {
          if(this.config.jsApiList[i]==jsApi)
          return true;
       }
       return false;
    },
    //删除指定JSApi操作
    removeJsApi:function(jsApi)
    {
       var index= this.config.jsApiList.indexOf(jsApi);
       if(index>-1)
          this.config.jsApiList.remove(index);
    },
    addJsApi:function(jsApi)
    {
      this.config.jsApiList.push(jsApi);
    },
    Del:function()
    {
    	Cookie.Set("ticket",null,3600);
    },
    /*
     函数功能：初始化
     */
    init:function(call,errorcall){
        if(!wx){//验证是否存在微信的js组件
            alert("微信接口调用失败，请检查是否引入微信js！");
            return;
        }
        
        var that = this;//保存当前作用域，方便回调函数使用
        //获取令牌
        this.wxImageList=[];
        this.wxVoiceList=[];
        this.wx_get_token(function(data){
            if(data.access_token){
            	that.config.appId=data.appId;
            	Cookie.Set("appId",data.appId,3600);
				Cookie.Set("timestamp",data.timestamp,3600);
				Cookie.Set("noncestr",data.noncestr,3600);
				Cookie.Set("ticket",data.ticket,3600);
                Cookie.Set("access_token", data.access_token, 3600);
                that.access_token = data.access_token;
                that.config.signature=data.signature;
                that.config.appId=data.appId;
                that.config.nonceStr=data.noncestr;
                that.config.timestamp=data.timestamp;
                
                that.initWx(call,errorcall);
            }
            
          
        });
    },
    //获取令牌
    wx_get_token:function(call){
        this.access_token =  Cookie.Get("access_token");
        var url=window.location.href.split('#')[0];
        if(Cookie.Get("ticket")==null||Cookie.Get("timestamp")==null||Cookie.Get("noncestr")==null){
            
            $.get(this.servletUrl,
            	{action:'getSign',url:url},
               function(data){
                    call && call(data);//回调函数来调用
                   
            },"json");
            return;
        }
        else
        {
            
            var s="jsapi_ticket=" + Cookie.Get("ticket") +
                  "&noncestr=" + Cookie.Get("noncestr") +
                  "&timestamp=" + Cookie.Get("timestamp") +
                  "&url=" + url;
            
           var sign= hex_sha1(s);   
           var data={
                 appId:Cookie.Get("appId"),
                 timestamp:Cookie.Get("timestamp"),
                 noncestr:Cookie.Get("noncestr"),
                 ticket:Cookie.Get("ticket"),
                 access_token:Cookie.Get("access_token"),
                 signature:sign
                 };
            call&&call(data);     
        }
        call && call({});
    },
   
    initWx:function(call, errorCall){//初始化微信接口
        var that = this;
        wx.config(this.config);//初始化配置
        /*config信息验证后会执行ready方法，所有接口调用都必须在config接口获得结果之后，
         *config是一个客户端的异步操作，所以如果需要在页面加载时就调用相关接口，
         *则须把相关接口放在ready函数中调用来确保正确执行。对于用户触发时才调用的接口，
         *则可以直接调用，不需要放在ready函数中。
         * */
        wx.ready(function(){
            that.isReady = true;
            
            if(that.readySuccessCall.length > 0) {//成功初始化后，执行的事务
                $.each(that.readySuccessCall, function(i, n){
                    wxJSSDK[n]();
                });
            }
            call && call();
        });
        /*config信息验证失败会执行error函数，如签名过期导致验证失败，
         *具体错误信息可以打开config的debug模式查看，也可以在返回的res参数中查看，
         * 对于SPA可以在这里更新签名。
         * */
        wx.error(function(res){
            that.isReady = false;
          
            errorCall && errorCall();
            if(that.errorSuccessCall.length > 0) {//成功初始化后，执行的事务
                $.each(that.errorSuccessCall, function(i, n){
                    n();
                });
            }
        });
    }
}
//执行初始化(不默认执行)
//wxJSSDK.init();