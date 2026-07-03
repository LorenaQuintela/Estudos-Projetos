# Crud de carros -> Gerenciador de Garagem que permita cadastrar, listar, editar, deletar e sair.

carros = []

def cadastrar_carro():
  placa = input("Digite a placa: ")
  cor = input("Digite a cor: ")
  modelo = input("Digite o modelo: ")
  ano = int(input("Digite o ano: "))

  carro = {
    "placa": placa,
    "cor": cor,
    "modelo": modelo,
    "ano": ano
  }

  carros.append(carro)
  print("\nCarro cadastrado com sucesso!")

def listar_carros():
  print("\n---------------------- LISTA DE CARROS ------------------------")
  
  for carro in carros:
    print(f"Placa: {carro["placa"]} | Modelo: {carro["modelo"]} | Cor: {carro["cor"]} | Ano: {carro["ano"]}")

  print(63*"-")
    
def exibir_menu():
  print("\n--- GERENCIADOR DE GARAGEM ---\n")
  print("1 - Cadastrar um carro")
  print("2 - Listar os carros existentes.")
  print("3 - Editar um carro")
  print("4 - Deletar um carro")
  print("5 - Sair")

while True:
  exibir_menu()

  opcao = input("Escolha uma opção: ")

  if opcao == "1":
    cadastrar_carro()
  elif opcao == "2":
    listar_carros()
  elif opcao == "3":
    print("\nAinda desenvolvendo")
  elif opcao == "4":
    print("\nAinda desenvolvendo")
  elif opcao == "5":
    print("\nEncerrando o Gerenciador de Garagem! Até mais.")
    break
  else:
    print("\nOpção inválida!!")



def Editar_carro():
  return

def Deletar_carro(placa):
  placa = input("Digite a placa: ")

