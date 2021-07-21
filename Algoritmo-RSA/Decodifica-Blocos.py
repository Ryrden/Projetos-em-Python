import math
import decimal as dc
import os
import time
dc.getcontext().prec = 100000000000000000


def MDC(num1, num2):

    num1 = abs(num1)
    num2 = abs(num2)

    if(num1 % num2 == 0):
        return num2
    elif (num2 % num1 == 0):
        return num1
    else:
        while(num2 != 0):
            resto = num1 % num2
            num1 = num2
            num2 = resto

        return num1


def alocaVetorPositive(tam):

    list = []
    for x in range(tam):
        list.append(x+1)

    return list


def alocaVetorNegative(tam):

    list = []
    for x in range(tam):
        list.append((x+1)*-1)

    return list


def resto_AB(a, b):

    r = abs(b % a)
    q = abs(b / a)

    if (a > 0 and b > 0):
        r = b % a
    elif (a > 0 and b < 0):
        b = abs(b)

        r = b % a
        q = b / a
        if (r > 0):
            q = -q - 1
            r = a - r

    return r


def Congruencia(p, q):

    n = (p-1)*(q-1)

    inversoP = []
    inversoN = []

    inversoP = alocaVetorPositive(n)
    inversoN = alocaVetorNegative(n)

    resto = resto_AB(n, 3)

    if (MDC(3, n) != 1):
        print("\n3 não tem inverso módulo ", n)
        print("\n\nO resto da divisão é ", resto)
    else:

        InversoPositive = 0
        InversoNegative = 0
        i = 0

        while (True):
            if (1 - n*inversoP[i] % 3 == 0):
                InversoPositive = (1 - n*inversoP[i] / 3)
                break
            i += 1

        i = 0
        while (True):
            if ((1 - (n*inversoN[i])) % 3 == 0):
                InversoNegative = (1 - (n*inversoN[i])) / 3
                break
            i += 1

        if InversoPositive > InversoNegative:
            return InversoPositive
        else:
            return InversoNegative


def DecodificaBloco(list, d, n):

    decodificado = []

    for x in range(len(list)):

        res = pow(dc.Decimal(list[x]), dc.Decimal(d))
        res = int(res % n)
        decodificado.append(res)

    return decodificado


def main():

    codificado = []
    decodificado = []
    print("Esse programa tem como objetivo Decodificar blocos de números nos quais foram codificados através do Algoritmo RSA.\nUtilizando"
          + " das números dos blocos e os números primos p e q, será dado a decodificação em lista, na mesma ordem.\n\n")

    p = int(input("Digite o primo p: "))
    q = int(input("Digite o primo q: "))

    n = p*q
    print("\n\nA chave secreta é n = p * q, logo:\n\t\t  n =", n, "\n")
    time.sleep(1)
    print("\nPróxima Etapa agora...\n")
    os.system("pause")
    os.system("cls")

    codificado.append(int(input("Digite o primeiro bloco codificado: ")))
    while codificado[-1] != 0:
        os.system("cls")
        print("Caso não queira Digitar mais nenhum bloco, digite 0\n")

        print("Blocos Digitados até o momento: -> ", end="")
        for x in range(len(codificado)):
            print(codificado[x], end=" ")

        codificado.append(
            int(input("\n\nDigite o próximo bloco codificado: ")))

    del codificado[-1]

    d = Congruencia(p, q)

    decodificado = DecodificaBloco(codificado, d, n)

    print("Processando...")
    time.sleep(3)

    print("\n\nO bloco decodificado é: \n\t", end="")
    for x in range(len(decodificado)):
        print(decodificado[x], end=" ")

    print("\n\n\n\n     encoded by: Ryan S.\n")
    os.system("pause")
main()
