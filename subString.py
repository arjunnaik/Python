s = 'Arjun'
l=[]
for i in range(len(s)+1):
    for j in range(i+1,len(s)+1):
        l.append(s[i:j])
        
        
print(l)
