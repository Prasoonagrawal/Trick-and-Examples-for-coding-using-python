L=[55,34,22,88,67,44,68]
value=91


# Function
def Linear_Search(L,values):
    pos=0
    while(pos<len(L)):
        if(L[pos]==values):
            print("Element found at index: ",pos)
            return
        else:
            pos=pos+1
    print("Element not found!!!")
    return
            
    
Linear_Search(L,value)
