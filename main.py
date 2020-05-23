from pprint import pprint
import psycopg2

from standart_query import query
from standart_query_title_2 import query_with_subtitle

database = psycopg2.connect(database="test", user="user1", password="password", host="localhost", port="5432")
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

### !!! COLUMN => 4 <= !!! ###
get_col_name_4 = """SELECT col_4 FROM test WHERE id_count=2 GROUP BY col_4"""
cursor.execute(get_col_name_4)
col_name_4 = [item for t in cursor.fetchall() for item in t]
print(col_name_4)


query4 = """SELECT DISTINCT(col_4) FROM test WHERE col_4 <> '' AND id_count > 3 """
cursor.execute(query4)
records4 = cursor.fetchall()
records4 = [item for t in records4 for item in t]
records4 = [el.replace("'","''") for el in records4]

for el in records4:
    cursor.execute("""SELECT col_4,Count(*) FROM test WHERE col_4='%s' GROUP BY col_4""" % el)
    print(cursor.fetchall())

### !!! COLUMN => 5 <= !!! ###
get_col_name_5 = """SELECT col_5 FROM test WHERE id_count=2 GROUP BY col_5"""
cursor.execute(get_col_name_5)
col_name_5 = [item for t in cursor.fetchall() for item in t]
print(col_name_5)


query5 = """SELECT DISTINCT(col_5) FROM test WHERE col_5 <> '' AND id_count > 3 """
cursor.execute(query5)
records5 = cursor.fetchall()
records5 = [item for t in records5 for item in t]
records5 = [el.replace("'","''") for el in records5]

for el in records5:
    cursor.execute("""SELECT col_5,Count(*) FROM test WHERE col_5='%s' GROUP BY col_5""" % el)
    print(cursor.fetchall())

### !!! COLUMN => 6 <= !!! ###
get_col_name_6 = """SELECT col_6 FROM test WHERE id_count=2 GROUP BY col_6"""
cursor.execute(get_col_name_6)
col_name_6 = [item for t in cursor.fetchall() for item in t]
print(col_name_6)


query6 = """SELECT DISTINCT(col_6) FROM test WHERE col_6 <> '' AND id_count > 3 """
cursor.execute(query6)
records6 = cursor.fetchall()
records6 = [item for t in records6 for item in t]
records6 = [el.replace("'","''") for el in records6]

for el in records6:
    cursor.execute("""SELECT col_6,Count(*) FROM test WHERE col_6='%s' GROUP BY col_6""" % el)
    print(cursor.fetchall())

### !!! COLUMN => 7 <= !!! ###
get_col_name_7 = """SELECT col_7 FROM test WHERE id_count=2 GROUP BY col_7"""
cursor.execute(get_col_name_7)
col_name_7 = [item for t in cursor.fetchall() for item in t]
print(col_name_7)


query7 = """SELECT DISTINCT(col_7) FROM test WHERE col_7 <> '' AND id_count > 3 """
cursor.execute(query7)
records7 = cursor.fetchall()
records7 = [item for t in records7 for item in t]
records7 = [el.replace("'","''") for el in records7]

for el in records7:
    cursor.execute("""SELECT col_7,Count(*) FROM test WHERE col_7='%s' GROUP BY col_7""" % el)
    print(cursor.fetchall())

### !!! COLUMN => 8 <= !!! ###
get_col_name_8 = """SELECT col_8 FROM test WHERE id_count=2 GROUP BY col_8"""
cursor.execute(get_col_name_8)
col_name_8 = [item for t in cursor.fetchall() for item in t]
print(col_name_8)

query8 = """SELECT DISTINCT(col_8) FROM test WHERE col_8 <> '' AND id_count > 3 AND col_8 NOT IN ('-') """
cursor.execute(query8)
records8 = cursor.fetchall()
records8 = [item for t in records8 for item in t]
records8 = [el.replace("'","''") for el in records8]

# split elements in sublists
rez = [el.split(',') for el in records8]
# transform to flat list
flat_list = [item for sublist in rez for item in sublist]
# remove whitespaces
flat_list_2 = []
for el in flat_list:
    flat_list_2.append(" ".join(el.split()))
flat_list_2 = sorted(flat_list_2)
# count Countries
d = {}
for el in flat_list_2:
    if el not in d:
        d[el] = 1
    else:
        d[el] += 1
print(d)

