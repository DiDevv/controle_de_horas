from datetime import datetime,  timedelta

#Removendo a DATA do datatime e extraindo só a duração
def filtrar_duracao (tempo):
    t = datetime.strptime(tempo, "%H:%M:%S")
    return timedelta(hours = t.hour, minutes = t.minute, seconds = t.second)


#O formato da hora deve ser "00:00:00" (Hora, Minutos, Segundos)
#Desconto é caso você tenha que descontar algumas horas do trabalho no dia
def tempo_restante(horas_totais:str, horas_trabalhadas:str, desconto:str, ) -> str:

    horas_totais_ = filtrar_duracao(horas_totais)
    horas_trabalhadas_hoje_ = filtrar_duracao(horas_trabalhadas)
    desconto_ = filtrar_duracao(desconto)

    restam = horas_totais_ - horas_trabalhadas_hoje_ - desconto_

    return f"Restam {restam} horas, bom trabalho ^^"

print(tempo_restante("06:00:00", "01:41:42", "00:30:00"))