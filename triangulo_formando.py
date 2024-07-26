#Formando e analisando triângulo

print ('Vamos analisar as retas do seu triângulo!')
r1 = float(input('Informe o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))
#Regra para formação de um triângulo:
#cada lado deve ser menor do que a soma dos outros dois lados.
if r1 < r2 + r3:
   r2 < r1 + r3
   r3 < r2 + r3
   print ('O triângulo pode ser formado com as medidas fornecidas!')
else:
  #Resposta para o não atendimento dos requisitos de formação do triangulo.
  print('Infelizmente as medidas fornecidas não permitem a formação de um triângulo!')