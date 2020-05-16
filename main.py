from pprint import pprint
import psycopg2

database = psycopg2.connect(database="postgres", user="user1", password="password", host="localhost", port="5432")
cursor = database.cursor()

### !!! COLUMN => 1 <= !!! ###


get_col_name = """SELECT col_1 FROM test WHERE id_count=2 GROUP BY col_1"""
cursor.execute(get_col_name)
col_name = [item for t in cursor.fetchall() for item in t]
print(col_name)


query1 = """SELECT DISTINCT(col_1) FROM test WHERE col_1 <> '' AND id_count > 3 """

cursor.execute(query1)
records1 = cursor.fetchall()
# print(records1)

for el in records1:
    cursor.execute("""SELECT col_1,Count(*) FROM test WHERE col_1='%s' GROUP BY col_1""" % el)
    print(cursor.fetchall())

### !!! COLUMN => 2 <= !!! ###
get_col_name_2 = """SELECT col_2 FROM test WHERE id_count=2 GROUP BY col_2"""
cursor.execute(get_col_name_2)
col_name_2 = [item for t in cursor.fetchall() for item in t]
print(col_name_2)


query2 = """SELECT DISTINCT(col_2) FROM test WHERE col_2 <> '' AND id_count > 3 """

cursor.execute(query2)
records2 = cursor.fetchall()
# pprint(records2)

for el in records2:
    cursor.execute("""SELECT col_2,Count(*) FROM test WHERE col_2='%s' GROUP BY col_2""" % el)
    print(cursor.fetchall())

### !!! COLUMN => 3 <= !!! ###
get_col_name_3 = """SELECT col_3 FROM test WHERE id_count=2 GROUP BY col_3"""
cursor.execute(get_col_name_3)
col_name_3 = [item for t in cursor.fetchall() for item in t]
print(col_name_3)


query3 = """SELECT DISTINCT(col_3) FROM test WHERE col_3 <> '' AND id_count > 3 """

cursor.execute(query3)
records3 = cursor.fetchall()
records3 = [item for t in records3 for item in t]
records3 = [el.replace("'","''") for el in records3]

for el in records3:
    cursor.execute("""SELECT col_3,Count(*) FROM test WHERE col_3='%s' GROUP BY col_3""" % el)
    print(cursor.fetchall())


cursor.close()

database.commit()

database.close()

