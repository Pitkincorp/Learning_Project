import openpyxl

book = openpyxl.open(r"C:\Users\YaYuBeletskiy\Desktop\Регистрация\+БЕЛЕЦКИЙ Я.Ю._Планы-отчёты_19.06.2018_Регистрация\+15.10.2021.xlsx",read_only=True)
sheet = book.active

# for row in range(3,sheet.max_row+1):
#     print(sheet[row][2].value)
pretext = "- Комиссионное рассмотрение паспорта "
posttext = ", выдача замечаний;\n"

text = [pretext+sheet[row][2].value[39:]+posttext for row in range(3,sheet.max_row+1)]
with open(r"C:\Users\YaYuBeletskiy\Desktop\Регистрация\+БЕЛЕЦКИЙ Я.Ю._Планы-отчёты_19.06.2018_Регистрация\Otchet.txt","w") as file:
    file.writelines(text)