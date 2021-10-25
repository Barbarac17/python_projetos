nome = 'Barbara'
altura = 1.50
idade = 26
peso = 60
ano_atual = 2021

ano_nasc = ano_atual - idade

imc = peso/(altura * altura)

print (f'{nome} tem {idade} anos, {peso}kg e tem {altura:.2f} de altura')
print (f'seu IMC é {imc:.2f}')
print (f'é nascida em {ano_nasc}')