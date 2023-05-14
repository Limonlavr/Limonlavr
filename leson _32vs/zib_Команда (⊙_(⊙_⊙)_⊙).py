n = int(input())
a = 0

for i in range(n):
    zadachi1 = input()
    zadachi1.split(" ")
    x = zadachi1[0]
    y = zadachi1[1]
    z = zadachi1[2]
    if x + y + z >=2:
        a+=1
        print(a)