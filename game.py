from winsound import Beep
import time

palavra = input("Digite a palavra secreta:").lower().strip()
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("YOU WON!")
        Beep(400, 200)
        Beep(1500, 200)
        Beep(1568,200)
        Beep(1568,200)
        Beep(740,200)
        Beep(784,200)
        Beep(784,200)
        Beep(784,200)
        Beep(370,200)
        Beep(392,200)
        Beep(370,200)
        Beep(392,200)
        Beep(392,400)
        Beep(196,400)
        Beep(740,200)
        Beep(784,200)
        Beep(784,200)
        Beep(740,200)
        Beep(784,200)
        Beep(784,200)
        Beep(740,200)
        Beep(84,200)
        Beep(880,200)
        Beep(831,200)
        Beep(880,200)
        Beep(988,400)
        
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    Beep(1500, 200)
    Beep(1568,200)
    Beep(1568,200)
    if tentativa in digitadas:
        print("You already tried that letter!")
        Beep(392,200)
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("You missed!")
            Beep(2000,400)
            
    print("X==:==\nX  :   ")
    print("X  O   " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |   "
    elif erros == 3:
        linha2 = " /|   "
    elif erros >= 4:
        linha2 = " /|\ "
    print("X%s" % linha2)
    linha3 = ""
    if erros == 5:
        linha3 += " /     "
    elif erros >= 6:
        linha3 += " / \ "
    print("X%s" % linha3)
    print("X\n===========")
    if erros == 6:
        print("GAME OVER")
        Beep(185,200)
        Beep(196,200)
        Beep(185,200)
        Beep(196,200)
        Beep(208,200)
        Beep(220,200)
        Beep(233,200)
        Beep(247,200)

        break
