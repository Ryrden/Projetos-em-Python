import math

def BlocoCodificado(list, n):

    for x in range(len(list)):
        list[x] = pow(list[x], 3) % n

    print("\nO bloco codificado é: ")
    for x in range(len(list)):
        print(list[x], end=" ")

    return list

def main():
    list = []

    p = int(input("Digite o primo p: "))
    q = int(input("Digite o primo q: "))

    n = p*q
    print("A chave é ", n, "\n\n")

    while True:
        list.append(int(input("Digite o bloco: ")))

        if list[-1] == 0:
            del list[-1]
            break

    print("O bloco é: ")
    for x in range(len(list)):
        print(list[x], end=" ")

    list = BlocoCodificado(list, n)

    print("O bloco codificado é: ")
    for x in range(len(list)):
        print(list[x], end=" ")

main()
