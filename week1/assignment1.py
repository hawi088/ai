import numpy as np
# Create a program that:
# 1. Creates a 3D array representing a small apartment building:
#    - 4 floors
#    - 3 apartments per floor
#    - 2 rooms per apartment
#    Store temperature readings for each room (°C)

floor = [
    [
        [12,34],
        [23,56],
        [67,45]
    ],
    [
        [65,45],
        [67,34],
        [54,56]
    ],
    [
        [45,34],
        [45,67],
        [67,76]
    ],
    [
        [87,87],
        [45,34],
        [65,34]
    ]
]

# 2. Generate random temperatures between 18-26°C
rnadomTemp = np.random.randint(18,26)
print(rnadomTemp)