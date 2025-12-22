from sys import stdin, stdout

def solve():
    input = stdin.read().strip().split()
    n = int(input[0])
    arr1 = list(map(int, input[1:1+n]))
    m = int(input[1+n])
    arr2 = list(map(int, input[2+n:2+n+m]))
    
    count_dict = {}
    for num in arr1:
        count_dict[num] = count_dict.get(num, 0) + 1
    
    result = []
    for num in arr2:
        result.append(str(count_dict.get(num, 0)))
    
    stdout.write(' '.join(result))

if __name__ == "__main__":
    solve()