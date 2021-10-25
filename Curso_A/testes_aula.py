"""idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if (idade > 18):
    print("Você é maior de idade.")
else:
    if (idade < 12):
        print("Você é uma criança.")
    elif (idade > 12):
        print("Você é um adolescente.")

        ______________________________
        conta = 3//2

print (conta)
print (type(conta))
_____________________
funções de string na documentação de python como letra - min - max - len (length/tamanho-quantidadeTotal)

---- Listas -----
valores = [0,0,0,1,2,3,4,4]
print(valores.count(4)) = 2 # essa função count retorno o numero de vezes que o número informado é encontrado

antes de pedir a posição dentro do index[] - verificar se o item procurado está dentro da lista com IN.


tuple é iniada com (parenteses) lista é iniciada com [colchetes] e o set e dictionary são com {chaves}
o SET {} não tem indice é uma lista desordenada
o dictionary é sempre em par {casa:10, predio:20} lado esquedro(casa) : lado direito (10)

list comprehension é escrever dentro dos [] o code para ação desejada e isso será aplicado as informações daquela lista


        """
inteiros = [1,3,4,5,7,8,9]
pares = [x for x in inteiros if x % 2 == 0]
#pares[] sem o comprehension é um pouco mais longo
#for numero in inteiros:
#    if numero %2 == 0:
#        pares.append(numero)

print(pares)