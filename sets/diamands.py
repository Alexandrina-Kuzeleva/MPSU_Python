data = input().split()
N = int(data[0])
a = int(data[1])
b = int(data[2])
K = int(data[3])
can_be_real = [True] * N
impossible = False
for i in range(K):
    data = input().split()
    total_weight = int(data[0])
    count = int(data[1])
    stones_idx = [int(x) - 1 for x in data[2:2+count]] 
    numerator = total_weight - count * a
    denominator = b - a
    if numerator % denominator != 0:
        impossible = True
        break
    real_count = numerator // denominator
    if real_count < 0 or real_count > count:
        impossible = True
        break
    if real_count == 0:
        for idx in stones_idx:
            can_be_real[idx] = False

if impossible:
    print("Impossible")
else:
    real_candidates = []
    for i in range(N):
        if can_be_real[i]:
            real_candidates.append(i + 1)  
    if not real_candidates:
        print("Fail")
    else:
        print(len(real_candidates))
        print(" ".join(map(str, real_candidates)))