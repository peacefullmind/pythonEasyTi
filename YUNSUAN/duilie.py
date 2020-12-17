
import sys

lst = []
num=int(input())
lst.append(num)

temp=input()
lst = []
lst.append([int(i) for i in temp.split(' ')])


j=0

mylist=lst[0]

alist=[]
for n in mylist:
    alist.append(n)


if(num==1):
    print(j)
    sys.exit(0)

while(len(alist)>1):
    a1 = alist.pop(0)
    a2 = alist.pop(0)
    c = a1 ^ a2
    alist.append(c)
    j+=c
print(j)