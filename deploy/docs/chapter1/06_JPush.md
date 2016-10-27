各种集成说明
===

一般常见会有几种错误，简单的判断错误方法就是判断状态码(`status_code`).

- `20x` 为成功状态
- `40x` 为受限服务，比如`404`没有找到资源，`401`，`403` 没有权限。
- `50x` 不用说了，服务器端错误。可以忽略，或者联系我修正。

push 说明
-----------------------

首先集成 jpush sdk 以后，会分配给设备一个 registration_id 的参数(具体看极光文档)

这个 registration_id 需要在用户注册和登录时候提交给服务器，关联到用户。

比如服务器要向某个用户发送推送，则这个是用户的标示。有了这个 registration_id 才会发送到指定的手机上。

手机端接受到 jpush 推送来的消息，点击后，跳转到 app 的用户消息界面即可(暂时这样)。


淘口令，比较简单，跟搜索差不多
-----------------------

接口：/api/v1.0/watchword/

提交参数有两个
```
{
    "watchword": "",
    "sort": null
}
```
watchword：淘口令的字符串(可以是淘口令，喵口令，或者是复制的链接，推荐复制链接过来)

sort：是返回列表的排序，默认可以为空

例如我们输入 http://share.laiwang.com/s/oDyyq?tm=0c02d5

返回的结果为：
```
{
    "results": [
        {
            "thumb": "http://img.alicdn.com/imgextra/i2/TB1AvitKFXXXXbbXFXXXXXXXXXX_!!0-item_pic.jpg_800x800.jpg",
            "title": "VQGT英伦尖头高帮皮鞋男靴子春秋皮靴男士短靴真皮系带马丁靴短筒",
            "price": "398.00",
            "open_iid": "AAGevuLyACLm9G8GlryjlzbV",
            "detail_url": "http://101.200.136.70:8000/api/v1.0/search/AAGevuLyACLm9G8GlryjlzbV/",
            "pic_url": "http://img.alicdn.com/imgextra/i2/TB1AvitKFXXXXbbXFXXXXXXXXXX_!!0-item_pic.jpg",
            "promotion_price": "398.00"
        }
    ]
}
```
