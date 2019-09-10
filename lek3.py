print("Vällkommen till mitt program där du kan räkna")

operator = input("välj räknasätt(+,-,): ")
try:
    tal1 = int(input("Mata in ett heltal: "))
except:
    print("Du måste skriva in en siffra")
    tal1 = 0

try:
    tal2 = int(input("Mata in ett till heltal: "))
except:
    print("Du måste skriva in en siffra")
    tal2 : 0



if operator =="+":
    summa = tal1 + tal2
elif operator == "-":
    summa = (tal1-tal2)
elif operator == "*":
    summa = (tal1*tal2)
else:
     print("FEL")

print ("Summan är:" + str(summa))