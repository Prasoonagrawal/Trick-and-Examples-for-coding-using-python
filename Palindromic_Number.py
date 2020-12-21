n=int(input())
rev=0
r=0
t=n
while(t!=0):
    r=t%10
    rev=rev*10+r
    t=t//10
if(rev==n):
    print("Palindromic number")
else:
    print("NOT Palindromic number")
