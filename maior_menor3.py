#Maior e menor entre 3 número
a = int (input('Digite o primeiro número: '))
b = int (input('Digite o segundo número: '))
c = int (input('Digite o terceiro número: '))
#saber o menor entre eles
if a<b and a<c:
  menor = a
if b<a and b<c:
  menor = b
if c<a and c<b:
  menor = c
#saber o maior entre eles
if a>b and a>c:
  maior = a
if b>a and b>c:
  maior = b
if c>a and c>b:
  maior = c
print ('O menor foi {};'.format(menor))
print ('O maior foi {}.'.format(maior))