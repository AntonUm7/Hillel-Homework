# sp=[1,3,5,6,7,8,9]
#
# a = sp [0::2]
#
# if sp == []:
#     print("0")
# else:
#     print ((sum(a))*sp[-1])


sp=[1,2,3,4,5,6]

total=0
result=0
if sp == []:
   print("0")
else:
    for num in sp[0::2]:
        total += num
    result = total* sp[-1]

    print(result)