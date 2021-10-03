def check(n):
    l = list(str(n))
    s = set(l)
    if len(l)==len(s):
        return True
    return False
    


n1 = int(input())
n2 = int(input())

for i in range(n1,n2+1):
    if check(i):
        print(i)
