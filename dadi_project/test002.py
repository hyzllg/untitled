'''
Created on 2016年7月7日
@author: Tommy
'''
import cx_Oracle
import yaml

class Oracle(object):
    """  oracle db operator  """

    def __init__(self, userName, password, host, instance):
        # 获取配置信息
        get_yaml_data = lambda path: yaml.load(open(path, encoding='utf-8'), Loader=yaml.SafeLoader)
        sit_oracle_conf = get_yaml_data('./conf/Config.yaml')["xshx_oracle"]["xsxb_sit_oracle"]
        self._conn = cx_Oracle.connect("%s/%s@%s/%s" % (userName, password, host, instance))
        self.cursor = self._conn.cursor()

    def queryTitle(self, sql, nameParams={}):
        if len(nameParams) > 0:
            self.cursor.execute(sql, nameParams)
        else:
            self.cursor.execute(sql)

        colNames = []
        for i in range(0, len(self.cursor.description)):
            colNames.append(self.cursor.description[i][0])

        return colNames

    # query methods
    def queryAll(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def queryOne(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def queryBy(self, sql, nameParams={}):
        if len(nameParams) > 0:
            self.cursor.execute(sql, nameParams)
        else:
            self.cursor.execute(sql)

        return self.cursor.fetchall()

    def insertBatch(self, sql, nameParams=[]):
        """batch insert much rows one time,use location parameter"""
        self.cursor.prepare(sql)
        self.cursor.executemany(None, nameParams)
        self.commit()

    def commit(self):
        self._conn.commit()

    def __del__(self):
        if hasattr(self, 'cursor'):
            self.cursor.close()

        if hasattr(self, '_conn'):
            self._conn.close()


def test1():
    # sql = """select user_name,user_real_name,to_char(create_date,'yyyy-mm-dd') create_date from sys_user where id = '10000' """
    sql = """select user_name,user_real_name,to_char(create_date,'yyyy-mm-dd') create_date from sys_user where id =: id """
    oraDb = Oracle('test', 'java', '192.168.0.192', 'orcl')

    fields = oraDb.queryTitle(sql, {'id': '10000'})
    print(fields)

    print(oraDb.queryBy(sql, {'id': '10000'}))


def test2():
    oraDb = Oracle('test', 'java', '192.168.0.192', 'orcl')
    cursor = oraDb.cursor

    create_table = """
    CREATE TABLE python_modules (
    module_name VARCHAR2(50) NOT NULL,
    file_path VARCHAR2(300) NOT NULL
    )
    """
    from sys import modules

    cursor.execute(create_table)
    M = []
    for m_name, m_info in modules.items():
        try:
            M.append((m_name, m_info.__file__))
        except AttributeError:
            pass

    sql = "INSERT INTO python_modules(module_name, file_path) VALUES (:1, :2)"
    oraDb.insertBatch(sql, M)

    cursor.execute("SELECT COUNT(*) FROM python_modules")
    print(cursor.fetchone())
    print('insert batch ok.')

    cursor.execute("DROP TABLE python_modules PURGE")


test2()