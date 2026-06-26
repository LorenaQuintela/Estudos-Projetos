''' Calculadora em Python refatorada de um projeto que ja tinha feito a muito tempo de projeto1_calculadora.py, aqui usando conceitos que simulam nossa calculadora do notebook ou celular, dando um valor atual e usando esse valor para fazer as operações.'''
def soma (a, b):
    return a + b
  
def subtracao(a, b):
    return a - b
   
def multiplicacao(a, b):
   return a * b
   
def divisao (a, b):
  return a / b

def exibir_menu():
    print(' ===  Calculadora em Python === ')

    print('Selecione o número da operação desejada:')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('0 - Sair')

def formatar_resultado(resultado):
   if resultado.is_integer(): 
      resultado_convertido = int(resultado)

      return resultado_convertido
   
   return resultado

def main():
  opcoes_validas = {"1", "2", "3", "4", "0"}

  try:
    resultado_atual = float(input("Digite o valor inicial: "))
  except ValueError:
    print("Número inicial inválido")
    return #Não precisa passar valor quando é para encerrar o fluxo.
    
  while True:
    resultado_formatado = formatar_resultado(resultado_atual)
    print(f"Resultado atual: {resultado_formatado}\n")
    exibir_menu()

    opcao_escolhida = input('Digite sua opção: (1/2/3/4/0): ')

    if opcao_escolhida == "0":
      break
      
    if opcao_escolhida not in opcoes_validas:
      print("\nOpção Inválida!")
      print("Opções válidas 1, 2, 3, 4 e 0\n")

      continue
    
    try:
      valor_operando = float(input("Digite o próximo valor do operando: "))
    except ValueError:
      print("\nNúmero inválido")
      continue #Vai pular os ifs abaixo e vai voltar para o inicio do while
    if opcao_escolhida == "1":
      resultado_atual = soma(resultado_atual, valor_operando)
    elif opcao_escolhida == "2":
      resultado_atual = subtracao(resultado_atual, valor_operando)
    elif opcao_escolhida == "3":
      resultado_atual = multiplicacao(resultado_atual, valor_operando)
    elif opcao_escolhida == "4":
      try:
        resultado_atual = divisao(resultado_atual, valor_operando)
      except ZeroDivisionError:
        print("\nNão se pode dividir por zero!")
  
  print("Encerrando a Calculadora. Até mais!")

main()
