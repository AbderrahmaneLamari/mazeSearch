from pyamaze import maze, agent, textLabel, COLOR
from queue import PriorityQueue

GOAL_CELL = (1,1)
def h(cell1, cell2):
    x1,y1 = cell1
    x2,y2 = cell2

    return abs(x1-x2) + abs(y1-y2)


def aStar(m):
    start = (m.rows, m.cols)
    g_score = {cell:float("inf") for cell in m.grid}
    g_score[start] = 0
    f_score = {cell:float("inf") for cell in m.grid}
    f_score[start] = h(start, GOAL_CELL)

    bSearch = []
    thePath = {}
    
    open = PriorityQueue()
    open.put( ( h(start, GOAL_CELL), h(start, GOAL_CELL), start ) )


    while not open.empty():
        currCell = open.get()[2]

        if currCell == GOAL_CELL:
            break

        for direction in 'ESNW':
            if m.maze_map[currCell][direction]:
                if direction == 'E':
                   childCell = (currCell[0], currCell[1]+1)
                if direction == 'S':
                    childCell = (currCell[0]+1, currCell[1])
                if direction == 'N':
                    childCell = (currCell[0]-1, currCell[1])
                if direction == 'W':
                    childCell = (currCell[0], currCell[1]-1)

                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h(childCell, GOAL_CELL)

                if temp_f_score < f_score[childCell]:
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score
                    open.put(( temp_f_score, h(childCell, GOAL_CELL), childCell ))

                    thePath[childCell] = currCell
                    bSearch.append(childCell)

    forwardPath = {}

    cell = (1,1)
    while cell != start:
        forwardPath[thePath[cell]] = cell
        cell = thePath[cell]

    return thePath, forwardPath, bSearch



def view_aStar(x, y):
    m = maze(x, y)
    m.CreateMaze(loopPercent=50)

    thePath, forwardPath, bSearch = aStar(m)
    a = agent(m, footprints=True, color=COLOR.green, shape='square')
    b = agent(m, footprints=True, color=COLOR.yellow, shape='square', filled=False)
    c = agent(m, 1,1, footprints=True, color=COLOR.cyan, shape='square', filled=True, goal=(m.rows, m.cols))

    l = textLabel(m, 'Path Length', len(forwardPath) + 1)
    l2 = textLabel(m, 'Visited nodes', len(bSearch) + 1)
    m.tracePath({a: bSearch}, delay=50)
    m.tracePath({c: thePath}, delay=50)
    m.tracePath({b: forwardPath}, delay=90)

    m.run()



