内容相关（The Contents）
====

|Version| 1.0.0|
|-
|Author| [`BoPo <http://bopo.me>`](http://bopo.me)|

> 首次撰写：2015-09-02

> 最后修改：2016-07-22

> 注意：关于api的GET参数说明，api后面跟随的`{pk}`或者`{id}` 是一个意思，代表改资源(`resource`)的主键.

### 接口列表如下:
#### 基础数据

|URL|HTTP|功能|权限|进度|
|-|-|-|-|-|
|[/v1.0/start/](#start_summary)|GET|APP开启时获取的基础数据|任意用户|完成|
|/v1.0/first/|POST|第一次开机奖励接口|注册用户|完成|
|/v1.0/trade/|POST|接收APP购买成功后返回的信息, 接口同 /me/trade/(别名) |注册用户|完成|
|/v1.0/bests/|GET|"惊" 字菜单的内容,返回两组数据<br/> goods, users|注册用户|完成|
|/v1.0/query/|GET|搜索商品接口|任意用户|完成|
|/v1.0/random/|POST|购买商品时候的随机数接口|任意用户|完成|
|/v1.0/search/|GET|商品列表数据接口|任意用户|完成|
|/v1.0/category/|GET|商品类别接口|任意用户|完成|
|/v1.0/feedback/|POST|用户中心反馈接口|注册用户|完成|
|/v1.0/location/|POST|用户地里位置接口|注册用户|完成|
|/v1.0/recommend/|GET|推荐商品接口|任意用户|完成|
|/v1.0/watchword/|POST|淘口令接口|注册用户|完成|

#### 客户端安装数据
> 客户端初次安装发送请求。

<!--|/v1.0/bootstrap/installations/{id}|PUT|更新安装数据|~|-->
<!--|/v1.0/bootstrap/installations/{pk}|GET|获取安装数据|高级用户|完成|-->

|URL|HTTP|功能|权限|进度|
|-|-|-|-|-|
|/v1.0/bootstrap/installations/|POST|上传安装数据|任意用户|完成|
|/v1.0/bootstrap/installations|GET|查询安装数据|高级用户|完成|
|/v1.0/bootstrap/pictures/|GET|开始显示图片|任意用户|完成|
|[/v1.0/bootstrap/upgrade/](http://bopo.me:8088/api/v1.0/bootstrap/pictures/)|GET|版本更新|任意用户|完成|

#### 各种排行榜

|URL|HTTP|功能|权限|进度|
|-|-|-|-|-|
|/v1.0/users/ranking/|GET|达人排行榜|任意用户|未测试|
|/v1.0/stars/ranking/|GET|明星排行榜|任意用户|未测试|

#### 文章部分，支持方法[GET,POST]

|URL|HTTP|功能|权限|进度|
|-|-|-|-|-|
|/v1.0/articles|GET|文章列表|认证用户|完成|
|/v1.0/articles|POST|发布文章|认证用户|缺文件上传|
|/v1.0/articles/{id}/|GET|文章详细|任意用户|完成|
