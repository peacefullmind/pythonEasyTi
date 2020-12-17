# 查询单词
lst = []

while True:
    temp = input()
    if temp == '':
        break
    lst.append([str(i) for i in temp.split(' ')])

# print(lst)
n=int(lst[0][0])
m=int(lst[0][1])

# for i in range(1,n+1):
#     print(lst[i])
# print('============')
# for j in range(n+1,m+n+1):
#     print(j)
#     print(lst[j])

for j in range(n+1,m+n+1):
    jn=0
    for i in range(1,n+1):
        if(lst[i]==lst[j]):
            jn+=1

    if(jn>=1):
        print(jn)
    else:
        print('Not Found!')
