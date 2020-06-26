
#素因数分解
def prime_factorization(N):
    n=N
    a=2
    prime_factor=[]
    while a**2<=n:
        while n%a==0:
            prime_factor.append(a)
            n//=a
        a+=1
    if n>1:
        prime_factor.append(n)
    return prime_factor


N=100
# N=int(input())

a=1
b=N//a
dis=abs(a-b)

Li=prime_factorization(N)
# print(Li)

for p in range(2**len(Li)):
    bit=[]
    for e in range(len(Li)):
        if (p>>e)&1==1:
            bit.append(1)
        else:
            bit.append(0)
    # print(bit)
        proindex=[]
        for _ in range(len(bit)):
            if bit[_] ==1:
                proindex.append(_)
        _a=1
        for j in range(len(Li)):
            if proindex.count(j)==1:
                _a*=Li[j]
        _b=N//_a
        _dis=abs(_a-_b)
        if _dis<dis:
            a=_a
            b=_b
            dis=_dis
# print(a,b)
print(a-1+b-1)