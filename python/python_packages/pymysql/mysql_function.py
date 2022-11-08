import pymysql.cursors 
import pandas as pd
import os

#mysql 접속을 위한 환경변수 불러오기
from dotenv import load_dotenv
load_dotenv()

config = { 'host':os.environ.get('host'),
            'port':int(os.environ.get('port')), 
            'user':os.environ.get('username'), 
            'password':os.environ.get('password'),
            'db':os.environ.get('database'),
            'cursorclass':pymysql.cursors.DictCursor}

def show_tables(config):
    '''
    pymysql을 활용하여 db에 있는 table 이름 리스트를 반환하는 함수
    '''
    connection = pymysql.connect(**config)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SHOW TABLES") 

    # Read and print tables
    tables = cursor.fetchall()  
    tb_list = list()
    for table in tables:
        for key, val in table.items():
            tb_list.append(val)
    return tb_list

def show_fields(config, tb):
    """
    유효한 mysql cofig와 테이블 이름을 넣으면 pymysql을 이용해 table의 필드 값을 리스트로 반환하는 함수
    """
    connection = pymysql.connect(**config)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(f"show fields from {tb}")
    return [f['Field'] for f in cursor.fetchall()]


def select_table(config, tb):
    '''
    유효한 mysql cofig와 테이블 이름을 넣으면 pymysql을 이용해 table 전체를 select 해서 df로 반환하는 함수
    '''
    # connection 변수 안에 pymysql.connect를 선언하고 connection 정보를 적어준다.
    connection = pymysql.connect(**config)

    # table 전체를  select해와서 dataframe 으로 만들기
    with connection: 
        with connection.cursor() as cursor: 
            sql = f"select * from {tb};" 
            cursor.execute(sql, ()) 
            tables = cursor.fetchall() 
            field_names = [i[0] for i in cursor.description]
            df = pd.DataFrame(data=tables, columns = field_names)
    return df


def sql_query(query, data=None):
    '''
    pymysql을 활용하여 db에 쿼리를 날리는 함수
    '''
    connection = pymysql.connect(**config)
    curs = connection.cursor(pymysql.cursors.DictCursor)
    if data==None:
        curs.execute(query)
    else:
        curs.execute(query, data)
    connection.commit()
    connection.close()
    return curs.fetchall()

