def funn(n, lst):
    maxi=0
    for i in range(2,len(lst),3):
        if lst[i]>maxi:
            maxi=lst[i]
    s=0
    c=0
    for i in range(2,len(lst),3):
        if lst[i]!=maxi:
            s+=lst[i]
            c+=1
    l1=[]
    l1.append(c)
    l1.append(s)
    return l1
n=int(input())
lst=[]
for i in range(3*n):
    lst.append(int(input()))
l=funn(n,lst)
for i in l:
    print(i)        


