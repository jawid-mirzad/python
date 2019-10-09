file = open("balance.txt", "r+")
test = file.read()
print(test)

test = input("skriv något: ")

file.write(test)

file.close()
