# Interview Question :

from collections import deque
def rotate_matrix_clockwise(mat, k):
    n = len(mat)
    layers = n

    for layer in range(layers):
        dq = deque()

        top = left = layer
        bottom = right = n-layer-1

        # Rotating the matrix by value :
        for j in range(left, right+1):
            dq.append(mat[top][j])

        for i in range(top+1, bottom):
            dq.append(mat[i][right])

        if(bottom != top):
            for j in range(right, left-1, -1):
                dq.append(mat[bottom][j])

        for i in range(bottom-1, top, -1):
            dq.append(mat[i][left])

        dq.rotate(k)

        # Rotating the index value :
        idx = 0
        for j in range(left, right+1):
            mat[top][j] = dq[idx]
            idx += 1

        for i in range(top+1, bottom):
            mat[i][right] = dq[idx]
            idx +=1

        if bottom != top:
            for j in range(right, left-1, -1):
                mat[bottom][j] = dq[idx]
                idx +=1
            
        for i in range(bottom-1, top, -1):
            mat[i][left] = dq[idx]
            idx += 1

    return mat

matrix_4x4 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

k = int(input("Enter the k shift : "))
print("The original matrix : ")
for x in matrix_4x4:
    print(x)
print("The Rotated matrix : ")
for x in rotate_matrix_clockwise(matrix_4x4, k):
    print(x)