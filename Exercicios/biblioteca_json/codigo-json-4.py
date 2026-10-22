import json

pessoa = {
    "nome": "Lucas",
    "idade": 29,
    "altura": 1.81,
    "dev": True,
    "linguagem": ["Python", "Java", "Angular"],
    
}
#Caso o arquivo não exista o python cria o arquivo e escreve dentro dele.
with open("pessoa.json", "w") as arquivo_json:
    json.dump(pessoa, arquivo_json, indent=2)

#A informação prévia que você tinha no arquivo se perde com alteração
#porque ela vai ser sobrescrita.
print("Terminamos de gravar no arquivo")