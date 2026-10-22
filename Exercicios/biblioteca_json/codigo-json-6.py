import json

lista_dicts = [
    {
    "nome": "Lucas",
    "idade": 29,
    "altura": 1.81,
    "dev": True,
    "linguagem": ["Python", "Java", "Angular"]
    },
    {
    "nome": "Lucas",
    "idade": 29,
    "altura": 1.81,
    "dev": True,
    "linguagem": ["Python", "Java", "Angular"]
    },
    {
    "nome": "Lucas",
    "idade": 29,
    "altura": 1.81,
    "dev": True,
    "linguagem": ["Python", "Java", "Angular"]
    }
]


#print(f"Tipo da lista: {type(lista_dicts)}")

#for item in lista_dicts:
    #print(f"Tipo do item: {type(item)}")

json_str = json.dumps(lista_dicts, indent=2)

print(json_str)
print(type(json_str))