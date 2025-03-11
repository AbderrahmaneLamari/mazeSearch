from pyamaze import agent, maze, COLOR, textLabel



def DFS(m):
    start=(m.rows, m.cols)
    frontier = [start]
    explored = [start]
    bSearch = []
    thePath = {}
    
    while len(frontier) > 0:

        currCell= frontier.pop()
        explored.append(currCell)

        if currCell == (1,1):
            break

        for direction in 'ESNW':
           
            if m.maze_map[currCell][direction] == True:
                if direction == 'E':
                   childCell = (currCell[0], currCell[1]+1)
                elif direction == 'S':
                    childCell = (currCell[0]+1, currCell[1])
                elif direction == 'N':
                    childCell = (currCell[0]-1, currCell[1])
                elif direction == 'W':
                    childCell = (currCell[0], currCell[1]-1)
                
                if childCell in explored:
                    continue

                frontier.append(childCell)
                explored.append(childCell)
                thePath[childCell] = currCell
                bSearch.append(childCell)

    forwardPath = {}

    cell = (1,1)
    while cell != start:
        forwardPath[thePath[cell]] = cell
        cell = thePath[cell]

    return thePath, forwardPath, bSearch

def view_dfs_search(x, y):
    
    m = maze(x, y)
    m.CreateMaze(loopPercent=100)

    thePath, forwardPath, bSearch = DFS(m)
    a = agent(m, footprints=True, color=COLOR.green, shape='square')
    b = agent(m, footprints=True, color=COLOR.yellow, shape='square', filled=False)
    c = agent(m, 1,1, footprints=True, color=COLOR.cyan, shape='square', filled=True, goal=(m.rows, m.cols))

    l = textLabel(m, 'Path Length', len(forwardPath) + 1)
    l2 = textLabel(m, 'Visited nodes', len(bSearch) + 1)
    m.tracePath({a: bSearch}, delay=90)
    m.tracePath({c: thePath}, delay=90)
    m.tracePath({b: forwardPath}, delay=90)

    m.run()
 

