def check(m, n, key, Y):
    for _ in range(m*n):
        if Y[i,j] < key:
            i = m
            j = n - 1
        elif Y[i,j] > key:
            i = m - 1
        elif Y[i,j] == key:
            return True
    return False
