# 计算三角形面积
def cal(a,b,c):
    p=float(a+b+c)/2
    s2=p*(p-a)*(p-b)*(p-c)
    s=s2**0.5
    return s

lst = []

num=int(input())
lst.append(num)
for i in range(num):
    temp = input()
    lst.append([int(i) for i in temp.split(' ')])

out=[]

for i in range(1,num+1):
    ss=cal(lst[i][0], lst[i][1], lst[i][2])
    print(round(ss,2))
