import psycopg2
database = psycopg2.connect(database="test", user="user1", password="password", host="localhost", port="5432")
cursor = database.cursor()

def query(col_name):
    get_col_name = """SELECT %s FROM test WHERE id_count=2 GROUP BY %s """ % (col_name, col_name)
    cursor.execute(get_col_name)
    col_name_full = [item for t in cursor.fetchall() for item in t]
    # print(col_name_9)
    with open("data/statistics.txt", "a") as f:
        f.write(str(col_name_full))
        f.write("\n")
        f.close()

    query_data = """SELECT DISTINCT(%s) FROM test WHERE %s <> '' AND id_count > 3 """ % (col_name, col_name)
    cursor.execute(query_data)
    data = cursor.fetchall()
    data = [item for t in data for item in t]
    data = [el.replace("'", "''") for el in data]

    for el in data:
        cursor.execute("""SELECT %s,Count(*) FROM test WHERE %s='%s' GROUP BY %s """ % (col_name, col_name, el, col_name))
        rez = cursor.fetchall()
        # print(rez)
        with open("data/statistics.txt", "a") as f:
            f.write(str(rez))
            f.write("\n")
            f.close()

