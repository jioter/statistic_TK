import sqlite3
from sqlite3 import Error

import xlrd

# take sheet name
xls = xlrd.open_workbook(r'data/statistics.xlsx', on_demand=True)

# try except
book = xlrd.open_workbook("data/statistics.xlsx")
sheet = book.sheet_by_name(xls.sheet_names()[0])

try:
    conn = sqlite3.connect(r"data/statistic_db.db")
except Error as e:
    print(e)

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS test (
 id_count INTEGER PRIMARY KEY,
 record_number VARCHAR,
 COL_1 VARCHAR,
 COL_2 VARCHAR,
 COL_3 VARCHAR,
 COL_4 VARCHAR,
 COL_5 VARCHAR,
 COL_6 VARCHAR,
 COL_7 VARCHAR,
 COL_8 VARCHAR,
 COL_9 VARCHAR,
 COL_10 VARCHAR,
 COL_11 VARCHAR,
 COL_12 VARCHAR,
 COL_13 VARCHAR,
 COL_14 VARCHAR,
 COL_15 VARCHAR,
 COL_16 VARCHAR,
 COL_17 VARCHAR,
 COL_18 VARCHAR,
 COL_19 VARCHAR,
 COL_20 VARCHAR,
 COL_21 VARCHAR,
 COL_22 VARCHAR,
 COL_23 VARCHAR,
 COL_24 VARCHAR,
 COL_25 VARCHAR,
 COL_26 VARCHAR,
 COL_27 VARCHAR,
 COL_28 VARCHAR,
 COL_29 VARCHAR,
 COL_30 VARCHAR,
 COL_31 VARCHAR,
COL_32  VARCHAR,
COL_33 VARCHAR,
COL_34 VARCHAR,
COL_35 VARCHAR,
COL_36 VARCHAR,
COL_37 VARCHAR,
COL_38 VARCHAR,
COL_39 VARCHAR,
COL_40 VARCHAR,
COL_41 VARCHAR,
COL_42 VARCHAR,
COL_43 VARCHAR,
COL_44 VARCHAR,
COL_45 VARCHAR,
COL_46 VARCHAR,
COL_47 VARCHAR,
COL_48 VARCHAR,
COL_49 VARCHAR,
COL_50 VARCHAR,
COL_51 VARCHAR,
COL_52 VARCHAR,
COL_53 VARCHAR,
COL_54 VARCHAR,
COL_55 VARCHAR,
COL_56 VARCHAR,
COL_57 VARCHAR,
COL_58 VARCHAR,
COL_59 VARCHAR,
COL_60 VARCHAR,
COL_61 VARCHAR,
COL_62 VARCHAR,
COL_63 VARCHAR,
COL_64 VARCHAR,
COL_65 VARCHAR,
COL_66 VARCHAR,
COL_67 VARCHAR,
COL_68 VARCHAR,
COL_69 VARCHAR,
COL_70 VARCHAR,
COL_71 VARCHAR,
COL_72 VARCHAR,
COL_73 VARCHAR,
COL_74 VARCHAR,
COL_75 VARCHAR,
COL_76 VARCHAR,
COL_77 VARCHAR,
COL_78 VARCHAR,
COL_79 VARCHAR,
COL_80 VARCHAR,
COL_81 VARCHAR,
COL_82 VARCHAR,
COL_83 VARCHAR,
COL_84 VARCHAR,
COL_85 VARCHAR,
COL_86 VARCHAR,
COL_87 VARCHAR,
COL_88 VARCHAR,
COL_89 VARCHAR,
COL_90 VARCHAR,
COL_91 VARCHAR,
COL_92 VARCHAR,
COL_93 VARCHAR,
COL_94 VARCHAR,
COL_95 VARCHAR,
COL_96 VARCHAR
);""")

query_setup = """INSERT INTO test(record_number, COL_1, COL_2, COL_3, COL_4, COL_5, COL_6, COL_7, COL_8, COL_9,
              COL_10, COL_11, COL_12, COL_13, COL_14, COL_15, COL_16, COL_17, COL_18,
              COL_19, COL_20, COL_21, COL_22, COL_23, COL_24, COL_25, COL_26, COL_27,
              COL_28, COL_29, COL_30, COL_31, COL_32, COL_33, COL_34,
              COL_35, COL_36, COL_37, COL_38, COL_39, COL_40, COL_41, COL_42, COL_43,
              COL_44, COL_45, COL_46, COL_47, COL_48, COL_49, COL_50, COL_51, COL_52,
              COL_53, COL_54, COL_55, COL_56, COL_57, COL_58, COL_59, COL_60, COL_61,
              COL_62, COL_63, COL_64, COL_65, COL_66, COL_67, COL_68, COL_69, COL_70,
              COL_71, COL_72, COL_73, COL_74, COL_75, COL_76, COL_77, COL_78, COL_79,
              COL_80, COL_81, COL_82, COL_83, COL_84, COL_85, COL_86, COL_87, COL_88,
              COL_89, COL_90, COL_91, COL_92, COL_93, COL_94, COL_95, COL_96) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
              ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
              ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
              ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

