sp=[0,5,2,9,0,4,0,6,0,0,7,8]
non_zero = []
zero = []
for i in sp:
    if i>0:
        non_zero.append(i)
        continue
for b in sp:
    if b<1:
        zero.append(b)
        continue
result=non_zero+zero
print(result)

