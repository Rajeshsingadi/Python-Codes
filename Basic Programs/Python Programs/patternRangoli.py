def print_rangoli(size):
    # your code goes here
    st="abcdefghijklmnopqrstuvwxyz"[0:size]
    for i in range(size-1,-size,-1):
        k=abs(i)
        pattern= st[size:k:-1] + st[k:size] 
        print("--"*k+'-'.join(pattern)+"--"*k)
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)