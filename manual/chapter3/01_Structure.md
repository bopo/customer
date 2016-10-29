语法结构
===

#### 列表返回结果结构

| 参数 | 说明 | 备注 |
| -- | -- | -- |
| count | 记录总数 | ~ |
| next | 下页链接 | 不足分页返回null |
| previous | 上页链接 | 不足分页返回null |
| results | 结果记录 | ~ |
| url | 详细项目的url | 如果有这个参数，可以通过这个参数直接跳转 |


#### 调用举例

```
{
    "count": 346,
    "next": "http://moo.life:8088/api/v1.0/stars/?page=2",
    "previous": null,
    "results": [
        {
            "url": "http://moo.life:8088/api/v1.0/stars/173/",
            "name": "李敏贞",
            "zodiac": "水瓶座",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2015/01-04/0-PnEWvl.jpg"
        },
        {
            "url": "http://moo.life:8088/api/v1.0/stars/103/",
            "name": "宋丹丹",
            "zodiac": "宋丹丹",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2015/01-04/0-QsdSza.jpg"
        },
        {
            "url": "http://moo.life:8088/api/v1.0/stars/119/",
            "name": "李冰冰",
            "zodiac": "双鱼座",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2014/12-30/0-Iz6kbg.jpg"
        },
        {
            "url": "http://moo.life:8088/api/v1.0/stars/338/",
            "name": "姜武",
            "zodiac": "天蝎座",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2015/01-04/0-nVj0cB.jpg"
        },
        {
            "url": "http://moo.life:8088/api/v1.0/stars/324/",
            "name": "薛之谦",
            "zodiac": "巨蟹座",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2015/01-04/0-Dk0BQX.jpg"
        },
        {
            "url": "http://moo.life:8088/api/v1.0/stars/226/",
            "name": "何润东",
            "zodiac": "处女座",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2015/01-04/0-E4I3sw.jpg"
        },
        {
            "url": "http://moo.life:8088/api/v1.0/stars/227/",
            "name": "方力申",
            "zodiac": "双鱼座",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2015/01-04/0-8RZ45g.jpg"
        },
        {
            "url": "http://moo.life:8088/api/v1.0/stars/236/",
            "name": "张学友",
            "zodiac": "狮子座",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2014/12-30/0-GZCBUn.jpg"
        },
        {
            "url": "http://moo.life:8088/api/v1.0/stars/156/",
            "name": "徐若瑄",
            "zodiac": "双鱼座",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2014/12-30/0-o0Tv0B.jpg"
        },
        {
            "url": "http://moo.life:8088/api/v1.0/stars/182/",
            "name": "刘仁娜",
            "zodiac": "刘仁娜",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2014/12-31/0-uKjuBJ.jpg"
        },
        {
            "url": "http://moo.life:8088/api/v1.0/stars/144/",
            "name": "薛凯琪",
            "zodiac": "狮子座",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2015/01-04/0-oQ3HpR.jpg"
        },
        {
            "url": "http://moo.life:8088/api/v1.0/stars/140/",
            "name": "吴千语",
            "zodiac": "天蝎座",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2015/01-04/0-HKjcko.jpg"
        },
        {
            "url": "http://moo.life:8088/api/v1.0/stars/86/",
            "name": "韩智敏 ",
            "zodiac": "天蝎座",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2015/01-04/0-OCQY9e.jpg"
        },
        {
            "url": "http://moo.life:8088/api/v1.0/stars/118/",
            "name": "郑爽",
            "zodiac": "狮子座",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2014/12-30/0-ESrX5o.jpg"
        },
        {
            "url": "http://moo.life:8088/api/v1.0/stars/185/",
            "name": "秋瓷炫",
            "zodiac": "水瓶座",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2014/12-30/0-ISxxy6.jpg"
        },
        {
            "url": "http://moo.life:8088/api/v1.0/stars/255/",
            "name": "李光洙",
            "zodiac": "巨蟹座",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2015/01-05/0-guDf7L.jpg"
        },
        {
            "url": "http://moo.life:8088/api/v1.0/stars/171/",
            "name": "刘仁英",
            "zodiac": "魔羯座",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2015/01-05/0-RYSwCF.jpg"
        },
        {
            "url": "http://moo.life:8088/api/v1.0/stars/263/",
            "name": "尹斗俊",
            "zodiac": "巨蟹座",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2015/01-05/0-rmyc9u.jpg"
        },
        {
            "url": "http://moo.life:8088/api/v1.0/stars/146/",
            "name": "蒙嘉慧",
            "zodiac": "狮子座",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2015/01-04/0-AdbLBl.jpg"
        },
        {
            "url": "http://moo.life:8088/api/v1.0/stars/250/",
            "name": "刘在石",
            "zodiac": "狮子座",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2014/12-31/0-YpY9Yo.jpg"
        }
    ]
}
```

