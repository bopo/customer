基础部分（The Basics）
====
|Version| 1.0.0|
|-
|Author| [`BoPo <http://bopo.me>`](http://bopo.me)|

> 首次撰写：2016-05-06

> 最后修改：-

### 接口列表如下:

|URL|HTTP|功能|进度|
|---|---|---|-|
|/auth/login/ | POST | 用户登录 |完成|
|/auth/logout/ | POST | 用户注销 |完成|
|/auth/password/reset/ | POST | 忘记密码重设,请求短信码 |完成|
|/auth/password/reset/confirm/ | POST | 忘记密码重设确认短信码 |完成|
|/auth/password/change/ | POST | 更新密码,要求输入旧密码和两次新密码 |完成|
|/auth/registration/ | POST | 用户注册，用户连接`手机注册前，先请求/auth/registration/verify_mobile/接口` |完成|
|/auth/registration/verify_mobile/ | POST | 请求发送用户手机号码验证短信 |完成|
