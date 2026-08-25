# Casa de show
# Entrada liberada se tem ingresso ou é aniversariante
# Exiba "Entrada liberada!" ou "Precisa comprar ingresso.".
entrada = input("Você tem ingresso, sim ou não? ")
aniversario = input("Hoje é seu aniversário, sim ou não? ")
if entrada =="sim":
    entrada = True
else:
    entrada = False
if aniversario == "sim":
    aniversario = True
else:
    aniversario = False
if entrada == True or aniversario == True:
    print("Entrada liberada!")
else:
    print("Precisa comprar ingresso.")