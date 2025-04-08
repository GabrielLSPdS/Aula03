frentista = input(f"Qual o combustivel:\n"
                      f" Etanol\n"
                      f" Gasolina")
qntd = float(input("Quantos litro:"))
G = 5.80
E = 4.90
valor = 0
if frentista == "G" or == "g":
    valor = G*qntd
elif ==
else:
    valor = E*qntd
print(f"Voce gastou R${valor:.2f}")