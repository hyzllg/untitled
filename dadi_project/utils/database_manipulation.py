import cx_Oracle


#创建数据库操作类
class Oracle_Class:
    def __init__(self,user,passwd,listener):
        #创建数据库连接
        self.conn = cx_Oracle.connect(user, passwd, listener)
        #创建cursor
        self.cursor = self.conn.cursor()

    # 查询操作：一次性取所有数据。输入查询SQL，返回结果元组列表。
    def query_data(self, sql):
        list_result = []
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        for row in rows:
            list_result.append(row)
        return list_result

    # 支持对数据库的插入、更新和删除操作。输入操作SQL，无返回。
    def insert_update_data(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    #批量插入数据
    def batch_insert(self,masterplate,list_datas):
        #masterplate sql批量插入模版
        #list_datas 列表，里面放元组，每个元组里面放基于模版的对应数据
        self.cursor.prepare(masterplate)
        self.cursor.executemany(None, list_datas)
        self.conn.commit()

    # 关闭连接，释放资源
    def close_all(self):
        self.cursor.close()
        self.conn.close()
