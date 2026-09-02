# Vamos usar um exercício de média do aluno, e adaptar a biblioteca datetime no exercício.
from datetime import date

media = float(input("Média do aluno: "))

if media >= 7.0:
  print("Passou direto.")
elif (media >= 4.0) and (media < 7.0):
  print("Recuperação")

  data_prazo = date(2026, 1, 31)

  data_prova_str = input("Informe quando o aluno fez a prova? (formato dd/mm/aaaa): ")

  formato_data = "%d/%m/%Y"
  data_prova_date = date.strptime(data_prova_str, formato_data)

  if data_prova_date <= data_prazo:
    
    nota_recuperacao = float(input("Nota recuperação: "))

    if nota_recuperacao >= 7.0:
      print("Passou na recuperação.")
    else:
      print("Reprovou na recuperação.")
  else:
    print("Prova feita fora do prazo. Aluno reprovado!")
else:
  print("Reprovou direto.")