for r in range(1, sheet.nrows):
    record_number = str(sheet.cell(r, 0).value)
    COL_1 = str(sheet.cell(r, 1).value)
    COL_2 = str(sheet.cell(r, 2).value)
    COL_3 = str(sheet.cell(r, 3).value)
    COL_4 = str(sheet.cell(r, 4).value)
    COL_5 = str(sheet.cell(r, 5).value)
    COL_6 = str(sheet.cell(r, 6).value)
    COL_7 = str(sheet.cell(r, 7).value)
    COL_8 = str(sheet.cell(r, 8).value)
    COL_9 = str(sheet.cell(r, 9).value)
    COL_10 = str(sheet.cell(r, 10).value)
    COL_11 = str(sheet.cell(r, 11).value)
    COL_12 = str(sheet.cell(r, 12).value)
    COL_13 = str(sheet.cell(r, 13).value)
    COL_14 = str(sheet.cell(r, 14).value)
    COL_15 = str(sheet.cell(r, 15).value)
    COL_16 = str(sheet.cell(r, 16).value)
    COL_17 = str(sheet.cell(r, 17).value)
    COL_18 = str(sheet.cell(r, 18).value)
    COL_19 = str(sheet.cell(r, 19).value)
    COL_20 = str(sheet.cell(r, 20).value)
    COL_21 = str(sheet.cell(r, 21).value)
    COL_22 = str(sheet.cell(r, 22).value)
    COL_23 = str(sheet.cell(r, 23).value)
    COL_24 = str(sheet.cell(r, 24).value)
    COL_25 = str(sheet.cell(r, 25).value)
    COL_26 = str(sheet.cell(r, 26).value)
    COL_27 = str(sheet.cell(r, 27).value)
    COL_28 = str(sheet.cell(r, 28).value)
    COL_29 = str(sheet.cell(r, 29).value)
    COL_30 = str(sheet.cell(r, 30).value)
    COL_31 = str(sheet.cell(r, 31).value)
    COL_32 = str(sheet.cell(r, 32).value)
    COL_33 = str(sheet.cell(r, 33).value)
    COL_34 = str(sheet.cell(r, 34).value)
    COL_35 = str(sheet.cell(r, 35).value)
    COL_36 = str(sheet.cell(r, 36).value)
    COL_37 = str(sheet.cell(r, 37).value)
    COL_38 = str(sheet.cell(r, 38).value)
    COL_39 = str(sheet.cell(r, 39).value)
    COL_40 = str(sheet.cell(r, 40).value)
    COL_41 = str(sheet.cell(r, 41).value)
    COL_42 = str(sheet.cell(r, 42).value)
    COL_43 = str(sheet.cell(r, 43).value)
    COL_44 = str(sheet.cell(r, 44).value)
    COL_45 = str(sheet.cell(r, 45).value)
    COL_46 = str(sheet.cell(r, 46).value)
    COL_47 = str(sheet.cell(r, 47).value)
    COL_48 = str(sheet.cell(r, 48).value)
    COL_49 = str(sheet.cell(r, 49).value)
    COL_50 = str(sheet.cell(r, 50).value)
    COL_51 = str(sheet.cell(r, 51).value)
    COL_52 = str(sheet.cell(r, 52).value)
    COL_53 = str(sheet.cell(r, 53).value)
    COL_54 = str(sheet.cell(r, 54).value)
    COL_55 = str(sheet.cell(r, 55).value)
    COL_56 = str(sheet.cell(r, 56).value)
    COL_57 = str(sheet.cell(r, 57).value)
    COL_58 = str(sheet.cell(r, 58).value)
    COL_59 = str(sheet.cell(r, 59).value)
    COL_60 = str(sheet.cell(r, 60).value)
    COL_61 = str(sheet.cell(r, 61).value)
    COL_62 = str(sheet.cell(r, 62).value)
    COL_63 = str(sheet.cell(r, 63).value)
    COL_64 = str(sheet.cell(r, 64).value)
    COL_65 = str(sheet.cell(r, 65).value)
    COL_66 = str(sheet.cell(r, 66).value)
    COL_67 = str(sheet.cell(r, 67).value)
    COL_68 = str(sheet.cell(r, 68).value)
    COL_69 = str(sheet.cell(r, 69).value)
    COL_70 = str(sheet.cell(r, 70).value)
    COL_71 = str(sheet.cell(r, 71).value)
    COL_72 = str(sheet.cell(r, 72).value)
    COL_73 = str(sheet.cell(r, 73).value)
    COL_74 = str(sheet.cell(r, 74).value)
    COL_75 = str(sheet.cell(r, 75).value)
    COL_76 = str(sheet.cell(r, 76).value)
    COL_77 = str(sheet.cell(r, 77).value)
    COL_78 = str(sheet.cell(r, 78).value)
    COL_79 = str(sheet.cell(r, 79).value)
    COL_80 = str(sheet.cell(r, 80).value)
    COL_81 = str(sheet.cell(r, 81).value)
    COL_82 = str(sheet.cell(r, 82).value)
    COL_83 = str(sheet.cell(r, 83).value)
    COL_84 = str(sheet.cell(r, 84).value)
    COL_85 = str(sheet.cell(r, 85).value)
    COL_86 = str(sheet.cell(r, 86).value)
    COL_87 = str(sheet.cell(r, 87).value)
    COL_88 = str(sheet.cell(r, 88).value)
    COL_89 = str(sheet.cell(r, 89).value)
    COL_90 = str(sheet.cell(r, 90).value)
    COL_91 = str(sheet.cell(r, 91).value)
    COL_92 = str(sheet.cell(r, 92).value)
    COL_93 = str(sheet.cell(r, 93).value)
    COL_94 = str(sheet.cell(r, 94).value)
    COL_95 = str(sheet.cell(r, 95).value)
    COL_96 = str(sheet.cell(r, 96).value)

    values = (record_number, COL_1, COL_2, COL_3, COL_4, COL_5, COL_6, COL_7, COL_8, COL_9,
              COL_10, COL_11, COL_12, COL_13, COL_14, COL_15, COL_16, COL_17, COL_18,
              COL_19, COL_20, COL_21, COL_22, COL_23, COL_24, COL_25, COL_26, COL_27,
              COL_28, COL_29, COL_30, COL_31, COL_32, COL_33, COL_34,
              COL_35, COL_36, COL_37, COL_38, COL_39, COL_40, COL_41, COL_42, COL_43,
              COL_44, COL_45, COL_46, COL_47, COL_48, COL_49, COL_50, COL_51, COL_52,
              COL_53, COL_54, COL_55, COL_56, COL_57, COL_58, COL_59, COL_60, COL_61,
              COL_62, COL_63, COL_64, COL_65, COL_66, COL_67, COL_68, COL_69, COL_70,
              COL_71, COL_72, COL_73, COL_74, COL_75, COL_76, COL_77, COL_78, COL_79,
              COL_80, COL_81, COL_82, COL_83, COL_84, COL_85, COL_86, COL_87, COL_88,
              COL_89, COL_90, COL_91, COL_92, COL_93, COL_94, COL_95, COL_96)

    cursor.execute(query_setup, values)

# query = """SELECT * FROM test"""
# r = cursor.execute(query)
# pprint(r)

conn.commit()

cursor.close()
