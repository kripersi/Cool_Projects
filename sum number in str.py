stroka='123 is kr1p but i3s d0nt fas4'
k=0
for i in stroka:
    if i.isdigit():
        k+=int(i)
print(k)
