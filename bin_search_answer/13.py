def time_for_one_trip(t):
    return (Z - U * t) / (V - U)

def total_time_with_k_trips(k):
    if U >= V:
        return float('inf')
    
    time = 0
    remaining = N
    for i in range(k):
        if remaining <= 4:
            travel_time = Z / V
            time += travel_time
            remaining = 0
            break
        else:
            travel_time = Z / V
            time += travel_time
            remaining -= 4
            if remaining > 0:
                meeting_time = time_for_one_trip(travel_time)
                time += meeting_time
    return time

N, V, U, Z = map(float, input().split())
N = int(N)

if U >= V:
    print("{:.10f}".format(Z / U))
else:
    left, right = 0, N
    for _ in range(100):
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        t1 = total_time_with_k_trips(int(mid1) + 1)
        t2 = total_time_with_k_trips(int(mid2) + 1)
        if t1 < t2:
            right = mid2
        else:
            left = mid1

    best_k = int(left) + 1
    answer = min(total_time_with_k_trips(best_k), total_time_with_k_trips(best_k + 1))
    print("{:.10f}".format(answer))