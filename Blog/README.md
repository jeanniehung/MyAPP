### flask 
对于本地使用的不是app.py的文件，需要再环境里手动设置
```
1. 设置app
win: set FLASK_APP=view.py
mac: export FLASK_APP=view.py
2. 设置环境变量
win: $env:FLASK_APP = "view.py"
3. 启动程序
flask runview
```
4. debug模式
```
linux:
export FLASK_ENV=development
cmd:
set FLASK_ENV=developmetn
powershell:
$env:FLASK_ENV = "development"
```


### 使用flask.request 接收数据
request.form：用于接收表单参数
request.args：用于接收GET参数
request.json：用于接收JSON参数
request.values：获取所有参数（表单参数+GET参数）
request.file：用于接收文件

# https://cloud.tencent.com/developer/article/1560357

接口自动化
https://my.oschina.net/u/4404102/blog/4436766