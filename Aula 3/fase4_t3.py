# brinquedo Radical
# para andar precisa ter 10 anos ou mais e altura igual ou superior a 1.4m
idade = int(input("Qual a sua idade? "))
altura = float(input("Qual a sua altura? "))
if idade < 10 and altura <1.4:
    print("Você não pode entrar nese brinquedo!")
else:
    print("Você pode entrar no brinquedo Radical!")
