import xlrd
import psycopg2
from pprint import pprint

book = xlrd.open_workbook("data/statistics.xlsx")
sheet = book.sheet_by_name("Лист4")

database = psycopg2.connect(database="test", user="user1", password="password", host="localhost", port="5432")
cursor = database.cursor()

query = """INSERT INTO test (ID, COL_1, COL_2, COL_3, COL_4, COL_5, COL_6, COL_7, COL_8, COL_9,
              COL_10, COL_11, COL_12, COL_13, COL_14, COL_15, COL_16, COL_17, COL_18,
              COL_19, COL_20, COL_21, COL_22, COL_23, COL_24, COL_25, COL_26, COL_27,
              COL_28, COL_29, COL_30, COL_31, COL_32, COL_33, COL_34, 
              COL_35, COL_36, COL_37, COL_38, COL_39, COL_40, COL_41, COL_42, COL_43,
              COL_44, COL_45, COL_46, COL_47, COL_48, COL_49, COL_50, COL_51, COL_52,
              COL_53, COL_54, COL_55, COL_56, COL_57, COL_58, COL_59, COL_60, COL_61,
              COL_62, COL_63, COL_64, COL_65, COL_66, COL_67, COL_68, COL_69, COL_70,
              COL_71, COL_72, COL_73, COL_74, COL_75, COL_76, COL_77, COL_78, COL_79,
              COL_80, COL_81, COL_82, COL_83, COL_84, COL_85, COL_86, COL_87, COL_88,
              COL_89, COL_90, COL_91, COL_92, COL_93, COL_94, COL_95, COL_96) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
              %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

for r in range(1, sheet.nrows):
    ID = sheet.cell(r, 0).value
    COL_1 = sheet.cell(r, 1).value
    COL_2 = sheet.cell(r, 2).value
    COL_3 = sheet.cell(r, 3).value
    COL_4 = sheet.cell(r, 4).value
    COL_5 = sheet.cell(r, 5).value
    COL_6 = sheet.cell(r, 6).value
    COL_7 = sheet.cell(r, 7).value
    COL_8 = sheet.cell(r, 8).value
    COL_9 = sheet.cell(r, 9).value
    COL_10 = sheet.cell(r, 10).value
    COL_11 = sheet.cell(r, 11).value
    COL_12 = sheet.cell(r, 12).value
    COL_13 = sheet.cell(r, 13).value
    COL_14 = sheet.cell(r, 14).value
    COL_15 = sheet.cell(r, 15).value
    COL_16 = sheet.cell(r, 16).value
    COL_17 = sheet.cell(r, 17).value
    COL_18 = sheet.cell(r, 18).value
    COL_19 = sheet.cell(r, 19).value
    COL_20 = sheet.cell(r, 20).value
    COL_21 = sheet.cell(r, 21).value
    COL_22 = sheet.cell(r, 22).value
    COL_23 = sheet.cell(r, 23).value
    COL_24 = sheet.cell(r, 24).value
    COL_25 = sheet.cell(r, 25).value
    COL_26 = sheet.cell(r, 26).value
    COL_27 = sheet.cell(r, 27).value
    COL_28 = sheet.cell(r, 28).value
    COL_29 = sheet.cell(r, 29).value
    COL_30 = sheet.cell(r, 30).value
    COL_31 = sheet.cell(r, 31).value
    COL_32 = sheet.cell(r, 32).value
    COL_33 = sheet.cell(r, 33).value
    COL_34 = sheet.cell(r, 34).value
    COL_35 = sheet.cell(r, 35).value
    COL_36 = sheet.cell(r, 36).value
    COL_37 = sheet.cell(r, 37).value
    COL_38 = sheet.cell(r, 38).value
    COL_39 = sheet.cell(r, 39).value
    COL_40 = sheet.cell(r, 40).value
    COL_41 = sheet.cell(r, 41).value
    COL_42 = sheet.cell(r, 42).value
    COL_43 = sheet.cell(r, 43).value
    COL_44 = sheet.cell(r, 44).value
    COL_45 = sheet.cell(r, 45).value
    COL_46 = sheet.cell(r, 46).value
    COL_47 = sheet.cell(r, 47).value
    COL_48 = sheet.cell(r, 48).value
    COL_49 = sheet.cell(r, 49).value
    COL_50 = sheet.cell(r, 50).value
    COL_51 = sheet.cell(r, 51).value
    COL_52 = sheet.cell(r, 52).value
    COL_53 = sheet.cell(r, 53).value
    COL_54 = sheet.cell(r, 54).value
    COL_55 = sheet.cell(r, 55).value
    COL_56 = sheet.cell(r, 56).value
    COL_57 = sheet.cell(r, 57).value
    COL_58 = sheet.cell(r, 58).value
    COL_59 = sheet.cell(r, 59).value
    COL_60 = sheet.cell(r, 60).value
    COL_61 = sheet.cell(r, 61).value
    COL_62 = sheet.cell(r, 62).value
    COL_63 = sheet.cell(r, 63).value
    COL_64 = sheet.cell(r, 64).value
    COL_65 = sheet.cell(r, 65).value
    COL_66 = sheet.cell(r, 66).value
    COL_67 = sheet.cell(r, 67).value
    COL_68 = sheet.cell(r, 68).value
    COL_69 = sheet.cell(r, 69).value
    COL_70 = sheet.cell(r, 70).value
    COL_71 = sheet.cell(r, 71).value
    COL_72 = sheet.cell(r, 72).value
    COL_73 = sheet.cell(r, 73).value
    COL_74 = sheet.cell(r, 74).value
    COL_75 = sheet.cell(r, 75).value
    COL_76 = sheet.cell(r, 76).value
    COL_77 = sheet.cell(r, 77).value
    COL_78 = sheet.cell(r, 78).value
    COL_79 = sheet.cell(r, 79).value
    COL_80 = sheet.cell(r, 80).value
    COL_81 = sheet.cell(r, 81).value
    COL_82 = sheet.cell(r, 82).value
    COL_83 = sheet.cell(r, 83).value
    COL_84 = sheet.cell(r, 84).value
    COL_85 = sheet.cell(r, 85).value
    COL_86 = sheet.cell(r, 86).value
    COL_87 = sheet.cell(r, 87).value
    COL_88 = sheet.cell(r, 88).value
    COL_89 = sheet.cell(r, 89).value
    COL_90 = sheet.cell(r, 90).value
    COL_91 = sheet.cell(r, 91).value
    COL_92 = sheet.cell(r, 92).value
    COL_93 = sheet.cell(r, 93).value
    COL_94 = sheet.cell(r, 94).value
    COL_95 = sheet.cell(r, 95).value
    COL_96 = sheet.cell(r, 96).value

    values = (ID, COL_1, COL_2, COL_3, COL_4, COL_5, COL_6, COL_7, COL_8, COL_9,
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

    cursor.execute(query, values)

query = """SELECT * FROM test"""
r = cursor.execute(query)
pprint(r)


cursor.close()

database.commit()

database.close()