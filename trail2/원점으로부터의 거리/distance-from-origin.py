n = int(input())
points = [(int(i+1), tuple(map(int, input().split()))) for i in range(n)]
#얘 형태는 지금 (1, (1,1)) 이런 형태로 나온다는 거잖어
# Please write your code here.
points.sort(key=lambda x:abs(x[1][0]) + abs(x[1][1]))

for point in points:
    print(point[0])