pershe_chislo = input("Введіть 1-ше число: ")
diya = input("Введіть дію: ")
druge_chislo = input("Введіть 2-ге число: ")


if int(pershe_chislo) // int(druge_chislo=="0"):
    print('На нуль ділити не можна')
elif diya== "+":
    print(int(pershe_chislo)+int(druge_chislo))
elif diya== "-":
    print(int(pershe_chislo) - int(druge_chislo))
elif diya== "*":
    print(int(pershe_chislo) * int(druge_chislo))
elif diya== ":":
    print(int(pershe_chislo) // float(druge_chislo))

