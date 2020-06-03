N=input()
count=0
AnyOperated=True

while AnyOperated==True:
    temp_count=count
    if N.count('BW')>0:
        count+=N.count('BW')
        newN=N.replace('BW','WB')
        N=newN
    if temp_count==count:
        AnyOperated=False
    else:
        pass

print(count)
