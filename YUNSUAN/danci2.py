
lst = []
temp=input()
lst.append([int(i) for i in temp.split(' ')])


n=int(lst[0][0])
m=int(lst[0][1])


for irun in range(1,n+m+1):
    temp=input()
    lst.append([str(i) for i in temp.split(' ')])

for j in range(n+1,m+n+1):
    jn=0
    for i in range(1,n+1):
        if(lst[i]==lst[j]):
            jn+=1

    if(jn>=1):
        print(jn)
    else:
        print('Not Found!')
