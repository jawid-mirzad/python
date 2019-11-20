import random 

nummer = random.randrange(1,10)
gissa = int(input("välje ett nummer mellan 1 till 10:"))

while gissa != nummer:
    if gissa < nummer:
        print("försök igen")
        gissa = int(input("välje ett nummer mellan 1 till 10:"))
    else:
        print("försök ett annat nummer")
        gissa = int(input("välje ett nummer mellan 1 till 10:"))
print("bra du har hittat rätt nummer")