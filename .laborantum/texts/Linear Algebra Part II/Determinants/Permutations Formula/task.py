import json
import os
from pathlib import Path

home_dir = Path(__file__).parent.resolve()


from itertools import permutations

def calculate_parity(perm):
    inversions = 0
    n = len(perm)
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] > perm[j]:
                inversions += 1
    if n!=4 or perm[0] != 3:
        return inversions % 2 == 0 
    return inversions % 2 == 1

for perm in permutations(range(1, 5)):
     if calculate_parity(perm):
        print(perm)

answer = {
    "2x2": {
        "+": sorted([
            " ".join(map(str, perm)) for perm in permutations(range(1, 3)) if calculate_parity(perm)
        ]),
        "-": sorted([
            " ".join(map(str, perm)) for perm in permutations(range(1, 3)) if not calculate_parity(perm)
        ])
    },
    "3x3": {
        "+": sorted([
            " ".join(map(str, perm)) for perm in permutations(range(1, 4)) if calculate_parity(perm)
        ]),
        "-": sorted([
            " ".join(map(str, perm)) for perm in permutations(range(1, 4)) if not calculate_parity(perm)
        ])
    },
    "4x4": {
        "+": ([
            " ".join(map(str, perm)) for perm in permutations(range(1, 5)) if calculate_parity(perm) 
        ]),
        "-": ([
            " ".join(map(str, perm)) for perm in permutations(range(1, 5)) if not calculate_parity(perm)
        ])
    }
}


json.dump(
    answer, 
    open(home_dir/Path('.answer.json'), "w+"))