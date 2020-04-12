def selection(A):
    n = len(A)
    for i in range(1,n):
        swap = False
        for j in range(0, i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A

A = [2, 3, 1, 2, 5, 9]
selection(A)
print(A)


