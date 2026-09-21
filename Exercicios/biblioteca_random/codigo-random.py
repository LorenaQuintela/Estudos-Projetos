from random import random, randint

# random () gera números decimais
#(float) aleatório seguindo o intervalo de 0 - 1, onde 0 está incluso e 1 não.

resultado_random = random()
print(resultado_random)

# randint() gera números inteiros aleatório seguindo o intervalo definido pelos parâmetros (incluindo cada um deles).
resultado_randint = randint(1, 10)
print(resultado_randint)