def fatorial(num):
    fat = num
    if num > 1:
        while num > 1:
            fat = fat * (num - 1)
            num -= 1
        return fat

    return 1


def num_binomial(n, p):
    # (n,p) =    n! / p! * (n-p)!

    fat_n = fatorial(n)
    fat_p = fatorial(p)

    answer = fat_n / ((fat_p) * (fatorial(n-p)))

    return answer


def binomio_de_newton(x, y, n):
    # (x,y)^n = Somátorio(i=0 -> n) de (n,i) * x^n-i * y^i
    cont_p = 0
    while (cont_p <= n):
        coeficiente = num_binomial(n, cont_p)

        if coeficiente > 1:
            print(f"({int(coeficiente)})", end="*")

        if cont_p > 0 and cont_p < n:
            exp = n - cont_p
            if exp != 1 and cont_p != 1:
                print(f"({x}){power(str(exp))}", end="")
                print(f"({y}){power(str(cont_p))}", end=" ")
            elif (cont_p == 1):
                print(f"({x}){power(str(exp))}", end="")
                print(f"({y})", end=" ")
            elif (cont_p == n - 1):
                print(f"({x})", end="*")
                print(f"({y}){power(str(cont_p))}", end=" ")

        elif cont_p == 0:  # 1º termo
            print(f"({x}){power(str(n))}", end=" ")
        elif cont_p == n:  # ultimo termo
            print(f"({y}){power(str(n))}", end=" ")

        if cont_p != n:
            if y < 0:
                if cont_p % 2 == 0:
                    print("-", end=" ")
                else:
                    print("+", end=" ")
            else:
                print("+", end=" ")

        cont_p += 1

    pass


def power(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)


def main():
    print("Entre com os números para expansão binômial com eles na forma:")
    print(
        f"\t\t\t(x+y){power('n')} \n\t\t\t  ou \n\t\t\t(x-y){power('n')}")
    x = int(input("Digite o x: "))
    y = int(input("Digite o y: "))
    n = int(input("Digite o n: "))

    binomio_de_newton(x, y, n)


main()
