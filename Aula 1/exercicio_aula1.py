nome_produto = input("Digite o nome do produto: ")
valor_produto = float(input("Digite o valor do produto: "))
produto_desconto = valor_produto * 0.10
produto_com_desconto = valor_produto - produto_desconto
print("Nome do produto é:", nome_produto) 
print("O valor do produto com 10% de desconto é:", produto_com_desconto)

# outra forma
nome_produto = input("Digite o nome do produto: ")
valor_produto = float(input("Digite o valor do produto: "))
produto_com_desconto = valor_produto - (valor_produto * 0.10)

print("Nome do produto é:", nome_produto) 
print("O valor do produto com 10% de desconto é:", produto_com_desconto)