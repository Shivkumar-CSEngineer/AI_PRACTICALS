GRAPH=[
    [0, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0]
]
DFS_Traversal= [0, 0, 0, 0, 0, 0, 0]
def DFS_METHOD(position):
    print(position,end=" ")
    DFS_Traversal[position]=1
    for i in range(7):
        if GRAPH[position][i]==1 and DFS_Traversal[i]==0:
            DFS_Traversal[i]=1
            DFS_METHOD(i)

DFS_METHOD(0)
