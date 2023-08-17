import pymysql
from pymysql import cursors

from utils.log_utils import logger
from utils.yaml_utils import open_yaml


def get_connect():
    """
    连接数据库
    :return:
    """
    db_info = open_yaml('test.yaml')['db_config']
    conn = pymysql.connect(host=db_info['host'], port=db_info['port'],
                           user=db_info['user'], password=db_info['password'],
                           database=db_info['database'], charset=db_info['charset'],
                           cursorclass=cursors.DictCursor)
    conn.autocommit(True)
    return conn


def excute_sql(sql):
    '''
    :param sql: 待执行的SQL语句
    :return:
    '''
    try:
        connect = get_connect()
        cursor = connect.cursor()
        cursor.execute(sql)
        record = cursor.fetchall()
        cursor.close()
        connect.close()
        if len(record) == 1:
            return record[0]
        elif len(record) == 0:
            return None
        else:
            return record
    except Exception as e:
        logger.error(e)
        return e

# print(excute_sql("select * from student_info where student_name='winnie'"))

# res = excute_sql("select * from student_info where student_name='winnie'")
# print(res)
# 添加语句
# print(excute_sql("insert into student_info(student_name) values('test')"))
# 删除语句
# print(excute_sql("delete from student_info where id=7"))
# 修改语句
# print(excute_sql("update student_info set student_name='hi' where student_name='hello'"))
# # 查询语句
# print(excute_sql("select * from student_info"))