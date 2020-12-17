#简单算术运算
print("请输入两个非负整数：用空格隔开")
a,b=map(int,input().split())
c=(float(a*b))**0.5
d=(float(a+b))/2

print('结果是 %0.2f'%(c-d))

