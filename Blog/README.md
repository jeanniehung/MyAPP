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
