import networkx as nx


def prince_graph(bd_size):
    prGraph = nx.DiGraph()
    for row in range(bd_size):
        for col in range(bd_size):
            nodeId = pos_to_node_id(row, col, bd_size)
            newPOsitions = genLegalMoves(row, col, bd_size)
            for e in newPOsitions:
                nid = pos_to_node_id(e[0], e[1], bd_size)
                prGraph.add_edge(nodeId, nid)
    return prGraph


def pos_to_node_id(row, column, board_size):
    return (row * board_size) + column


def genLegalMoves(x, y, bd_size):

    newMoves = []
    moveOffsets = [(1, -1), (0, 1), (-1, 0)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legal_coord(newX, bd_size) and legal_coord(newY, bd_size):
            newMoves.append((newX, newY))
    return newMoves


def legal_coord(x, bd_size):

    if x >= 0 and x < bd_size:
        return True
    else:
        return False


def dfs(graph, v):
    visited = [False] * (len(graph))
    # count = [0]*len(graph)
    dfs_1(graph, v, visited)
    for n in visited:
        if n == False:
            return False
    return True


def dfs_1(graph, v, visited):
    visited[v] = True
    # print(v, end=' ')

    for i in graph[v]:
        if visited[i] == False:
            dfs_1(graph, i, visited)

    for n in visited:
        if n == False:
            visited[v] = False
            break


bd_size = int(input("Enter board size: "))

graph = prince_graph(bd_size)
output = [["N" for g in range(0, bd_size)] for i in range(0, bd_size)]
print("DFS starting...")
for row in range(0, bd_size):
    for col in range(0, bd_size):
        if dfs(graph, pos_to_node_id(row, col, bd_size)):
            output[row][col] = "Y"
print("DFS finished...")
for r in range(0, bd_size):
    for c in range(0, bd_size):
        print(output[bd_size - r - 1][c], end=' ')
    print()
