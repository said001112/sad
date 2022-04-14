import pymysql
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123')
# try:
#    connection.cursor().execute("""drop database my_db""")
# except:
#    pass
create = """create database my_db;
       use my_db;
       CREATE TABLE some_table( id INT NOT NULL AUTO_INCREMENT, some_text VARCHAR(255) NULL, PRIMARY KEY (`id`));"""
for element in create.split(';'):
    try:
        print(element)
        connection.cursor().execute(element)
        connection.commit()
    except:
        print("FALL IN" + str(element))
connection.close()
connect = pymysql.connect(host='localhost',
                        user='root',
                        password='123',
                        db='my_db',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor
                          )
with connect.cursor() as cursor:
    cursor.execute("""show tables""")
    print(cursor.fetchall())
    cursor.execute("""insert into some_table (some_text) value(123)""")
connect.commit()
with connect.cursor() as cursor:
    cursor.execute("""select * from some_table;""")
    print(cursor.fetchall())
connect.close()
