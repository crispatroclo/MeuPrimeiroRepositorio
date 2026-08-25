# programa que le a idade de uma pessoa
# se ela tiver 18 anos ou mais, exiba "Você pode dirigir e votar!".
# caso contrario, exiba, "Você ainda é menor de idade.".
idade = int(input("Qual a sua idade? "))
if idade >= 18:
    print("Você pode dirigir e votar!")
else:
    print("Você ainda é menor de idade.")

# teste
# programa que le a idade de uma pessoa
# se ela tiver 18 anos ou mais, exiba "Você pode dirigir e votar!".
# caso contrario, exiba, "Você ainda é menor de idade.".
idade = int(input("Qual a sua idade? " ))
if idade >= 18:
    print("Você pode dirigir e votar!")
else:
    if idade <18 and idade >= 16:
        print("Você pode votar, mas não pode dirigir!")
    else:
        print("Você não pode dirigir nem votar!")

# teste
# programa que le a idade de uma pessoa
# se ela tiver 18 anos ou mais, exiba "Você pode dirigir e votar!".
# caso contrario, exiba, "Você ainda é menor de idade.".
idade = int(input("Qual a sua idade? " ))
if idade >= 18:
    print("Você pode dirigir e votar!")
else:
    if idade <18 and not idade < 16:
        print("Você pode votar, mas não pode dirigir!")
    else:
        print("Você não pode dirigir nem votar!")
