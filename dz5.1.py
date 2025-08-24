import keyword
import string
original=('assert_exception')
underscore=original.count("__")
#
# for a in original:
#     a=count("_")
#     if len(a) > 1:
#         print("False3")

a = False
for i in original:
    if i in string.punctuation and i!="_":
        a = True
        break

if underscore >= 1:
    print("False1")

elif " " in original:
    print("False2")

elif original in keyword.kwlist:
    print("False3")

elif not original.islower() and original != "_":
    print("False4")

elif original.startswith(("1","2","3","4","5","6","7","8","9","0")):
    print("False5")
elif a:
    print("False7")

else:
    print("True")

# elif original in string.punctuation:
#     print("False2")



# for i in original:
#     if i.lower() and not keyword.kwlist:
#         print("True")

# print(keyword.kwlist)
# print(string.punctuation)


