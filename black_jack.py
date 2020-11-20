#fazer um jogo de black jack
import random


def cartas():
    cartas = (2,3,4,5,6,7,8,9,10,'j','q','k','a')
    return random.choice(cartas)

def contador(cartas):
    valor = 0
    for c in cartas:
        if c in ['j','q','k']:
            valor += 10
        elif c == 'a':
            if valor <= 10:
                valor += 1
            else:
                valor += 11
        else:
            valor += c    
    return valor  

def verificador(jogador,valor,show=True):
    if valor < 21:
        if show == True:             #usei para não mostrar as cartas do dealer, e nem fazer a pergunta para o dealer
            print(f'Suas cartas foram:{jogador}\n Teve um total de {valor}.')
            continuar = input('Você quer mais alguma carta? [S/N]').upper().strip()
            while True:
                try:
                    if continuar == 'N':
                        teste = False
                        break
                    elif continuar == 'S':
                        teste = True
                        break
                except:
                    print('Você deve ter digitado errado....')

            return teste
        else:
            if valor > 18:
                teste = False
            else:
                teste = True 
            return teste
                       
    elif valor == 21:
        teste = False
        return teste
    else:
        teste = False
        return teste

valor_jogador = valor_dealer = 0
jogador = [cartas(), cartas()]
dealer = [cartas(), cartas()]
teste = True
while teste:
    valor_jogador = contador(jogador)
    teste = verificador(jogador, valor_jogador)
    if teste:
        jogador.append(cartas())


teste = True

while teste:
    valor_dealer = contador(dealer)
    teste =verificador(dealer,valor_dealer,show=False)
    if teste:
        dealer.append(cartas())

print(f'O jogador teve {valor_jogador} pontos, com as cartas {jogador}')
print(f'O dealer teve {valor_dealer} pontos, com as cartas {dealer}')
