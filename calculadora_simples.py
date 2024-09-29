# Calculadora Simples
print("-----" * 15)
print("Bem-vindo à Calculadora")
print("-----" * 15)

# solicitaçao para de variaveis como operandos
v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))

print("-----" * 15, "\nInforme com o respectivo número, qual operação deseja realizar:")

# var 'escolha' com 'input()' para requisiçao de numero correspondente a operaçao
escolha = int(input("Soma[1]\nSubtração[2]\nMultiplicação[3]\nDivisão[4]\n"))
resul = ""
ope = 0

# estruturas de decisao para aplicaçao de operaçao desejada e saida para o resultado
if escolha == 1:
    resul = "adição"
    ope = v1 + v2
    print(f"O resultado para sua operação de {resul} {v1} + {v2} é igual a {ope}")
elif escolha == 2:
    resul = "subtração"
    ope = v1 - v2
    print(f"O resultado para sua operação de {resul} {v1} - {v2} é igual a {ope}")
elif escolha == 3:
    resul = "multiplicação"
    ope = v1 * v2
    print(f"O resultado para sua operação de {resul} {v1} x {v2} é igual a {ope}")
elif escolha == 4:
    resul = "divisão"
    ope = v1 / v2
    print(f"O resultado para sua operação de {resul} {v1} : {v2} é igual a {ope:.2f}")
else:
    print("Operação invalida!")
print("-----" * 15)
