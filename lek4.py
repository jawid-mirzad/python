# en slumpgenerator
# program som rullar en tärning

import random # laddar in random klassen så vi kan använda den

print("vill du rulla en tärning?") # meddelande till användaren

# försök läsa in sides som en int, vid fel sätt sides till 1
try:
    sides = int(input("hur många sidor: "))
except:
    print("Tärningen behöver 1+ sidor")
    sides = 1

run = "y" # vi ger run värdet y som standard

# SÅ LÄNGE RUN == y kör loopen
while run.lower() == "y":
    randomNumber = random.randint(1, sides) # slupa ett tal mellan 1 och sides
    print(randomNumber) # skriva ut 

    run = input("vill du rulla en till träning[y/n]: ")
