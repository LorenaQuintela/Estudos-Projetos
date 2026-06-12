def calcular_media(numero_aluno):
  nota1 = float(input("Digite a primeira nota: "))
  nota2 = float(input("Digite a segunda nota: "))
  nota3 = float(input("Digite a terceira nota: " ))

  resul_media = (nota1 + nota2 + nota3) / 3
  resul_media = round(resul_media, 1)

  print(f"Média do aluno {numero_aluno}: {resul_media} \n")

calcular_media(1)
calcular_media(2)
calcular_media(3)

  
