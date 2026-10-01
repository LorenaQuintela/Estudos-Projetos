import json

pessoa = {
    "nome": "Lucas",
    "idade": 29,
    "altura": 1.81,
    "dev": True,
    "linguagem": ["Python", "Java", "Angular"],
    
}

with open("pessoa.json", "w") as arquivo_json:
    json.dump(pessoa, arquivo_json)