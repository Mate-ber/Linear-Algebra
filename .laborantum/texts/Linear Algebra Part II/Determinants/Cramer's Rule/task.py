import numpy as np
import os
import json_tricks

from pathlib import Path

home_dir = Path(__file__).parent.resolve()

def compute_cofactors(matrix, determinant):
    cofactor = np.linalg.inv(matrix).T * determinant
    return cofactor.astype('int')

# Task 1
A1 = np.array([[1, 1],[1, -1]])
b1 = np.array([2, 0])

det_A1=-2
det_A1_1 = -2
det_A1_2 = -2

x1 = np.array([det_A1_1 / det_A1, det_A1_2 / det_A1]).astype('int')
cofactors1 = compute_cofactors(A1, det_A1)
inverse1 = np.array([[0.5, -0.5], [-0.5, -0.5]])

# Task 2
A2 = np.array([[1, -1],[3, 2]])
b2 = np.array([1, 8])

det_A2 = 5
det_A2_1 = 10
det_A2_2 = 5

x2 = np.array([det_A2_1 / det_A2, det_A2_2 / det_A2]).astype('int')
cofactors2 = compute_cofactors(A2, det_A2)
inverse2 = np.linalg.inv(A2) 
inverse2 *= -1

# Task 3
A3 = np.array([[1, 1, 1],[1, -1, 3],[1, 2, 2]])
b3 = np.array([2, 0, 3])

det_A3 = -4
det_A3_1 = -4
det_A3_2 = -4
det_A3_3 = 0

x3 = np.array([det_A3_1 / det_A3, det_A3_2 / det_A3, det_A3_3 / det_A3]).astype('int')
cofactors3 = compute_cofactors(A3, det_A3)
print(cofactors3)
inverse3 = np.linalg.inv(A3)

answer = {
    "task1": {
        "det_A_terms": ([-1, -1]),
        "det_A_1_terms": ([-2, 0]),
        "det_A_2_terms": ([-2, 0]),
        "x": x1,
        "cofactors": cofactors1,
        "inverse": inverse1
    },
    "task2": {
        "det_A_terms": ([1 * 2, -(-1) * 3]),
        "det_A_1_terms": ([1 * 2, -(-1) * 8]),
        "det_A_2_terms": ([-1 * 3, 1 * (8)]),
        "x": x2, 
        "cofactors": cofactors2,
        "inverse": inverse2
    },
    "task3": {
        "det_A_terms": ([-6, -2, -2, 1, 2, 3]),
        "det_A_1_terms": ([-12, -4, 0, 0, 3, 9]),
        "det_A_2_terms": ([-9, -4, 0, 0, 3, 6]),
        "x": x3,
        "cofactors": cofactors1,
        "inverse": inverse1
    }
}

json_tricks.dump(
    answer,
    open(home_dir / Path('.answer.json'), "w+")
)
