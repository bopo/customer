商品相关（The Goods）
===

|Version| 1.0.0|
|-
|Author| [`BoPo <http://bopo.me>`](http://bopo.me)|

> 首次撰写：2015-09-02

> 最后修改：-

> 注意：关于api的GET参数说明，api后面跟随的`{pk}`或者`{id}` 是一个意思，代表改资源(`resource`)的主键.

### 接口列表如下:

#### 品牌数据

| URL | HTTP | 功能 | 权限 |进度|
| --- | --- | ---- | --- |-|
| /v1.0/brands|GET|获得品牌列表数据|任意用户|完成|
| /v1.0/brands/{id}|GET|获取单个品牌详细信息|任意用户|完成|
| /v1.0/brands/categories|GET|获取品牌分类列表|任意用户|完成|
| /v1.0/brands/categories/{id}|GET|获取单个品牌分类详情|任意用户|完成|

#### 商品数据

| URL | HTTP | 功能 |  权限 |进度|
| --- | --- | --- |  -- |-|
| /v1.0/goods | GET | 获得明星列表数据 |任意用户|完成|
| /v1.0/goods/{id}|GET|获取单个明星详细信息<br>recommend参数：1.未知，2推荐，3未推荐 |任意用户|完成|
| /v1.0/goods/categories|GET|获取明星分类列表 |任意用户|完成|
| /v1.0/goods/categories/{id}|GET| 获取单个明星分类详情|任意用户|完成|
