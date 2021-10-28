import cx_Oracle


class DatabaseManipulation:
    def sql_cha(self,cursor, my_sql):
        try:
            # 创建oracle连接
            # conns = cx_Oracle.connect(conf[0], conf[1], conf[2])
            # cursor = conns.cursor()
            # 执行sql
            cursor.execute(my_sql)
            all_data = cursor.fetchall()
            oo = list(all_data)
            # cursor.close()
            return oo
        except cx_Oracle.DatabaseError:
            return print("无效的SQL语句")

    def sql_update(self,setting, v, vv):
        try:
            conns = cx_Oracle.connect(setting[0], setting[1], setting[2])
            cursor = conns.cursor()
            my_sql_c = "UPDATE system_setup SET businessdate = :v,batchdate = :vv".format()
            cursor.execute(my_sql_c, {'v': v, 'vv': vv})
            conns.commit()  # 这里一定要commit才行，要不然数据是不会插入的
            conns.close()
            print("核心数据库时间更改成功  {}".format(v))

        except cx_Oracle.DatabaseError:
            return print("无效的SQL语句")
