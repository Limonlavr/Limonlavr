# Задачя 2
# name = input("Как файл назавёшь?:")
# f=open("text.txt","r" ,encoding="utf-8")
# g=f.readlines()
# n=0
# for line in g:
#     n=n+1
#     print(str(n)+line.rstrip())
# Задачя 3--------------------------------------------------------------------------------------------------
f0 = open("text.txt","r" ,encoding="utf-8")
v = f0.readlines()   # построчное содержание
f0.close
hf = 0
while v != []:  #пока не выписали всё шо можно
    nf = nf + 1
    fm = open(str(nf) + ",txt", "w", encoding="utf - 8")
    ts = v[:3]  #вытащили три строчки
    fm.write(str(ts))
