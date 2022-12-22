chegada_hora = int(input('Digite a hora de chegada: '))
chegada_minuto = int(input('Digite o minuto de chegada: '))
partida_hora = int(input('Digite a hora de partida: '))
partida_minuto = int(input('DIgite o minuto de partida: '))

intervalo_hora = 0

if 0 <= chegada_hora < 24 and 0 <= partida_hora < 24:
    if 0 <= chegada_minuto < 60 and 0 <= partida_minuto < 60:
        if partida_hora == chegada_hora and partida_minuto > chegada_minuto:
            intervalo_hora += 1
        elif partida_hora == chegada_hora and partida_minuto < chegada_minuto:
            intervalo_hora = 24
        elif partida_hora > chegada_hora:
            intervalo_hora = partida_hora - chegada_hora

            if chegada_minuto >= partida_minuto:
                pass
            else:
                intervalo_hora += 1
        else:
            intervalo_hora = 24 - (chegada_hora - partida_hora)
            if chegada_minuto >= partida_minuto:
                pass
            else:
                intervalo_hora += 1
    else:
        print('Minuto inválido')
else:
    print('Hora inválida')
if intervalo_hora > 0:
    print(f'Tempo permanecido no estacionamento: {intervalo_hora} horas')

    if 1 <= intervalo_hora <= 2:
        print('Deve pagar R$ 1,00')
    elif 3 <= intervalo_hora <= 4:
        print('Deve pagar R$ 1,40')
    elif intervalo_hora > 5:
        print('Deve pagar R$ 2,00')
    else:
        print('Erro')
else:
    print('Erro')
