# desenvolva programa que leia a nota de um aluno (0 a 10) e mostre o conceito correspondente
# >= 9 = conceito A - Excelente!
# >= 7 = conceito B - Bom!
# >= 5 = conceito C - Regular
# else = conceito D - Reprovado
nota = int(input("Indique sua nota: "))
if nota >= 9:
    print("conceito A - Excelente!")
else:
    if nota >= 7:
        print("conceito B - Bom!")
    else:
        if nota >= 5:
            print("conceito C - Regular")
        else:
            print("conceito D - Reprovado")



# teste 1
nota = int(input("Indique sua nota: "))
if nota >10:
    print("valor não autorizado")
else:
    if nota >= 9:
        print("conceito A - Excelente!")
    else:
        if nota >= 7:
            print("conceito B - Bom!")
        else:
            if nota >= 5:
                print("conceito C - Regular")
            else:
                print("conceito D - Reprovado")

# teste 2
nota = int(input("Indique sua nota: "))
if nota >10:
    print("valor não autorizado")
else:
    if nota >= 9:
        print("conceito A - Excelente!")
    else:
        if nota >= 7:
            print("conceito B - Bom!")
        else:
            if nota >= 5:
                print("conceito C - Regular")
            else:
                print("conceito D - Reprovado")


# teste 3
# >= 9 = conceito A - Excelente!
# >= 7 = conceito B - Bom!
# >= 5 = conceito C - Regular
# else = conceito D - Reprovado
nota = int(input("Indique sua nota: "))
if nota >10:
    print("valor não autorizado")
else:
    if nota < 5:
        print("conceito D - Reprovado")
    else:
        if nota > 8 :
            print("conceito A - Excelente!")
        else:
            if nota > 6:
                print("conceito B - Bom!")
            else:
                print("conceito C - Regular")


# com elif
# desenvolva programa que leia a nota de um aluno (0 a 10) e mostre o conceito correspondente
# >= 9 = conceito A - Excelente!
# >= 7 = conceito B - Bom!
# >= 5 = conceito C - Regular
# else = conceito D - Reprovado
print("com elif")
nota = int(input("Indique sua nota: "))
if nota >= 9:
    print("conceito A - Excelente!")
elif nota >= 7:
    print("conceito B - Bom!")
elif nota >= 5:
    print("conceito C - Regular")
else:
    print("conceito D - Reprovado")

# com not
# desenvolva programa que leia a nota de um aluno (0 a 10) e mostre o conceito correspondente
# >= 9 = conceito A - Excelente!
# >= 7 = conceito B - Bom!
# >= 5 = conceito C - Regular
# else = conceito D - Reprovado
print("com not")
nota = int(input("Indique sua nota: "))
if not nota < 11:
    print("valor não autorizado") 
elif not nota < 9:
    print("conceito A - Excelente!")
elif not nota < 7:
    print("conceito B - Bom!")
elif not nota < 5:
    print("conceito C - Regular")
else:
    print("conceito D - Reprovado")