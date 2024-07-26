#Jogo de Adivinha

#'randint' é um metodo de random para escolher um número int aleatório.
from random import randint
#'sleep' de 'time' é um método para esperar alguns segundo.
from time import sleep
#metodo escolherá aleatoriamente entre 1 a 5
num = randint(1, 5)
print('----' * 20)
print('Vou pensar em um número entre 1 e 5!')
print('----' * 20)
jogada = int(input('Qual número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogada == num:
  print('Parabéns você acertou!')
else:
  print('Você errou!')
print(f'Eu escolhi o número {num}.')