# Calculadora:
# Objetivo: O usuário envia 2 números e uma operação entre +, -, * e /
# Desafio: Fazer isso em menos de 30 linhas (menos 3 de apresentação e as linhas em branco)
def num(txt):
    while True:
        n = input(f"Qual o {txt} número? ")
        if n.isdigit():
            return int(n)
        else:
            print("Isso não é um número!")
def calc(n1, n2):
    while True:
        opr = input("Qual a operação? ")
        match opr:
            case "+":
                return n1 + n2
            case "-":
                return n1 - n2
            case '*':
                return n1 * n2
            case '/':
                if n1 == 0 or n2 == 0:
                    print("Não é possível fazer divisão por 0!")
                else:
                    resultado = n1 / n2
                    return int(resultado) if resultado.is_integer() else resultado
            case _:
                print("Isso não é nem +, nem -, nem * ou /!")
print(f"O resultado é igual a {calc(num("primeiro"), num("segundo"))}")
# Desafio comprido!