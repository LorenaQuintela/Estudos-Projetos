import json

json_input= '{ "nome": "Lucas", "idade": 29, "email": "lucas@email.com", "desenvolvedor": true}'
print(f"Tipo do input: {type(json_input)}\n")

#Faz caminho reverso de um json para dicionário
dict_convertido = json.loads(json_input)

print(dict_convertido)
print(f"Tipo do dict convertido: {type(dict_convertido)}")

print(dict_convertido["nome"])