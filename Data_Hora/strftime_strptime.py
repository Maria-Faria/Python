from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = '%d/%m/%Y %a' # %a -> dia da semana
mascara_en = '%Y-%m-%d %H:%M'

print(data_hora_atual.strftime(mascara_ptbr))

print(datetime.strptime(data_hora_str, mascara_en))