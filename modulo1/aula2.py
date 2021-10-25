nome = input('qual seu nome? ')
idade = input('qual sua idade? ')
ano_nasc = 2021 - int(idade) ## colocando a variavel dentro do tipo faço um typecast

print (f'{nome} tem {idade} anos, e nasceu em {ano_nasc}')