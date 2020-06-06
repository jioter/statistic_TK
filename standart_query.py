import psycopg2
import openpyxl
import os.path

database = psycopg2.connect(database="test", user="user1", password="password", host="localhost", port="5432")
cursor = database.cursor()


def query(col_name):
    # if no such file -> create it
    if not os.path.isfile("data/statistics_calculated.xlsx"):
        book = openpyxl.Workbook()
        book.save("data/statistics_calculated.xlsx")

    #  SELECT column name & subcolumn_name
    get_col_name = """SELECT %s FROM test WHERE id_count=2 GROUP BY %s """ % (col_name, col_name)
    cursor.execute(get_col_name)
    col_name_full = [item for t in cursor.fetchall() for item in t]

    get_sub_col_name = """SELECT %s FROM test WHERE id_count=3 GROUP BY %s """ % (col_name, col_name)
    cursor.execute(get_sub_col_name)
    sub_col_name_full = [item for t in cursor.fetchall() for item in t]

    #  Check if column name is not empty.
    if not col_name_full == ['']:
        book = openpyxl.load_workbook("data/statistics_calculated.xlsx")
        sheet = book.active
        sheet.append(col_name_full)
        book.save("data/statistics_calculated.xlsx")
    if not sub_col_name_full == ['']:
        book = openpyxl.load_workbook("data/statistics_calculated.xlsx")
        sheet = book.active
        sheet.append(sub_col_name_full)
        book.save("data/statistics_calculated.xlsx")

        # print(col_name_full)
        # with open("data/statistics.txt", "a") as f:
        #     f.write(str(col_name_full))
        #     f.write("\n")
        #     f.close()

    #SELECT distinct data and GROUP & COUNT values
    query_data = """SELECT DISTINCT(%s) FROM test WHERE %s <> '' AND id_count > 3 """ % (col_name, col_name)
    cursor.execute(query_data)
    global data2
    data2 = cursor.fetchall()
    data2 = [item for t in data2 for item in t]
    data2 = [el.replace("'", "''") for el in data2]

    for el in data2:
        cursor.execute("""SELECT %s,Count(*) FROM test WHERE %s='%s' GROUP BY %s """ % (col_name, col_name, el, col_name))
        rez = cursor.fetchall()

        print(rez)
        # with open("data/statistics.txt", "a") as f:
        #     f.write(str(rez))
        #     f.write("\n")
        #     f.close()

        book = openpyxl.load_workbook("data/statistics_calculated.xlsx")
        sheet = book.active
        sheet.append(rez[0])
        book.save("data/statistics_calculated.xlsx")

