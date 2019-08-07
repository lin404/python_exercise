def bubble(a):
    for r in range(len(a)-1, 0, -1):
        for i in range(r):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]


a = [3, 2, 1]
bubble(a)
print(a)
