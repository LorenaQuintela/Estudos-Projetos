# Vamos usar um exercício de média do aluno, e adaptar a biblioteca datetime no exercício.

media = float(input("Média do aluno: "))

if media >= 7.0:
  print("Passou direto.")
elif (media >= 4.0) and (media < 7.0):
  print("Recuperação")

  nota_recuperacao = float(input("Nota recuperação: "))

  if nota_recuperacao >= 7.0:
    print("Passou na recuperação.")
  else:
    print("Reprovou na recuperação.")
else:
  print("Reprovou direto.")