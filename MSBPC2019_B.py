# N=1079
N=int(input())

ans=int(round((N*100/108)+0.1))

if (ans*1.08)//1 == N:
    print(ans)
else:
    print(":(")
