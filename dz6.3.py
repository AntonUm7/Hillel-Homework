number=999

while number>9:
    zminna=1

    temp = number

    while temp > 0:
        digit = temp % 10
        zminna*=digit
        temp = temp // 10

    number=zminna
print(number)

