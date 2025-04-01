time1 = (input("Insira o primeiro time"))
gols1 = int (input(f"Insira quantivo de gols do {time1}"))
time2 = (input("Insira o segundo time"))
gols2 = int (input(f"Insira quantitativo de gols do {time2}"))
if gols1 == gols2:
    print("Jogo paia")
else:
    if gols1 > gols2:
        print(f"time {time1} vencedor")
    else:
        print(f"{time2} vencedor")

