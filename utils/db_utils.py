import pymysql

from utils.yaml_utils import open_yaml


def get_connect():
    """
    连接数据库
    :return:
    """
    db_info = open_yaml('test.yaml')['db_config']
    conn = pymysql.connect(host=db_info['host'], port=db_info['port'],
                           user=db_info['user'], password=db_info['password'],
                           database=db_info['database'], charset=db_info['charset'])
    return conn


def excute_sql(sql):
    connect = get_connect()
    cursor = connect.cursor()
    cursor.execute(sql)
    record = cursor.fetchall()
    # record = cursor.fetchone()
    return record

# print(excute_sql("select * from student_info"))
