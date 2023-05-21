input()
kamu = input()
perepeskamu = list(kamu)
perehodi = 0
while perehodi < len(perepeskamu) - 1:
    if perepeskamu[perehodi] == perepeskamu[perehodi + 1]:
        perepeskamu.pop(perehodi)
    else:
        perehodi += 1
    perepeskamu =
print(perepeskamu)