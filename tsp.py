import math
import numpy as np

# Provided list of cities as coordinates
cities = [
    (20833.3333, 17100.0000),
    (20900.0000, 17066.6667),
    (21300.0000, 13016.6667),
    (21600.0000, 14150.0000),
    (21600.0000, 14966.6667),
    (21600.0000, 16500.0000),
    (22183.3333, 13133.3333),
    (22583.3333, 14300.0000),
    (22683.3333, 12716.6667),
    (23616.6667, 15866.6667),
    (23700.0000, 15933.3333),
    (23883.3333, 14533.3333),
    (24166.6667, 13250.0000),
    (25149.1667, 12365.8333),
    (26133.3333, 14500.0000),
    (26150.0000, 10550.0000),
    (26283.3333, 12766.6667),
    (26433.3333, 13433.3333),
    (26550.0000, 13850.0000),
    (26733.3333, 11683.3333),
    (27026.1111, 13051.9444),
    (27096.1111, 13415.8333),
    (27153.6111, 13203.3333),
    (27166.6667, 9833.3333),
    (27233.3333, 10450.0000),
]

nCities = len(cities)

# Initialize the distance matrix
mtrx = np.zeros((nCities, nCities))

# Compute the distance matrix
for i, c1 in enumerate(cities):
    for j, c2 in enumerate(cities):
        if i != j:
            a = c1[0] - c2[0]
            b = c1[1] - c2[1]
            mtrx[i][j] = math.sqrt(a*a + b*b)

# Initialize the DP array
dp = np.full((1 << nCities, nCities), float('inf'))
dp[1, 0] = 0

# Run the DP TSP solver
for i in range(1, 1 << nCities):  # states
    for j in range(nCities):  # current state
        if dp[i, j] == float('inf'): continue
        for k in range(1, nCities):  # cities to visit
            if (i & (1 << k)) != 0: continue
            p = (i | (1 << k))  # new state
            dp[p, k] = min(dp[p, k], dp[i, j] + mtrx[j, k])

# Retrieve the answer
ans = min(dp[(1 << nCities)-1, i] + mtrx[i][0] for i in range(1, nCities))

# Output the answer, rounding down to nearest integer
int(ans)
