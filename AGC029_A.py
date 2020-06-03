a=input()
N=list(a)
count=0
AnyOperated=True

while AnyOperated==True:
    temp_count=count
    for n in range(len(N)-1):
        if N[n]=='B' and N[n+1]=='W':
            N[n]='W'
            N[n+1]='B'
            count+=1
        else:
            pass
    if temp_count==count:
        AnyOperated=False
    else:
        pass
    
print(count)
