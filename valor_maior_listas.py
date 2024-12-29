# Encontrar o maior numero da matriz (v1)

matriz = [[10, 44, 25], [33, 4, 11], [25, 44, 55], [21, 47, 3]]
maior = []

# variaveis criadas para percorrer cada lista da matriz
for i in matriz[0]:
    for y in matriz[1]:
        for x in matriz[2]:
            for z in matriz[3]:

                if i > y and x and z:
                    maior = i
                if y > i and x and z:
                    maior = y
                if x > i and y and z:
                    maior = x
                if z > i and y and x:
                    maior = z

print(maior)  # saida 55
