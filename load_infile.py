import pymysql


def get_conn(db):
    global conn
    conn = pymysql.connect(host="localhost", port=3306, user='root', passwd='122089', db=db, charset='utf8')
    global cur
    cur = conn.cursor()


def load_csv(csv_file_path, table_name, database):
    file = open(csv_file_path, 'r', encoding='utf-8')
    reader = file.readline()
    b = reader.split(',')
    column = ''
    for a in b:
        column = column + a + ' varchar(255),'
    column = column[:-1]
    create_sql = 'create table if not exists ' + table_name + '' + '(' + column + ')' + ' DEFAULT CHARSET=UTF8'
    data_sql = """load data infile '{0}' into table {1} fields terminated by "," enclosed by '"' lines terminated by '\\r\\n' ignore 1 lines""".format(
        csv_file_path, table_name)
    cur.execute('use {}'.format(database))
    cur.execute('SET NAMES utf8;')
    cur.execute('SET character_set_connection=utf8;')
    cur.execute(create_sql)
    cur.execute(data_sql)
    conn.commit()
    conn.close()
    cur.close()


if __name__ == '__main__':
    get_conn("movies")
    load_csv("D:\\\\python\\\\py\\\\movies.csv", table_name="fm_list", database="movies")
