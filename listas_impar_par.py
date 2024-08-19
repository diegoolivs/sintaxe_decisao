# Criação de duas listas
listaP = []
listaI = []

# repetição FOR com a função RANGE(quantidade de dados já atribuida)
for n in range(0, 21):

    # condição de decisão para achar valores pares
    if n % 2 == 0:

        # atribuição dos pares para lista específica
        listaP.append(n)

    # caso não atende, será inserida na outra lista os ímpares
    else:
        listaI.append(n)

print(f'Esta lista contém os números pares:\n {listaP}')
print(f'Esta lista contém os números impares:\n {listaI}')

