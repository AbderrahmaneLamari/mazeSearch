from a_start_solver import aStar
from bfs_solver import BFS
from dfs_solver import DFS
from pyamaze import maze, agent, textLabel, COLOR
from timeit import timeit

def view_dfs_bfs(x, y):

    M = maze(x, y)
    M.CreateMaze(loopPercent=100)

    dfsPath, dfsForward, dfsSearch = DFS(m = M)
    bfsPath, bfsFroward, bfsSearch = BFS(m=M)
    #aPath, aForward, aSearch = aStar(m = M)

    # Creating Labels
    l1= textLabel(M, "BFS Path lengh: ", len(bfsFroward)+1)
    l2 = textLabel(M, "DFS Path length: ", len(dfsForward) + 1)

    l3 = textLabel(M, "DFS: Blue, BFS: Yellow", "")
    # creating agents
    dfsAgent = agent(M, footprints=True,color=COLOR.cyan)
    bfsAgent = agent(M, footprints=True,color=COLOR.yellow)
    #aAgent = agent(M, footprints=True,color=COLOR.yellow)

    M.tracePath({dfsAgent: dfsForward}, delay=40)
    M.tracePath({bfsAgent: bfsFroward}, delay=40)
   # M.tracePath({aAgent: aForward}, delay=40)

    # Calculating time

    t1 = timeit(stmt=lambda: DFS(M), number=10, globals=globals())
    t2 = timeit(stmt=lambda: BFS(M), number=10, globals=globals())

    lt1 = textLabel(M, "DFS Time: ", t1)
    lt2 = textLabel(M, "BFS Time: ", t2)

    M.run()

