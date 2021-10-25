# com FOR - para ...
def jogar_adivinha():

    import random
    print ("*********************************")
    print ('Bem vindo ao jogo de adivinhação')
    print ("*********************************")
    print('Adivinhhe o número dentro de 01 - 100.')

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Escolha o nível de dificuldade para jogar:")
    print("(1) Fácil (2) Médio (3) Difícil ")

    nivel =  int(input("Escolha o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #em python não precisa usar parenteses mas usamos para facilitar a leitura
    # no for só o range tem () ou usar [] para definir o numero que vai rodar
    # colocar o mais  '+1' dentro do for, se ele não considera/não roda o ultimo numero
    #range é (start, stop, step) inicia, para, pula

    for rodada in range(1, total_de_tentativas +1):
        print("Tentativas {} de {}".format(rodada,total_de_tentativas))# essa formação é string interpolation - interpolação de string
        chute = int(input('Digite seu palpite: '))
        print (chute)
        #print (type(chute))

        if(chute < 1 or chute > 100):
            print("Você tem que digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(numero_secreto == chute):
            print("Você ACERTOU !!! Você fez {} pontos .". format( pontos))
            break
        else:
            pontos_perdidos = abs(chute - numero_secreto)
            pontos = pontos - pontos_perdidos
            if(maior):
                print('Você errou! seu chute foi MAIOR que o número secreto')
                if (rodada == total_de_tentativas):
                    print("o número secreto era {}. Você fez {} pontos .". format(numero_secreto, pontos))
            elif(menor):
                print('Errou! seu chute foi MENOR que o número secreto')
                if (rodada == total_de_tentativas):
                    print("o número secreto era {}. Você fez {} pontos .". format(numero_secreto, pontos))


    print("Numero secreto é: ", numero_secreto)
    print("Pontuação: ", pontos)
    print("Fim de jogo")

if (__name__ == "__main__"):
    jogar_adivinha()
#criado o if name/main para poder ser executado no arquivo que ele está
# DEF é para definir uma função