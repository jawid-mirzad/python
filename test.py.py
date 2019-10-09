
from datetime import datetime

birthday = input("when is your birthday (k/mm/yyyy)? ")
birthday_date = datetime.strptime(birthday, "%d/%m/%Y")
print('birthday: ' + str(birthday_date))
