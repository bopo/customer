接入指南
=====

|Version| 1.0.0|
|-
|Author| [`BoPo <http://bopo.me>`](http://bopo.me)|

> 特别说明：
- 注册，登录的测试接口表单，默认显示json数据结构。
- 增加一个测试的高级管理账号 `develop` 密码 `secret`。
- 更新测试 `http://mi-tang.com:8088/api/v1.0/`。

> 问题：接口方面 补全下数据吧 比如说 烦null的地方 比如说反数组的地方 加数据吧 否则不知道怎么解析

> 解答：如果是空列表数据则会返回以下结构，直接解析json就可以了，判断results 是否空即可。

```
{
    "count": 0,
    "next": null,
    "previous": null,
    "results": []
}
```

> 如果是单条空数据 则会返回以下内容，直接解析json就可以了，判断是否有detail，有则为空数据，或者有异常错误的数据。

```
{
    "errors": {
        "code": 404,
        "msgs": "你要找的内容不存在。"
    }
}
```



