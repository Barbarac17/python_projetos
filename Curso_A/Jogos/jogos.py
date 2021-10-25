import forca
import adivinha2

print ("*********************************")
print ('******* Escolha seu jogo ********')
print ("*********************************")

print ("(1) Forca (2) Adivinhação")

jogo = int(input("Qual o jogo? "))

if (jogo == 1):
    print("Jogar Forca")
    forca.jogar_forca()
elif(jogo == 2):
    print ("Jogar adivinha")
    adivinha2.jogar_adivinha()



print("********** Fim *************")