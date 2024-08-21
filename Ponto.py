from datetime import datetime,  timedelta

#Removendo a DATA do datatime e extraindo só a duração
def filtrar_duracao (tempo):
    t = datetime.strptime(tempo, "%H:%M:%S")
    return timedelta(hours = t.hour, minutes = t.minute, seconds = t.second)


#O formato da hora deve ser "00:00:00" (Hora, Minutos, Segundos)
#Desconto é caso você tenha que descontar algumas horas do trabalho no dia
def tempo_restante(hora_atual:str, horas_totais:str, horas_trabalhadas:str, desconto:str ) -> str:

    hora_atual_ = filtrar_duracao(hora_atual)
    horas_totais_ = filtrar_duracao(horas_totais)
    horas_trabalhadas_hoje_ = filtrar_duracao(horas_trabalhadas)
    desconto_ = filtrar_duracao(desconto)

    restam = horas_totais_ - horas_trabalhadas_hoje_ - desconto_
    trabalhar_ate = hora_atual_ + restam

    return f"Ainda faltam {restam} horas, de acordo com o horário atual {hora_atual}, você deverá trabalhar até às {trabalhar_ate}"

print(tempo_restante("14:50:00", "06:00:00", "01:41:42", "00:30:00"))