nota1 = float (input("insira a primeira nota: "))
nota2= float(input("insira segunda nota: "))
nota3= float(input("insira terceira nota:"))
media = (nota1 + nota2 + nota3)/3
print(media)

if media >= 7:
    print("Aprovado")
else:
    if media < 4:
        print("Reprovado")
    else:
        print("Recuperação")
print (f"Sua media {media}")