# Crud de carros -> Gerenciador de Garagem que permita cadastrar, listar, editar, deletar e sair.

carros = []

def encontrar_carro(placa):

  carro_encontrado = None

  for carro in carros:
    if carro["placa"].lower() == placa.lower():
      carro_encontrado = carro
      break
  return carro_encontrado

def cadastrar_carro():
  placa = input("Digite a placa: ").strip()

  if len(placa) == 0:
    print("\nO campo placa não pode ser vazio.")
    return
  
  carro_existente = encontrar_carro(placa)
  if carro_existente != None:
    print("\nJá existe um carro cadastrado com essa placa.")
    return
  
  cor = input("Digite a cor: ").strip()
  if len(cor) == 0:
    print("\nO campo cor não pode ser vazio.")
    return

  modelo = input("Digite o modelo: ").strip()
  if len(modelo) == 0:
    print("\nO campo modelo não pode ser vazio.")
    return
  
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

def editar_carro():
  placa = input("Digite a placa do carro que deseja atualizar: ").strip()

  carro_existente = encontrar_carro(placa)

  if carro_existente == None:
    print("\nNão foi encontrado o carro com essa placa!")
    return
  
  dicionario_atualizacao = {
    "placa": carro_existente["placa"],
    "cor": carro_existente["cor"],
    "modelo": carro_existente["modelo"],
    "ano": carro_existente["ano"]
  }

  print("\nPressione Enter para manter o valor atual.")

  nova_placa = input(f"Nova placa (atual:{carro_existente["placa"]}): ").strip()

  if len(nova_placa) > 0:
    if encontrar_carro(nova_placa) != None:
      print("Já existe um outro com essa placa.")
      return
    
    dicionario_atualizacao["placa"] = nova_placa

  nova_cor = input(f"Nova cor (atual: {carro_existente["cor"]}): ").strip()
  if len(nova_cor) > 0:
    dicionario_atualizacao["cor"] = nova_cor

  novo_modelo = input(f"Novo modelo (atual: {carro_existente["modelo"]}): ").strip()
  if len(novo_modelo) > 0:
    dicionario_atualizacao["modelo"] = novo_modelo

  novo_ano = input(f"Novo ano (atual: {carro_existente["ano"]}): ")
  if len(novo_ano) > 0:
    dicionario_atualizacao["ano"] = int(novo_ano)

  carro_existente["placa"] = dicionario_atualizacao["placa"]
  carro_existente["cor"] = dicionario_atualizacao["cor"]
  carro_existente["modelo"] = dicionario_atualizacao["modelo"]
  carro_existente["ano"] = dicionario_atualizacao["ano"]

  print("\nCarro editado com êxito.")

#Precisa referenciar uma informação única no caso (Placa)
def deletar_carro():
  placa = input("Digite a placa do carro a ser deletado: ").strip()

  carro_retornado = encontrar_carro(placa)

  if carro_retornado == None:
    print("\nNão foi encontrado o carro com essa placa!")
    return
  
  carros.remove(carro_retornado)
  print("\nCarro removido com sucesso!")
    
def exibir_menu():
  print("\n--- GERENCIADOR DE GARAGEM ---\n")
  print("1 - Cadastrar um carro")
  print("2 - Listar os carros existentes.")
  print("3 - Editar um carro")
  print("4 - Deletar um carro")
  print("5 - Sair")

while True:
  exibir_menu()

  opcao = input("Escolha uma opção: ").strip()

  if opcao == "1":
    cadastrar_carro()
  elif opcao == "2":
    listar_carros()
  elif opcao == "3":
    editar_carro()
  elif opcao == "4":
    deletar_carro()
  elif opcao == "5":
    print("\nEncerrando o Gerenciador de Garagem! Até mais.")
    break
  else:
    print("\nOpção inválida!!")
