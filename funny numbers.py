b=int(input())
a=0
spis=[]

while a<b:
    a+=1
    print(set(str(a)))
    if '4' in set(str(a)) or '7' in set(str(a)):
        spis.append(a)

print(*spis)
