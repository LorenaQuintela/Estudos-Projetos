#Desenvolva uma calculadora em python com tudo que você aprendeu nos capitulos até aqui no curso, sem pesquisar, organize os passos a passos e comece a desenvolver. Tudo que você viu até aqui, você tem capacidade de realizar esse desafio.



print('*************** Calculadora em Python *******************')

print('Selecione o número da operação desejada:')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
opcao = int(input('Digite sua opção: (1/2/3/4): '))
if opcao == 1:
  def Soma ():
    print("Você escolheu a operação SOMA!")
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    resultado_soma = num1 + num2
    print('A soma dos números', num1, "e", num2, ' é =', resultado_soma)
  Soma()
elif opcao == 2:
  print("Você Escolheu a operação de SUBTRAÇÃO!")
  def Subtracao():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    resultado_sub = num1 - num2
    print('A subtração dos números ', num1, 'e', num2, 'é =', resultado_sub)
  Subtracao()
elif opcao == 3:
  def Multiplicacao():
   print("Você escolheu a operação de MULTIPLICAÇÃO!")
   num1 = int(input('Digite o primeiro número: '))
   num2 = int(input('Digite o segundo número: '))
   resultado_mult = num1 * num2
   print('A Multiplicação dos números ', num1, 'e', num2, 'é =', resultado_mult)
  Multiplicacao()
elif opcao == 4:
  def Divisao ():
    print("Você escolhe a operação de DIVISÃO!")
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    resultado_div = num1 / num2
    print('A Divisão dos números ', num1, 'e', num2, 'é =', resultado_div)
  Divisao()
else:
  print('Opção inválida!')
  print("Selecione um dos números (1/2/3/4)")