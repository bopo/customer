互动部分（The Interaction）
====

|Version| 1.0.0|
|-
|Author| [`BoPo <http://bopo.me>`](http://bopo.me)|

> 首次撰写：2015-09-02

> 最后修改：-

> 注意：关于api的GET参数说明，API 后面跟随的`{pk}`或者`{id}` 是一个意思，代表改资源(`resource`)的主键.

### 接口列表如下:

|URL|HTTP|功能|权限|进度|
|-|-|-|-|-|
|/v1.0/users/{pk}/follow/|GET|关注用户|认证用户|未开始|
|/v1.0/users/{pk}/articles/|GET|用户的文章|任意用户|未测试|
|/v1.0/articles/{pk}/comments/|GET/POST|评论文章|认证用户|已完成|
|/v1.0/articles/{pk}/favorite/|GET|收藏文章|认证用户|已完成|
|/v1.0/goods/{pk}/favorite/|GET|收藏商品|认证用户|已完成|
|/v1.0/articles/{pk}/favorite/|GET|收藏文章|认证用户|已完成|
|/v1.0/stars/{pk}/favorite/|GET|收藏明星|认证用户|已完成|
|/v1.0/articles/{pk}/like/|GET|喜欢文章|认证用户|已完成|
|/v1.0/stars/{pk}/like/|GET|喜欢明星|认证用户|已完成|
|/v1.0/store/{pk}/like/|GET|喜欢文章|认证用户|已完成|
|/v1.0/goods/{pk}/like/|GET|喜欢商品|认证用户|已完成|

<!--|/v1.0/users/{pk}/subscribe/|GET|订阅文章/用户|认证用户|未测试|-->

