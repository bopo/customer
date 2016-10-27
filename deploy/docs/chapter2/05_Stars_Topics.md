明星相关 （The Stars）
====

|Version| 1.0.0|
|-
|Author| [`BoPo <http://bopo.me>`](http://bopo.me)|

> 首次撰写：2015-09-02

> 最后修改：-

> 注意：关于api的GET参数说明，api后面跟随的`{pk}`或者`{id}` 是一个意思，代表改资源(`resource`)的主键.

### 接口列表如下:
|URL|HTTP|功能|权限|进度|
|--|--|--|-|
|/v1.0/stars|GET|获得明星列表数据|任意用户|完成|
|/v1.0/stars/{id}|POST|获取单个明星详细信息|任意用户|完成|
|/v1.0/stars/{id}/favorite|GET|收藏明星|认证用户|完成|

