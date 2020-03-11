def findPoint(px, py, qx, qy):
    x = qx - px
    y = qy - py
    return [qx +x,qy+y]

n = int(input())
l = []
for n_itr in range(n):
    pxPyQxQy = input().split()
    px = int(pxPyQxQy[0])

    py = int(pxPyQxQy[1])

    qx = int(pxPyQxQy[2])

    qy = int(pxPyQxQy[3])

    result = findPoint(px, py, qx, qy)
    l.append(result)
    
for i in l:
    for j in i:
        print(str(j)+" ", end='')
    print





'''    print(pxPyQxQy)
    px = int(pxPyQxQy[0])

    py = int(pxPyQxQy[1])

    qx = int(pxPyQxQy[2])

    qy = int(pxPyQxQy[3])

    result = findPoint(px, py, qx, qy)

    print(result)'''