### !!! COLUMN => 9 <= !!! ###
get_col_name_9 = """SELECT col_9 FROM test WHERE id_count=2 GROUP BY col_9"""
cursor.execute(get_col_name_9)
col_name_9 = [item for t in cursor.fetchall() for item in t]
print(col_name_9)


query9 = """SELECT DISTINCT(col_9) FROM test WHERE col_9 <> '' AND id_count > 3 """
cursor.execute(query9)
records9 = cursor.fetchall()
records9 = [item for t in records9 for item in t]
records9 = [el.replace("'","''") for el in records9]

for el in records9:
    cursor.execute("""SELECT col_9,Count(*) FROM test WHERE col_9='%s' GROUP BY col_9""" % el)
    print(cursor.fetchall())

query("col_10")
query("col_11")
query("col_12")
query("col_13")
query("col_14")
query("col_15")
query("col_16")
query("col_17")
query("col_18")
query("col_19")
query("col_20")
query("col_21")
query("col_22")
query_with_subtitle("col_23", "col_23")
query_with_subtitle("col_23", "col_24")
query_with_subtitle("col_23", "col_25")
query_with_subtitle("col_23", "col_26")
query_with_subtitle("col_23", "col_27")
query_with_subtitle("col_23", "col_28")
query_with_subtitle("col_23", "col_29")
query_with_subtitle("col_23", "col_30")
query_with_subtitle("col_23", "col_31")
query_with_subtitle("col_23", "col_32")
query_with_subtitle("col_23", "col_33")
query_with_subtitle("col_34", "col_34")
query_with_subtitle("col_34", "col_35")
query_with_subtitle("col_34", "col_36")
query_with_subtitle("col_34", "col_37")
query_with_subtitle("col_34", "col_38")
query_with_subtitle("col_34", "col_39")
query_with_subtitle("col_34", "col_40")
query_with_subtitle("col_34", "col_41")
query_with_subtitle("col_34", "col_42")
query_with_subtitle("col_34", "col_43")
query_with_subtitle("col_34", "col_44")
query_with_subtitle("col_45", "col_45")
query_with_subtitle("col_45", "col_46")
query_with_subtitle("col_45", "col_47")
query_with_subtitle("col_45", "col_48")
query_with_subtitle("col_45", "col_49")
query_with_subtitle("col_45", "col_50")
query_with_subtitle("col_45", "col_51")
query_with_subtitle("col_45", "col_52")
query_with_subtitle("col_45", "col_53")
query_with_subtitle("col_45", "col_54")
query_with_subtitle("col_45", "col_55")
query_with_subtitle("col_56", "col_56")
query_with_subtitle("col_56", "col_57")
query_with_subtitle("col_56", "col_58")
query_with_subtitle("col_56", "col_59")
query_with_subtitle("col_56", "col_60")
query_with_subtitle("col_56", "col_61")
query_with_subtitle("col_56", "col_62")
query_with_subtitle("col_56", "col_63")
query_with_subtitle("col_56", "col_64")
query_with_subtitle("col_56", "col_65")
query_with_subtitle("col_56", "col_66")
query_with_subtitle("col_67", "col_67")
query_with_subtitle("col_67", "col_68")
query_with_subtitle("col_67", "col_69")
query_with_subtitle("col_67", "col_70")
query_with_subtitle("col_67", "col_71")
query_with_subtitle("col_67", "col_72")
query_with_subtitle("col_67", "col_73")
query_with_subtitle("col_67", "col_74")
query_with_subtitle("col_75", "col_75")
query_with_subtitle("col_75", "col_76")
query_with_subtitle("col_75", "col_77")
query_with_subtitle("col_75", "col_78")
query_with_subtitle("col_75", "col_79")
query_with_subtitle("col_75", "col_80")
query_with_subtitle("col_75", "col_81")
query_with_subtitle("col_75", "col_82")
query_with_subtitle("col_75", "col_83")
query_with_subtitle("col_75", "col_84")
query_with_subtitle("col_85", "col_85")
query_with_subtitle("col_85", "col_86")
query_with_subtitle("col_85", "col_87")
query_with_subtitle("col_85", "col_88")
query_with_subtitle("col_85", "col_89")
query_with_subtitle("col_85", "col_90")
query_with_subtitle("col_85", "col_91")
query_with_subtitle("col_85", "col_92")
query_with_subtitle("col_85", "col_93")
query_with_subtitle("col_85", "col_94")
query("col_95")
query("col_96")



cursor.close()

database.commit()

database.close()

