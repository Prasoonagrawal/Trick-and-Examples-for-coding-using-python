def prime(n):
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                print("Not prime")
                break
        else:
            print("Prime")

    else:
        print("Not Prime")
        
        
n=int(input())
prime(n)
