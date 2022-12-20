h = int(input('Digite a hora de inicio: '))
m = int(input('Digite o minuto de inicio: '))
s = int(input('Digite o segundo de inicio: '))
h_d = int(input('Digite a hora duração: '))
m_d = int(input('Digite o minuto duração: '))
s_d = int(input('Digite o segundo de duração: '))
h_f = h + h_d
m_f = m + m_d
s_f = s + s_d
print(f'O experimento terminou com {h_f} horas, {m_f} minutos e {s_f} segundos')
