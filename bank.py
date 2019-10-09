user = "jawid mirzad"
userName = (input("skriva dit användarenam:"))
if user != userName:
    exit()

bank = "Nordia"
bankName = (input("skriv ditt bank"))
if bank != bankName:
    exit()

pin = 1234 # Det är en integer som innehåler heltal och en variabel.

userPin = int(input("Skriv in din pinkod: ")) # Det är en integer som innehåler heltal och en funktion som man kan skriva sitt pinkod.

if pin != userPin: # if "om", vilkorsats för om. pin är inte lika med userPin.
    exit() # stänga av

try: # "försök" try är en undantaghantering som testar ett block av kod för fel.
    with open("balance.txt", "r") as balancefile: # Är en string som öppner balancefilen och kan läsa.
        try: #försök och testar ett block av kod för fel.
            balance = balancefile.readline() # variabel som försökar läsa balancefilen.
            balance = float(balance) # variabel och datatyp för decimaal tal.
        except (ValueError): # undantag att avbryta körning.
            print("ValueError") # köra programet.
            balance = 0.0 # variabel och fload decimaltal.
except (FileNotFoundError): # undantag att avbryta körning.
    balance = 0.0 #variabel lika och fload decimaltal.
menu = 0 # variabel lika med.
# menu 1 insättning
# menu 2 uttag
# menu 3 avsluta
while menu != 3:  #loop som kan köra vidare 
    print("Ditt saldo är: ", balance) # en funktion som kör programet.
    menu = int(input("Skriv ditt val[1,2,3]: ")) # Det är en integer som innehåler heltal och en funktion som man kan skriva en sifra.
    if menu == 1: # vilkor sats för om, om menu är lika med 1. 
        balance = balance + float(input("Gör en insättning: ")) # tilldelningsoperator, datatyp och funktion som vi kan sätta mera sifror. 
    elif menu == 2: # annars om, om det fungerar inte kan hoppa till nästa steg.
        balance = balance - float(input("Gör en utag: ")) # tilldelning, datatyp och funtion som man kan ta ut prngar.
    else:
        print("fel eller avslut")
        try:
            with open("balance.txt","w")as balancefile: # skriva balance.txt om det finns annars skapar en fil med hjälp av "w".
                balancefile.write(str(balance))
        except(FileNotFoundError):
            print("ingen fil")
