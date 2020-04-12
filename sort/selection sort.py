def selection(A):
    n = len(A)
    for i in range(n):
        mini = i
        for j in range(i + 1, n):
            if A[mini] > A[j]:
                mini = j
        A[mini], A[i] = A[i], A[mini]
    return A

A = [3, 1, 12, 1, 5, 7, 1, 2]
selection(A)
print(A)
