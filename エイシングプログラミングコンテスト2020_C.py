def f(a,b,c):
    n=(a+b+c)**2 -a*b -b*c -c*a
    return n

N=int(input())

anslist=[0]*1000005

for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            n= f(x,y,z)
            anslist[n-1]+=1

for i in range(N):
    print(anslist[i])