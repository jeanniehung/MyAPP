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