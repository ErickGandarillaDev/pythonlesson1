numero = 100
n=2

for m in range (2,101):
    for n in  range(2,m):
        if m%n==0:
            break
    print (m)
    break        