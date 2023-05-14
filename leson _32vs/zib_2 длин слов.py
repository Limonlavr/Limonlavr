words = int(input())
for i in range(words):
    words2 = input()
    if len(words2) > 10:
        p1 = words2[0]
        p2 = str(len(words2) - 2)
        p3 = words2[-1]
        a = p1 + p2 + p3
        print(a)
    else:
        print(words2)