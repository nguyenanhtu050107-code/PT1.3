a = [2,3,5,2,4,5,26,6,2,7,8,9,10]
b = []
for i in a:
    if i not in b:
        b.append(i)
b.sort()
print(b)    
