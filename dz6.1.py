import string

a="a-A"

first=a[0]
last=a[-1]

first_index=string.ascii_letters.index(first)
last_index=string.ascii_letters.index(last)

result=""

while first_index<=last_index:
    result+=string.ascii_letters[first_index]
    first_index += 1
print(result)






