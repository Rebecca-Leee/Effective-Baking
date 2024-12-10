
import pandas as pd
import streamlit as st
import pymysql
from sqlalchemy import create_engine, text

def get_sql_engine():
    # 数据库
    mysql_config = {
        "db": "effective_baking",
        "host": "mysql.sqlpub.com",
        "user": "rebecca_leee",
        "password": "8p8cMQhcstwVg4q5",
        "port": 3306,
    }
    engine = create_engine(
        "mysql+pymysql://{}:{}@{}:{}/{}".format(mysql_config['user'], mysql_config['password'], mysql_config['host'],
                                                mysql_config['port'], mysql_config['db']))
    return engine

st.title('database test')

# 连接到MySQL数据库
conn = pymysql.connect(host='mysql.sqlpub.com', user='rebecca_leee', password='8p8cMQhcstwVg4q5', db='effective_baking')
 
# 创建一个Cursor:
cursor = conn.cursor()
 
# 执行一条SQL查询语句:
cursor.execute("SELECT VERSION()")
 
# 关闭Cursor和Connection:
cursor.close()
conn.close()

engine = get_sql_engine()


# data = {"a":[1,2],"b":["x","y"]}
df = pd.read_sql_query(text('select * from test_df'), con=engine.connect())


df_edit = st.data_editor(df)

df_edit.to_sql('test_df', con=engine, if_exists='replace', index=False)

test = pd.read_sql_query(text('select * from test_df'), con=engine.connect())
st.write(test.head())