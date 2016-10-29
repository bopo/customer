用户部分（The Users）
====

|Version| 1.0.0|
|-
|Author| [`BoPo <http://bopo.me>`](http://bopo.me)|

> 首次撰写：2015-09-02

> 最后修改：-

> 注意：关于api的GET参数说明，api后面跟随的`{pk}`或者`{id}` 是一个意思，代表改资源(`resource`)的主键.

### 接口列表如下(登录权限):
> 注意：删除(delete)，更新(put)操作需带参数主键id


| URL | HTTP | 功能 | 备注 |进度|
| --- | ---- | ---- | ---- |--|
| /api/v1.0/me/profile/ | GET | 我的详细信息 | 需登录 |完成|
| /api/v1.0/me/affairs/ | GET | 我的财务，中奖信息 | 需登录 |完成|
| /api/v1.0/me/notices/ | GET | 我的公告提醒信息,用户消息显示列表（注意：如果owenr为空的则为系统公告，要置顶） | 需登录 |完成|
| /api/v1.0/me/extract/ | GET | 我的提现记录信息 | 需登录 |完成|
| /api/v1.0/me/shared/ | GET/POST |  GET请求为用户中心的分享记录列表；POST请求为分享成功后的回调，字段内容请查看API网址raw data内容 | 需登录 |完成|
| /api/v1.0/me/orders/ | GET |  我的淘宝(购买)订单信息 | 需登录 | 完成 |

### 交易接口 (登录权限):
> 注意：只支持 post 请求

| URL | HTTP | 功能 | 备注 |进度|
| --- | ---- | ---- | ---- |--|
| /api/v1.0/trade/ | POST | 购买商品后回调接口 | 需登录 |完成|

<!--| /v1.0/me/likes/{type} | GET/DELETE |  我的喜欢记录<br/> 类型：<ul><li>goods</li><li>store</li><li>stars</li> | ~ |未完成|-->
<!--| /v1.0/me/follows/ | GET/DELETE | 我的关注记录 | 需登录 |完成|-->
<!--| /v1.0/me/scores/ | GET | 我的积分记录 | 需登录 |完成|-->
<!--| /v1.0/me/fans/ | GET | 我的粉丝记录 | 需登录 |完成|-->
<!--| /v1.0/me/comments/ | GET/DELETE | 我的评论记录 | 需登录 |完成|-->
<!--| /v1.0/me/articles/ | GET/DELETE | 我的写的文章 | 需登录 |完成|-->

<a name="me_detail"></a>
### 登录用户信息 (~/me/)

>  ##### 版本：v1.0
>  ##### 方法：GET

#### 接口调用说明
开发者可通过OpenID来获取用户基本信息。请使用https协议。

```
http请求方式: GET
http://bopo.me:8088/api/v1.0/me/profile
```

#### 调用举例

```
http GET http://bopo.me:8088/api/v1.0/me/profile
```

#### 调用参数说明
|参数|说明|备注|
|---|---|---|
|id|用户id|~|

#### 返回说明
正常情况下，获取数据接口的返回JSON数据包如下：
```

{
    "name": "",
    "nick": null,
    "phone": "",
    "avatar": null,
    "gender": "male",
    "zodiac": "",
    "birthday": null,
    "alipay": "",
    "qq": "",
    "payment": "0.00",
    "balance": "0.00",
    "total": "0.00",
    "qrcode": "http://101.200.136.70:8000/q/6d7gw",
    "jpush_registration_id": "werw",
    "slug": "6d7gw"
}
```


- #### 返回参数说明

|参数|说明|备注|
|---|---|---|
|name|姓名|~|
|nick|昵称|~|
|avatar|头像|~|
|gender|性别|~|

- #### 返回错误信息

错误时会返回错误码等信息，JSON数据包示例如下:

```
{
    "errors": {
        "code": 403,
        "msgs": "身份认证信息未提供许。"
    }
}
```

