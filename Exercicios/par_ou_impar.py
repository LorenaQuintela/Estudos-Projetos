def par_ou_impar(numero):

  if numero % 2 == 0 :
    return f"O número {numero} é Par!"

  else:
    return f"O número {numero} é Impar!"

numero = int(input("Digite um número inteiro: "))

resultado = par_ou_impar(numero)
print(resultado)