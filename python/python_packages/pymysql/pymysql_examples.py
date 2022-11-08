import pymysql

def show_tables(config):
    connection = pymysql.connect(**config)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SHOW TABLES") 

    # Read and print tables
    tables = cursor.fetchall()  
    for table in tables:
        for key, val in table.items():
            print(val)

if __name__ == '__main__':
    config = "INSERT YOUR CONFIGURATION"
    show_tables(config)
