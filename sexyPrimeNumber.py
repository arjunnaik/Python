def isPrime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
        
    


n1 = int(input())
n2 = int(input())

for i in range(n1,n2+1):
    if isPrime(i) and isPrime(i+6) and i+6<n2+1:
        print([i,i+6])
        
        
