import psycopg2
database = psycopg2.connect(database="test", user="user1", password="password", host="localhost", port="5432")
cursor = database.cursor()

def query(col_name):
    get_col_name_9 = """SELECT %s FROM test WHERE id_count=2 GROUP BY %s """ % (col_name, col_name)
    cursor.execute(get_col_name_9)
    col_name_9 = [item for t in cursor.fetchall() for item in t]
    print(col_name_9)


    query9 = """SELECT DISTINCT(%s) FROM test WHERE %s <> '' AND id_count > 3 """ % (col_name, col_name)
    cursor.execute(query9)
    records9 = cursor.fetchall()
    records9 = [item for t in records9 for item in t]
    records9 = [el.replace("'","''") for el in records9]

    for el in records9:
        cursor.execute("""SELECT %s,Count(*) FROM test WHERE %s='%s' GROUP BY %s """ % (col_name, col_name, el, col_name))
        print(cursor.fetchall())