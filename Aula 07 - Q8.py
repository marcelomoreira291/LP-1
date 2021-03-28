#gera arquivo principal
with open("numeros.txt", "w") as numeros:
    for i in range(2, 1001):
        numeros.write(f"{i}\n")

#gera os multiplos de 2
with open("multiplos2.txt", "w") as multiplos2:
    with open("numeros.txt") as numeros:
        for i in numeros.readlines():
            if int(i) % 2 == 0:
                multiplos2.write(f"{i}")

# gerando invertidos
with open("multiplos_invertidos.txt", "w") as multiplos_i:
    with open("multiplos2.txt") as multiplos2:
        l = []
        for i in multiplos2.readlines():
            l.append(int(i))
        for i in l[::-1]:
            multiplos_i.write(f"{i}\n")

#impares
with open("impares.txt", "w") as impares:
    with open("numeros.txt") as numeros:
        for i in numeros.readlines():
            if int(i) % 2 != 0 and 10 < int(i) < 800:
                impares.write(f"{i}")

#primos
def primo(n):  # função
    cont = 0
    i = 0
    while i<= n or cont < 2:
        i = i + 1
        x = n % i
        if x == 0:
            cont = cont + 1

    if cont <= 2:
        primos.write(f"{n}\n")
        print("\n")

with open("primos.txt", "w") as primos:
    with open("numeros.txt") as numeros:
        for i in numeros:
            primo(int(i)) 

#multiplos
with open("multiplos2.txt", "w") as m2, open("multiplos3.txt", "w") as m3, open("multiplos5.txt", "w") as m5:
    with open("numeros.txt") as numeros:
        for i in numeros.readlines():
            if int(i) % 2 == 0:
                m2.write(f"{int(i)}\n")
            if int(i) % 3 == 0:
                m3.write(f"{int(i)}\n")
            if int(i) % 5 == 0:
                m5.write(f"{int(i)}\n")