import json

pessoa = {
    "nome": "Lorena",
    "idade": 33,
    "email": "lorena@email.com",
    "desenvolvedor": True
}

print(f" Tipo da pessoa: {type(pessoa)}\n")

#Convertendo o dicionário em Json e adicionando formatação com indent=2
json_conversão = json.dumps(pessoa, indent=2)

print(json_conversão)
print(f"Tipo do json conversão: {type(json_conversão)}")