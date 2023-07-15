valor = float(input("Qual o valor de saque? "))

valores = [1, 5, 10, 50, 100]

qtd = [0, 0, 0, 0, 0]

i = 4

while (i >= 0):
    while (valor >= valores[i]):
        qtd[i] += 1
        valor -= valores[i]
    i -= 1

for i in range(4, -1, -1):
    if (qtd[i] != 0 and qtd[i] > 1):
        print(f"{qtd[i]} notas de {valores[i]}", end=', ')
    elif (qtd[i] == 1):
        print(f"1 nota de {valores[i]}", end=', ')
print("\b\b  ")
