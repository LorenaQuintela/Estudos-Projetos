# Crud de carros -> Gerenciador de Garagem que permita cadastrar, listar, editar, deletar e sair.
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
    print("\nAinda desenvolvendo")
  elif opcao == "2":
    print("Ainda desenvolvendo")
  elif opcao == "3":
    print("Ainda desenvolvendo")
  elif opcao == "4":
    print("Ainda desenvolvendo")
  elif opcao == "5":
    print("\nEncerrando o Gerenciador de Garagem! Até mais.")
    break
  else:
    print("Opção inválida!!")

def Cadastrar_carro(placa, cor, modelo, ano):
  placa = input("Digite a placa: ")
  cor = input("Digite a cor: ")
  modelo = input("Digite o modelo: ")
  ano = input("Digite o ano: ")

  return placa, cor, modelo, ano

def Listar_carro(lista):
  lista_carros = []
  return lista

def Editar_carro():
  return

def Deletar_carro(placa):
  placa = input("Digite a placa: ")

