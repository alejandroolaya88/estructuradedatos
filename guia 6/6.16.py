m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
t = [[m[j][i] for j in range(3)] for i in range(3)]
for f in t:
    print(f)