queue=[]
GRAPH=[
    [0, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0]
]
BFS_Traversal= [0, 0, 0, 0, 0, 0, 0]
def BFS_METHOD(position):
    print(position,end=" ")
    BFS_Traversal[position]=1
    queue.append(position)
    while(len(queue)!=0):
        element=queue.pop(0)
        for i in range(7):
            if GRAPH[element][i]==1 and BFS_Traversal[i]==0:
                print(i,end=" ")
                BFS_Traversal[i]=1
                queue.append(i)
BFS_METHOD(0)