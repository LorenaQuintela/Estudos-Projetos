import json
pessoa = {
    "nome": "Daniel",
    "idade": 50,
    "altura": 1.76,
    "dev": True,
    "linguagem": ["Python", "JavaScript", "Ruby", "Go"],
    #"numeros_preferidos": {13, 15, 25} #Json não tem suporte a conjunto
}

pessoa_json = json.dumps(pessoa, indent= 2)
print(type(pessoa_json))
print(pessoa_json)