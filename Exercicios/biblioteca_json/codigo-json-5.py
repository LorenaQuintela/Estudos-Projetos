import json

#No modo leitura o arquivo precisa estar criado(precisa existir), caso contrário dará erro.
#Convertendo para json para dicionário e usando propriedade de dicionário para comprovar.
with open("pessoa.json", "r") as arquivo_json:
    dict_convertido = json.load(arquivo_json)

    print(dict_convertido)
    print(type(dict_convertido))
    print(dict_convertido["altura"])

