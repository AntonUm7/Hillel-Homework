pershe_chislo = input("Введіть 1-ше число: ")
diya = input("Введіть дію: ")
druge_chislo = input("Введіть 2-ге число: ")
dali=True

if diya== ":" and druge_chislo=="0":
    print('На нуль ділити не можна')
elif diya== "+":
    print(int(pershe_chislo)+int(druge_chislo))
elif diya== "-":
    print(int(pershe_chislo) - int(druge_chislo))
elif diya== "*":
    print(int(pershe_chislo) * int(druge_chislo))
elif diya== ":":
    print(int(pershe_chislo) / int(druge_chislo))


while dali:
    povtorniy_zapit =input("Бажаєте продовжити? :")
    if povtorniy_zapit != "y" and povtorniy_zapit != "yes":
        print("Дякую за користування калькулятором!")
        break
    if  povtorniy_zapit == "y" and povtorniy_zapit == "yes":
        dali = True
    pershe_chislo = input("Введіть 1-ше число: ")
    diya = input("Введіть дію: ")
    druge_chislo = input("Введіть 2-ге число: ")

    if diya == ":" and druge_chislo == "0":
        print('На нуль ділити не можна')
    elif diya == "+":
        print(int(pershe_chislo) + int(druge_chislo))
    elif diya == "-":
        print(int(pershe_chislo) - int(druge_chislo))
    elif diya == "*":
        print(int(pershe_chislo) * int(druge_chislo))
    elif diya == ":":
        print(int(pershe_chislo) // int(druge_chislo))



