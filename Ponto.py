from datetime import datetime,  timedelta

#Removendo a DATA do datatime e extraindo só a duração
def filtrar_duracao (tempo):
    t = datetime.strptime(tempo, "%H:%M:%S")
    return timedelta(hours = t.hour, minutes = t.minute, seconds = t.second)


#O formato da hora deve ser "00:00:00" (Hora, Minutos, Segundos)
#Desconto é caso você tenha que descontar algumas horas do trabalho no dia
def tempo_restante(hora_inicial:str, horas_totais:str, horas_trabalhadas:str, desconto:str ) -> str:

    hora_inicial_ = filtrar_duracao(hora_inicial)
    horas_totais_ = filtrar_duracao(horas_totais)
    horas_trabalhadas_hoje_ = filtrar_duracao(horas_trabalhadas)
    desconto_ = filtrar_duracao(desconto)

    restam = horas_totais_ - horas_trabalhadas_hoje_ - desconto_
    trabalhar_ate = hora_inicial_ + restam

    return f"""
            Carga horária diária: {horas_totais_}
            Horas já trabalhadas hoje: {horas_trabalhadas_hoje_}
            Ainda faltam: {restam},
            Horário de Início: {hora_inicial}
            Horas descontadas: {desconto_}
            Precisa trabalhar até: {trabalhar_ate}, para atingir as {horas_totais_} horas diárias.
            """

w = input("Que horas pretende iniciar o turno? (Formato de entrada: 00:00:00) ")
x = input("Qual a carga horária diária total? (Formato de entrada: 00:00:00) ")
y = input("Quantas horas já trabalhou hoje? (Formato de entrada: 00:00:00) ")
z = input("Deseja descontar alguma quantidade de horas? (Formato de entrada: 00:00:00) ")


print(tempo_restante(w, x, y,z))