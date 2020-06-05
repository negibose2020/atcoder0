N,M=map(int,input().split())
ans=['A']*(N+1)
for i in range(M):
    s,c=map(str,input().split())
    s=int(s)
    if ans[s]=='A' or ans[s]==c :
        ans[s]=c
    else:
        print('-1')
        exit()
if N>1 and ans[1]=='A':
    print('-1')
    exit()
elif N>1 and ans[1]=='0':
    print('-1')
    exit()
else:
    pass
FA=ans[1:]
FA=''.join(FA)
if FA.count('A')>0:
    print(int(FA.replace('A','0')))
    exit()
print(int(FA))
