def produto( x, y):
  resultado_produto = x * y
  return x, y, resultado_produto

def soma(x, y):
  resultado_soma = x + y
  return x, y, resultado_soma

x, y, res_função_produto = produto(10, 2)
print(f"O produto de {x} x {y} é: {res_função_produto}")

x, y, res_função_soma = soma(25, 31)
print(f"A soma de {x} + {y} é: {res_função_soma}")

diferenca = res_função_soma - res_função_produto 

print(f"A diferença entre {res_função_soma} e {res_função_produto} é: {diferenca}")