import os
import sys
from blog.config.setting import SERVER_PORT
from blog.view import app
from blog.api import app
from blog.manage import app


# 项目根路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_PATH)  # 将项目根路径临时加入环境变量，程序退出后失效

if __name__ == '__main__':
    # host为主机ip地址，port指定访问端口号，debug=True设置调试模式打开
    app.run(host="127.0.0.1", port=SERVER_PORT, debug=True)
