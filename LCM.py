def LCM(a,b):
    greater=max(a,b)

    while(True):
        if(greater%a==0 and greater%b==0):
            LCM=greater
            break
        else:
            greater=greater+1
    return LCM
    
    l=[10,23,35,145,14,524654,2345]
lcm=LCM(l[0],l[1])

for i in range(2,len(l)):
    lcm=LCM(lcm,l[i])
print(lcm)
