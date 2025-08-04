sp = []
if len(sp) == 3:
        print([sp[0:2],sp[2:3]])
elif len(sp) == 1:
        print([sp[0],[]])
elif sp ==[]:
    print([sp,sp])
elif len(sp) % 2:
    print([sp[0:3], sp[3:5]])
else:
    print([sp[:3] , sp [3:6]])
