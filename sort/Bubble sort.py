def Bubble(A):
    n = len(A)
    for i in range(0,n):
        for j in range (i + 1, n):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    return A

#test
A = [4, 1, 2, 7, 9, 2, 0, 1]
Bubble(A)
print(A)