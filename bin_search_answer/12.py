m, n = map(int, input().split())
deer = list(map(int, input().split()))
elves = list(map(int, input().split()))

deer_idx = sorted(range(m), key=lambda i: deer[i])
deer_sorted = [deer[i] for i in deer_idx]

elves_sorted = sorted(elves)

pairs = []
deer_ptr = 0
elf_ptr = 0

while deer_ptr < m and elf_ptr + 1 < n:
    if elves_sorted[elf_ptr] < deer_sorted[deer_ptr] < elves_sorted[elf_ptr + 1]:
        pairs.append((deer_idx[deer_ptr] + 1, elves_sorted[elf_ptr], elves_sorted[elf_ptr + 1]))
        deer_ptr += 1
        elf_ptr += 2
    elif elves_sorted[elf_ptr + 1] <= deer_sorted[deer_ptr]:
        elf_ptr += 1
    else:
        deer_ptr += 1

print(len(pairs))
for d_idx, e1, e2 in pairs:
    e1_idx = elves.index(e1) + 1
    elves[elves.index(e1)] = -1
    e2_idx = elves.index(e2) + 1
    elves[elves.index(e2)] = -1
    print(d_idx, e1_idx, e2_idx)