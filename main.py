import openpyxl
import psycopg2

from standart_query import query
from standart_query_filtered import query_filter
from itertools import product


database = psycopg2.connect(database="test", user="user1", password="password", host="localhost", port="5432")
cursor = database.cursor()



global all_data
all_data = []
for i in range(1, 7):
    rez = "col_"+str(i)
    query(rez)

    from standart_query import data2
    all_data.append(data2)

rez = list(product(*all_data))
print(rez)


for j in range(len(rez)):
    print("================", rez[j], "================")
    book = openpyxl.load_workbook("data/statistics_calculated.xlsx")
    sheet = book.active
    visual_separator = ["================"]
    sheet.append(visual_separator)
    sheet.append(rez[j])
    sheet.append(visual_separator)
    book.save("data/statistics_calculated.xlsx")
    for i in range(7, 97):
        rez2 = "col_"+str(i)
        result = query_filter(rez2, "col_1", rez[j][0],
                              "col_2", rez[j][1],
                              "col_3", rez[j][2],
                              "col_4", rez[j][3],
                              "col_5", rez[j][4],
                              "col_6", rez[j][5])

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


cursor.close()

database.commit()

database.close()

