# AtCoder Beginner Contest 182
# 
'''
a=input()
if int(a)%3==0:
    print(0)
    exit()


N=list(map(int,a))
# N=list(map(int,input()))
mod0=[]
M0=0
mod1=[]
M1=0
mod2=[]
M2=0


for i in range (len(N)):
    m=N[i]%3
    if m==0:
        mod0.append(N[i])
        M0+=1
    elif m==1:
        M1+=1
        mod1.append(N[i])
    else:
        M2+=1
        mod2.append(N[i])

if M1==M2:
    print(0)
    exit()

ans=abs(M1-M2)%3

# if M1>M2:
#     ans=(M1-M2)%3
# else:
#     ans=(M2-M1)%3

if ans==len(N):
    print(-1)
else:
    print(ans)
'''



N=input()
r1=0
r2=0
if int(N)%3==0:
    print(0)
    exit()
for e in N:
    if int(e)%3==0:
        pass
    elif int(e)%3==1:
        r1+=1
    else:
        r2+=1
# print(r1,r2)

if r2<r1:
    r1%=3
    r2%=3
    # print(r1,r2)
    if r1==r2:
        print(0)
        exit()
    ans=abs(r1-r2)
    if ans==len(N):
        print(-1)
    else:
        print(ans)
else:
    ans=(r2-r1)%3
    if ans==len(N):
        print(-1)
    else:
        print(ans)
    
'''
if r1==r2:
    print(0)
    exit()

ans=abs(r1-r2)%3
if ans==len(N):
    print(-1)
else:
    print(ans)
'''