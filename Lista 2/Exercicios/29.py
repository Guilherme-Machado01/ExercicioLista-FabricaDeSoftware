# Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. 
# As condições para aposentadoria são:
# • Ter pelo menos 65 anos,
# • Ou ter trabalhado pelo menos 30 anos,
# • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade = int(input("Digite a sua idade: "))
tempTrab = float(input("Digite o tempo de serviço: "))

if(idade >= 60 or tempTrab >= 30 or idade >=60 and tempTrab == 25):
    print("Pode se aposentar")
else:
    print("Não pode se aposentar ainda!")