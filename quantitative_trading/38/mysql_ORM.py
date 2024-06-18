import numpy as np
import peewee
from peewee import *

db = MySQLDatabase(
    'py_test',
    user='root',
    password='ep000000',
    host='localhost',
    port=3306
)


class Price(peewee.Model):
    timestamp = peewee.DateTimeField(primary_key=True)
    BTCUSD = peewee.FloatField()

    class Meta:
        database = db


def test_peewee():
    # 建表
    # Price.create_table()

    # 插入
    # Price.create(timestamp='2022-12-07 13:17:18', BTCUSD='12345.67')

    # 查询
    priceList = Price.select()
    # print(type(priceList))
    BTCUSDList = []
    for price in priceList:
        print(price.timestamp, price.BTCUSD)
        BTCUSDList.append(price.BTCUSD)

    print(np.min(BTCUSDList), np.max(BTCUSDList))

    # 关闭数据库连接
    db.close()

if __name__ == '__main__':
    test_peewee()