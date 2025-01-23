arr = [0] * 31

for i in range(28):
    n = int(input())
    arr[n] = 1

result = []
first_index = arr.index(0, 1)
result.append(first_index)
next_index = first_index+1
next_index = arr.index(0, next_index)
result.append(next_index)

for i in range(len(result)):
    print(result[i])