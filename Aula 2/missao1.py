# adquirir os numeros inteiros
numero1 = int(input("digite o primeiro numero inteiro: "))
numero2 = int(input("digite o segundo numero inteiro: "))
numero3 = int(input("digite o terceiro numero inteiro: "))

# primeiro bloco condicional para achar o menor numero
if numero1 < numero2 and numero1 < numero3:
    print("o menor numero é: ", numero1)
else:
    if numero2 < numero1 and numero2 < numero3:
        print("o menor numero é: ", numero2)
    else:
        if numero3 < numero1 and numero3 < numero2:
                print("o menor numero é: ", numero3)

# segundo bloco condicional para achar o numero do meio, fazendo o uso de condicionais compostas "and" e "or"
if numero1 > numero2 and numero1 < numero3 or numero1 < numero2 and numero1 > numero3: 
    print("o numero do meio é: ", numero1)
else:
    if numero2 > numero1 and numero2 < numero3 or numero2 < numero1 and numero2 > numero3: 
        print("o numero do meio é: ", numero2)
    else:
        if numero3 > numero1 and numero3 < numero2 or numero3 < numero1 and numero3 > numero2:
            print("o numero do meio é: ", numero3)

# terceiro blocoo condicional para achar o maior numero
if numero1 > numero2 and numero1 > numero3:
    print("o maior numero é: ", numero1)
else:
    if numero2 > numero1 and numero2 > numero3:
        print("o maior numero é: ", numero2)
    else:
        if numero3 > numero1 and numero3 > numero2:
            print("o maior numero é: ", numero3)