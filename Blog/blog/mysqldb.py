import pymysql


class MysqlDb(object):

    def __init__(self, host, port, user, passwd, db):
        # 建立数据库连接
        self.conn = pymysql.connect(
            host=host, 
            port=port,
            user=user,
            passwd=passwd,
            db=db
        )
        # 创建游标，并让查询结果以字典的形式输出
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
    
    def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作
        # 关闭游标
        self.cur.close()
        # 关闭连接
        self.conn.close()

    def select_db(self, sql):
        """查询"""
        # 检查连接是否断开，如果断开就进行重连
        self.conn.ping(reconnect=True)
        # 使用execute() 执行sql
        self.cur.execute(sql)
        # 使用fetchall() 获取查询结果
        data = self.cur.fetchall()
        return data
    
    def execute_db(self, sql):
        """变更/新增/删除"""
        try:
            # 检查连接是否断开，如果断开就进行重连
            self.conn.ping(reconnect=True)
            # 使用execute() 执行sql
            self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            print('操作数显错误， {}'.format(e))
            # 回滚所有更改
            self.conn.rollback()


