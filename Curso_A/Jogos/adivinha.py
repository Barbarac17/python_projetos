# com WHILE - enquanto

print ('Bem vindo ao jogo de adivinhação')
numero_secreto = 42
total_de_tentativas = 3
rodada = 1
#em python não existe do_while que é laço de repetição com saida
while(rodada <= total_de_tentativas):
    print("tentativa {} de {}".format(rodada,total_de_tentativas))# essa formação é string interpolation - interpolação de string
    chute = int(input('Digite seu palpite: '))
    print (chute)
    #print (type(chute))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(numero_secreto == chute):
        print('Você acertou')
    else:
        if(maior):
            print('Você errou! seu chute foi MAIOR que o número secreto')
        elif(menor):
            print('Errou! seu chute foi MENOR que o número secreto')

    rodada = rodada + 1

print("Fim de jogo")
