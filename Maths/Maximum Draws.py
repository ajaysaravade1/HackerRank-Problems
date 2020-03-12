def maximumDraws(n):
    return n+1

n = int(input())
l = []
for n_itr in range(n):
    t = int(input())
    
    result = maximumDraws(t)
    l.append(result)
    
for i in l:
    print(str(i)+" ", end='')
    print
