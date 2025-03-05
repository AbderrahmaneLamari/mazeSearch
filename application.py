
from pyamaze import maze
from a_start_solver import view_aStar
from bfs_solver import view_bfs_search
from dfs_solver import view_dfs_search
from comparison import view_dfs_bfs
from comparison2 import view_dfs_aStar

# make option to view bfs search
# make option to view dfs search
# make option to view aStar search
# make option to view bfs vs dfs
# make option to view bfs vs aStar





if __name__ == "__main__":
    

        print("1 - View BFS Search\n",
              "2 - View DFS Search\n",
              "3 - View A* Search\n",
              "4 - View DFS vs BFS\n",
              "5 - View DFS vs A*\n")
        
        try:
            z = int(input("Enter An Option> "))
            x, y = map(int, input("Enter the dimensions x, y: ").split())
            # print(f"First number: {x}, Second number: {y}")
        except:
            print("Enter Valid integer pair for the map size\n")
        if z == 1:
            view_bfs_search(x, y)
        elif z == 2:
            view_dfs_search(x, y)
        elif z == 3:
            view_aStar(x, y)
        elif z == 4:
            view_dfs_bfs(x, y)
        elif z == 5:
            view_dfs_aStar(x, y)


