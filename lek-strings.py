firstName = "Jawid"
middleName = "Nej"
lastName = "mirzad"

nickName = "No"

print(firstName [3])

tecken = """()parenteser,
[] hakparenters
{} mååsvingar, krullparenteser
: kolon
; semikolon
, komma
\" dubbelfnutt
\' enkelfnutt"""

print(tecken[13:37])

print(lastName.capitalize())
print(firstName.upper())


# för.efternam
# jawid.mirzad
# firstName[3].lastName[3]
#print(firstName[0:3].lower() + "" + lastName[0:3].lower() + "19")
userName = firstName[0:3].lower()
userName +=lastName[0:3].lower()
userName +="19"
print(userName)


# bygg en elevmails sträng firstName.lastName@elev.ga.ntig.se

print(firstName,lastName)