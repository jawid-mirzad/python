
# varabler för att komma ihåg namn och ålder

# läsa in namn
name = input("skriv in ditt namn: ")
# lasa in ålder
age = input("Hur gammal är du: ")

# skriva ut hej namn och du är x gammal
print("Hejsan ", name,", välkommen till mitt program.")
print("Du är ", age," gammal")

# skriva ut om du är 18 eller inte

if age < 18:
    print("Du har inte fyllt 18 ännu")
else:
    print("Du har fyllt 18")