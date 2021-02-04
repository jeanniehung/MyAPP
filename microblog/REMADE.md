### 创建数据库迁移存储库
```shell
flask db init
```
### 第一次数据迁移
```shell
flask db migrate -m "users table"
flask db migrate -m "posts table"

```
### flask db migrate命令不会对数据库进行任何更改，只会生成迁移脚本。 要将更改应用到数据库，必须使用flask db upgrade命令
```shell
flask db upgrade
```


### 为Flask_Login准备用户模型
Flask-Login插件需要在用户模型上实现某些属性和方法。这种做法很棒，因为只要将这些必需项添加到模型中，Flask-Login就没有其他依赖了，它就可以与基于任何数据库系统的用户模型一起工作。

必须的四项如下：

is_authenticated: 一个用来表示用户是否通过登录认证的属性，用True和False表示。
is_active: 如果用户账户是活跃的，那么这个属性是True，否则就是False（译者注：活跃用户的定义是该用户的登录状态是否通过用户名密码登录，通过“记住我”功能保持登录状态的用户是非活跃的）。
is_anonymous: 常规用户的该属性是False，对特定的匿名用户是True。
get_id(): 返回用户的唯一id的方法，返回值类型是字符串(Python 2下返回unicode字符串).