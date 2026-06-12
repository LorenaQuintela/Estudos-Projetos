'''Crie uma função chamada calcular_velocidade_media que receba a distância percorrida (em km) e o tempo gasto para o deslocamento (horas).
A função deve calcular a velocidade média e devolvê-la arrendondada com duas casas décimais.'''

def calcular_velocidade_media(distancia, tempo):
  
  resultado_calculo = distancia /tempo
  resultado_calculo = round(resultado_calculo, 2)


  return resultado_calculo
  
distancia_percorrida = float(input("Informe a distância percorrida em km: "))
tempo_gasto = float(input("Informe o tempo em horas: "))

velocidade_media = calcular_velocidade_media(distancia_percorrida, tempo_gasto)

print(f"A Velocidade média: {velocidade_media} km/h")

