pin = 1234

userPin = int(input("Skriv in din pinkod: "))

if pin != userPin:
    exit()

saldo = 0.0
menu = 0
# menu 1 saldo
# menu 2 insättning
# menu 2 uttag
# menu 4 avsluta
while menu != 3:
    print("Ditt saldo är: ", saldo)
    menu = int(input("Skriv ditt val[1,2,3]: "))
    if menu == 1:
        saldo = saldo + float(input("Gör en insättning: "))
    elif menu == 2:
        saldo = saldo - float(input("Gör en utag: "))
    else:
        print("fel eller avslut")
    