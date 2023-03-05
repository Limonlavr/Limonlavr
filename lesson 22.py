import json
# open("Я Генадий.txt", "w",encoding="utf-8").write("Приффки я генадий")
# open("геннадий.json", "w").write("Heelo")

# JSON ЗАПИСЬ
# text = [1, 5.3, True, None, [1, 2], (5, 7), "ENG", "РУС"]
# f = open("я генадий.json", "w", encoding="utf-8")
# json.dump(text, f, ensure_ascii=False)
# b = json.dump(text, ensure_ascii=False)
# print(b)
# f.close()


# JSON ЧТЕНИЕ
# f = open("zzz генннадий.json", "r", encoding="utf-8")
# content = json.load(f)
# print(content)
# print(type(content))
# f.close()


# JSON задачя №1
#
# f = open("ягеннадий2.txt", "r", encoding="utf-8")
# con = f.readlines()
# print(con)
# f.close()
# slovarishe = {}
# for elementiki in con:
#     print(elementiki)
#     lomka = elementiki.split(": ")
#     print(lomka[0])
#     print(lomka[1])
#     slovarishe['gaechni'] = lomka[1]
#
# print(slo)

#Адачя 2--------------------------------------------------------------------------------------------
f = open("ягеннадий2.txt", "r", encoding="utf-8")
content = json.load(f)
f.close()
print(content)
for i,em in content:
    if type(em) == str:
        content[i] + "!"
