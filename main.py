import psycopg2

from standart_query import query
from standart_query_title_2 import query_with_subtitle

database = psycopg2.connect(database="test", user="user1", password="password", host="localhost", port="5432")
cursor = database.cursor()

from standart_query_filtered import query_filter
from itertools import product



global all_data
all_data = []
for i in range(1, 96):
    rez = "col_"+str(i)
    query(rez)
    # from standart_query import data2
    # all_data.append(data2)

# rez = list(product(*all_data))
# print(rez)

# for j in range(len(rez)):
#     print("================", rez[j], "================")
#     for i in range(9, 97):
#         rez2 = "col_"+str(i)
#         result = query_filter(rez2, "col_1", rez[j][0],
#                               "col_2", rez[j][1],
#                               "col_3", rez[j][2],
#                               "col_4", rez[j][3],
#                               "col_5", rez[j][4],
#                               "col_6", rez[j][5])

# test query
# test_query = """SELECT DISTINCT("col_9") FROM test WHERE "col_9" <> '' AND id_count > 3 AND "col_1"=%s""" % ("'"+rez[0][0]+"'")

# cursor.execute(test_query)
# test = cursor.fetchall()
# print(test)






# query("col_1")
# from standart_query import data2
# print(data2)
#
# query("col_2")
# from standart_query import data2
# print(data2)
#
# query("col_3")
# from standart_query import data2
# print(data2)
#
# query("col_4")
# from standart_query import data2
# print(data2)
#
# query("col_5")
# from standart_query import data2
# print(data2)
#
# query("col_6")
# from standart_query import data2
# print(data2)
#
# query("col_7")
# from standart_query import data2
# print(data2)

# !!! COLUMN => 8 <= !!!
get_col_name_8 = """SELECT col_8 FROM test WHERE id_count=2 GROUP BY col_8"""
cursor.execute(get_col_name_8)
col_name_8 = [item for t in cursor.fetchall() for item in t]
# print(col_name_8)
with open("data/statistics.txt", "a") as f:
    f.write(str(col_name_8))
    f.write("\n")
    f.close()

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
# print(d)
with open("data/statistics.txt", "a") as f:
    f.write(str(d))
    f.write("\n")
    f.close()



# query("col_9")
# query("col_10")
# query("col_11")
# query("col_12")
# query("col_13")
# query("col_14")
# query("col_15")
# query("col_16")
# query("col_17")
# query("col_18")
# query("col_19")
# query("col_20")
# query("col_21")
# query("col_22")
# query_with_subtitle("col_23", "col_23")
# query_with_subtitle("col_23", "col_24")
# query_with_subtitle("col_23", "col_25")
# query_with_subtitle("col_23", "col_26")
# query_with_subtitle("col_23", "col_27")
# query_with_subtitle("col_23", "col_28")
# query_with_subtitle("col_23", "col_29")
# query_with_subtitle("col_23", "col_30")
# query_with_subtitle("col_23", "col_31")
# query_with_subtitle("col_23", "col_32")
# query_with_subtitle("col_23", "col_33")
# query_with_subtitle("col_34", "col_34")
# query_with_subtitle("col_34", "col_35")
# query_with_subtitle("col_34", "col_36")
# query_with_subtitle("col_34", "col_37")
# query_with_subtitle("col_34", "col_38")
# query_with_subtitle("col_34", "col_39")
# query_with_subtitle("col_34", "col_40")
# query_with_subtitle("col_34", "col_41")
# query_with_subtitle("col_34", "col_42")
# query_with_subtitle("col_34", "col_43")
# query_with_subtitle("col_34", "col_44")
# query_with_subtitle("col_45", "col_45")
# query_with_subtitle("col_45", "col_46")
# query_with_subtitle("col_45", "col_47")
# query_with_subtitle("col_45", "col_48")
# query_with_subtitle("col_45", "col_49")
# query_with_subtitle("col_45", "col_50")
# query_with_subtitle("col_45", "col_51")
# query_with_subtitle("col_45", "col_52")
# query_with_subtitle("col_45", "col_53")
# query_with_subtitle("col_45", "col_54")
# query_with_subtitle("col_45", "col_55")
# query_with_subtitle("col_56", "col_56")
# query_with_subtitle("col_56", "col_57")
# query_with_subtitle("col_56", "col_58")
# query_with_subtitle("col_56", "col_59")
# query_with_subtitle("col_56", "col_60")
# query_with_subtitle("col_56", "col_61")
# query_with_subtitle("col_56", "col_62")
# query_with_subtitle("col_56", "col_63")
# query_with_subtitle("col_56", "col_64")
# query_with_subtitle("col_56", "col_65")
# query_with_subtitle("col_56", "col_66")
# query_with_subtitle("col_67", "col_67")
# query_with_subtitle("col_67", "col_68")
# query_with_subtitle("col_67", "col_69")
# query_with_subtitle("col_67", "col_70")
# query_with_subtitle("col_67", "col_71")
# query_with_subtitle("col_67", "col_72")
# query_with_subtitle("col_67", "col_73")
# query_with_subtitle("col_67", "col_74")
# query_with_subtitle("col_75", "col_75")
# query_with_subtitle("col_75", "col_76")
# query_with_subtitle("col_75", "col_77")
# query_with_subtitle("col_75", "col_78")
# query_with_subtitle("col_75", "col_79")
# query_with_subtitle("col_75", "col_80")
# query_with_subtitle("col_75", "col_81")
# query_with_subtitle("col_75", "col_82")
# query_with_subtitle("col_75", "col_83")
# query_with_subtitle("col_75", "col_84")
# query_with_subtitle("col_85", "col_85")
# query_with_subtitle("col_85", "col_86")
# query_with_subtitle("col_85", "col_87")
# query_with_subtitle("col_85", "col_88")
# query_with_subtitle("col_85", "col_89")
# query_with_subtitle("col_85", "col_90")
# query_with_subtitle("col_85", "col_91")
# query_with_subtitle("col_85", "col_92")
# query_with_subtitle("col_85", "col_93")
# query_with_subtitle("col_85", "col_94")
# query("col_95")
# query("col_96")

# print(query_with_subtitle("col_85", "col_94"))
# from standart_query_title_2 import data
# print("data", data)


cursor.close()

database.commit()

database.close()

