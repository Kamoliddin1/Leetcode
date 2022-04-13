from typing import List

def get_rows_cols(array):
    column = len(array[0])
    row = len(array)
    print(f"{row}x{column}")
    return row, column


def spiralOrder(array: List[List[int]]) -> List[int]:
    n, m = get_rows_cols(array)
    spiraled = []
    top, bottom, right, left = 0, n - 1, m - 1, 0
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            spiraled.append(array[top][i])
        top += 1
        for i in range(top, bottom + 1):
            spiraled.append(array[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                spiraled.append(array[bottom][i])
        bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                spiraled.append(array[i][left])
        left += 1
    return spiraled

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))