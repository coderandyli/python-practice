# 第38课 数据库 日志系统
'''
    - mysqlclient不支持python3.9及以上版本，改用PyMySQL
'''
import pymysql


def test_pymysql():
    print("执行sql脚本")
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='ep000000',
        db='py_test'
    )

    cur = conn.cursor()
    # 执行建表语句
    cur.execute('''
            CREATE TABLE price (
                timestamp TIMESTAMP NOT NULL,
                BTCUSD FLOAT(8,2),
                PRIMARY KEY (timestamp)
            );
        ''')
    # 执行插入语句
    cur.execute('''
            INSERT INTO price VALUES(
                "2019-07-14 14:12:17",
                11234.56
            );
        ''')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    test_pymysql()