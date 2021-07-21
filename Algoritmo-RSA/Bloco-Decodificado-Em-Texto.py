import os

bloco = []
texto = []
frase = []

bloco.append(int(input("Digite o primeiro bloco codificado: ")))
while bloco[-1] != 0:
    os.system("cls")
    print("Caso não queira Digitar mais nenhum bloco, digite 0\n")

    print("Blocos Digitados até o momento: -> ", end="")
    for x in range(len(bloco)):
        print(bloco[x], end=" ")

    bloco.append(
        int(input("\n\nDigite o próximo bloco codificado: ")))

del bloco[-1]

for x in range(len(bloco)):
    texto.append(str(bloco[x]))

texto = str(''.join(texto))

for x in range(0, len(texto), 2):

    temp = []
    temp.append(texto[x])
    try:
        temp.append(texto[x+1])
    except:
        None
    temp = int(''.join(temp))

    if (temp+55) == '99':
        frase.append(" ")
    else:
        frase.append(chr(temp+55))
    

for x in range(len(frase)):

    print(frase[x], end=' ')
