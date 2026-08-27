# Dadas as 4 notas de um estudante, calcule a media e defina seu status final
# media > 7: Aprovado
# media entre 5 e 7: recuperação
# media < 5: reprovado
nota_1 = float(input("Insira a primeira nota: "))
nota_2 = float(input("Insira a segunda nota: "))
nota_3 = float(input("Insira a terceira nota: "))
nota_4 = float(input("Insira a quarta nota: "))
soma = nota_1 + nota_2 + nota_3 + nota_4
media = soma/4
if media > 7:
    print("média: ", media, "Aprovado")
elif media <= 7 and media >= 5:
    print("média: ", media, "Recuperação")
else:
    print("média: ", media, "Reprovado")
       