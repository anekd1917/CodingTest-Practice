# 파이썬 이중리스트 예시

arr = []
# for i in range(3): #row
#     line = []
#     for j in range(4): #col
#         line.append(j)
#     arr.append(line)

for i in range(4):
    line = []
    line.append(0)
    line.append(i)
    arr.append(line)

print(arr)
