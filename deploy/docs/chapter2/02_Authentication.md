认证部分（The Authes）
====

|Version| 1.0.0|
|-
|Author| [`BoPo <http://bopo.me>`](http://bopo.me)|

> 首次撰写：2015-09-02

> 最后修改：-

认证方法
- 用户登录后会返回一个josn,其中`key`值则为认证的码。
- 访问需要认证用户的`API`时，在请求的 `http headers` 里加上该码便可。
- 格式例如： `Authorization:Token 11eb2b41ead9af78cd4c0b9375cb893ed2004d1e` 注意：Token 后面有空格。
- 免责声明的html页面连接为 `http://<domain>/license/` 注意后面的斜线。

举例说明：

```
http GET http://<domain>/api/v1.0/me/profile/ \
Authorization:Token\ 11eb2b41ead9af78cd4c0b9375cb893ed2004d1e
```

如果提示如下信息，说明登录过期，重新登录。

```
{
    "errors": {
        "code": 40x,
        "msgs": "Invalid token。"
    }
}
```

### 接口列表如下:

|URL|HTTP|功能|进度|
|---|---|---|-|
|/auth/login/ | POST | 用户登录 |完成|
|/auth/logout/ | POST | 用户注销 |完成|
|/auth/password/reset/ | POST | 忘记密码重设,请求短信码 |完成|
|/auth/password/reset/confirm/ | POST | 忘记密码重设确认短信码 |完成|
|/auth/password/change/ | POST | 更新密码,要求输入旧密码和两次新密码 |完成|
|/auth/registration/ | POST | 用户注册，用户连接`手机注册前，先请求/auth/registration/verify_mobile/接口`，增加一个设备号(device)参数，由客户端获取并提交，用来判断一个设备最大注册用户数 | 完成 |
|/auth/registration/verify_mobile/ | POST | 请求发送用户手机号码验证短信 |完成|



<!--|/auth/social/ | POST/GET | 社会化第三方绑定，GET列表，POST绑定 |未完成,需要协商|-->
<!--|/auth/password/reset/sms | POST | 请求发送手机短信验证码重置用户密码。 |未完成|-->
<!--|/auth/password/reset/sms/{code} | PUT | 验证手机短信验证码并重置密码。|未完成|-->
<!--|/auth/registration/verify-email/ | POST | 邮件验证 |完成|-->
<!--|/auth/registration/confirm-email/{code} | GET | 邮件验证确认 |完成|-->
<!--|/auth/registration/verify-mobile/ | POST | 请求发送用户手机号码验证短信 |未完成|-->
<!--|/auth/registration/confirm-mobile/{code} | POST | 使用"验证码"验证用户手机号码 |未完成|-->
<!--|/auth/registration/login/sms/code | POST | 请求发送手机号码登录短信。 |未完成|-->
