print('######FIBONACCI NUMBER########')
fib=[0,1]
n=int(input('Enter the Number of Series:'))
if(n==0): n=1 
for i in range(n):
    if n<2:
        break
    if i>1:
       # print(i)
        a=fib[i-1]+fib[i-2]
        fib.append(a)
       # print (fib)
print(fib)