from datetime import datetime

# Para descrever formato de anos com 4 os digitos usamos %Y maúsculo, para ano abreviado com 2 digitos usamos %y minúsculo.

data_string = "27/07/2026"
data_formato = "%d/%m/%Y"
data_date  = datetime.strptime(data_string, data_formato)

data_formatada = data_date.strftime( "%d/%m/%Y")
print(data_formatada)
print(type(data_date))