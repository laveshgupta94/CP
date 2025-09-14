a=list(map(int,input().split()))
for i in range(len(a)):
    a[i],a[len(a)-i-1]=a[len(a)-i-1],a[i]
print(a)

