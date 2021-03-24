import random as rd


class Adivinhe:

    def __init__(self):

        self.numero = rd.randrange(1, 100)

    def Jogo(self, num):

        acertou = False
        tentativas = 0

        while not acertou:

            if num == self.numero:
                print("\nParabéns, você acertou, o número realmente é", self.numero)
                print("\nVocê levou", tentativas, "tentativas para acertar")
                acertou = True
            else:
                print("\n\t\tERROU!!")

                if num > self.numero:
                    print(
                        "\nVocê digitou um número MAIOR do que ao que eu estou pensando...")
                else:
                    print(
                        "\nVocê digitou um número MENOR do que ao que eu estou pensando...")

                num = int(input("\nTente de novo, digite outro valor: "))

                tentativas += 1

    def Iniciar(self):
        print(self.barras() +
              '\n                        Bem vindo ao jogo ADIVINHE O NÚMERO\n\n'
              'nesse jogo eu irei pensar em um número entre 1 a 100\n'
              'e você terá de adivinha-ló, será que você vai conseguir?\n' +
              self.barras())

        num = int(input("Digite um valor entre 1 a 100 para começar: "))

        self.Jogo(num)

    def barras(self):

        barra = '-'
        for i in range(85):
            barra = barra + '-'
        return barra


m = Adivinhe()

m.Iniciar()
