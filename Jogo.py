#Função principal
def teste(rex, bob, oli):

    if abs(oli - rex) < abs(oli - bob):
        print('Rex pegou Oli')
    elif abs(oli - bob) < abs(oli - rex):
        print('Bob pegou Oli')
    else:
        print('Oli escapou')

#Função que verifica se os inteiros são positivos
def verifica_entrada(valor):
    if valor < 0:
        print('Informe números inteiros positivos para as posições!')
        return True

#Entrada de dados do usuário
print('Informe 3 números inteiros positivos.')
while True:
    try:
        rex = int(input('Informe a posição de Rex: '))
        if verifica_entrada(rex):
            continue
        bob = int(input('Informe a posição de Bob: '))
        if verifica_entrada(bob):
            continue
        oli = int(input('Informe a posição de Oli: '))
        if verifica_entrada(oli):
            continue
        if rex == oli or bob == oli:
            print('A posição de Oli não pode ser a mesma dos cachorros!')
        break
    except ValueError:
        print('Erro! Informe números inteiros para as posições!')
teste(rex,bob,oli)