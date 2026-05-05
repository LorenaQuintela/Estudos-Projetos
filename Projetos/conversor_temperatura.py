#Conversor de Temperatura
# O usuário escolhe uma conversão (Celsius ⇄ Fahrenheit ⇄ Kelvin) e insere um valor para ser convertido.

escala_escolhida = input("Escolha uma escala, C para Celsius, F para Faherenheit e K para Kelvin. (C/F/K): ")

temperatura = float(input("Digite a temperatura: "))

escala_destino = input("Qual conversão você deseja ? (C/F/K): ")

if escala_escolhida == "C" and escala_destino == "F":
  resultado = (temperatura * 9/5) + 32

elif escala_escolhida == "C" and escala_destino == "K":
  resultado = temperatura + 273.15

elif escala_escolhida == "F" and escala_destino == "C":
  resultado = (temperatura - 32) * 9/5

elif escala_escolhida == "F" and escala_destino == "K":
  resultado = (temperatura - 32) *5/9 + 273.15

elif escala_escolhida == "K" and escala_escolhida == "C":
  resultado = temperatura -273.15

elif escala_escolhida == "K" and escala_destino == "F":
  resultado = (temperatura -273.15) * 9/5 + 32

elif escala_escolhida == escala_destino:
  resultado = temperatura

else:
  print("Escala Inválida!")
  resultado = None

if resultado is not None:
  print(f"Resultado: {resultado:.2f} {escala_destino}")