nome = input("insira seu nome")
idade = int (input("insira sua idade"))
salario = float (input("insira seu salario"))
aumento = float (input("insira seu salario com aumento"))
porcentagem = (salario*aumento)/100
salariofinal = salario + porcentagem
print(f"OLa {nome} sua idade é {idade} sua grana {salario} seu aumento foi de {porcentagem} seu salario final é de {salariofinal}")
