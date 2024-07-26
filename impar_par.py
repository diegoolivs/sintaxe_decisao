#Impar_Par
print('Olá, vamos saber se o número é impar ou par!')
num = int (input('Digite um número e eu direi: '))
#variavel 'resul' recebera o resto da divisao do valor de 'num'
resul = (num % 2)
#se o resultado for igual a 0, a resposta sera par, caso contrario impar
if resul == 0:
  print (f'O número {num} é par.')
else:
  print (f'O número {num} é impar.')