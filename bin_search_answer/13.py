import math

N, V, U, Z = map(float, input().split())
N = int(N)

if V <= U:
    print(f"{Z/U:.10f}")
else:
    time = 0.0
    remaining = N
    while remaining > 0:
        take = min(4, remaining)
        time += Z / V
        remaining -= take
        if remaining > 0:
            back = min(1, remaining)
            time += Z / V
    trips = math.ceil(N / 4)
    time = Z / V + (trips - 1) * Z / U
    print(f"{time:.10f}")
