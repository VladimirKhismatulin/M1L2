#теперь можно генерировать пароли, пока не найдёшь понравившийся
import random
simvols = "+-*!&$#?_@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
a = int(input("Из скольки символов будет пароль?"))
for i in range(a):
    print(random.choice(simvols), end = "")
while True:
    print("")
    a = int(input("Из скольки символов теперь будет пароль?"))
    for i in range(a):
        print(random.choice(simvols), end = "")
