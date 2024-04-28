import sys
from collections import deque
import heapq 
import math




dir=[[-1,0],[1,0],[0,-1],[0,1]]
pnt={}
visited=set()

def path_finder():
    current = end
    while True:
        if current == start:
            break

        if current in pnt:
            visited.add(current)
            current = pnt[current]

        else:
            return None

    return

def bfs():
    
    num_col = len(grid[0])
    row = len(grid)
    q = deque([start])

    while q:
        
        current = q.popleft()

        
        for i in dir:
            x = current[0] + i[0]
            y = current[1] + i[1]

            
            if (y < num_col) and (y >= 0) and (x < row) and (x >= 0) and (grid[x][y] != -1) and ((x, y) not in pnt):
                q.append((x, y))
                pnt[(x, y)] = current
            else:
                continue

            if (x, y) == end:
                return

    
    return None

def ucs():

    
    row=len(grid)
    num_col=len(grid[0])
    q=[] 
    st=start[0]
    st1=start[1]
    heapq.heappush(q,[0,(-st,-st1)])
    

    while q:

        
        current=heapq.heappop(q)
        cost=current[0]

        
        for i in range(len(dir)):
            x=-current[1][0]+dir[i][0]
            y=-current[1][1]+dir[i][1]

            
            if (x<0) or (x>=row) or (y<0) or (y>=num_col) or ((x,y) in pnt) or (grid[x][y]==-1):
                continue
            else:
                
                elev_cost=0
                current_cost=0

                if(grid[-current[1][0]][-current[1][1]]<grid[x][y]):
                    elev_cost=grid[x][y]-grid[-current[-(1)][-(0)]][-current[1][1]]
                current_cost=elev_cost+cost+1

                
                heapq.heappush(q,[current_cost,((-x),(-y))])
                pnt[(x,y)]=(-current[1][0],-current[1][1])

            if (x,y)==end:
                return

def manhattan():
    row = len(grid)
    num_col = len(grid[0])
    que = []
    st = start[0]
    st1 = start[1]
    heapq.heappush(que, [0, (-st, -st1)])

    while que:
        current = heapq.heappop(que)
        cost = current[0]

        for dx, dy in dir:
            y = -current[1][1] + dy
            x = -current[1][0] + dx

            if (x < 0) or (x >= row) or (y < 0) or (y >= num_col) or ((x, y) in pnt) or (grid[x][y] == -1):
                elev_cost = 0
                current_cost = 0
                continue
            
            elev_cost = 0
            current_cost = 0

            if grid[x][y] > grid[-current[1][0]][-current[1][1]]:
                elev_cost = -grid[-current[1][0]][-current[1][1]] + grid[x][y]
            current_cost = elev_cost + abs(x + current[1][0]) + abs(y + current[1][1]) + cost + 1

            heapq.heappush(que, [current_cost, (-x, -y)])
            pnt[(x, y)] = (-current[1][0], -current[1][1])

def euclidean():
    row = len(grid)
    num_col = len(grid[0])
    que = []
    st = start[0]
    st1 = start[1]
    heapq.heappush(que, [0, (-st, -st1)])

    while que:
        current = heapq.heappop(que)
        cost = current[0]

        for dx, dy in dir:
            y = -current[1][1] + dy
            x = -current[1][0] + dx

            if ((x, y) in pnt) or (x >= row) or (x < 0) or (y < 0) or (y >= num_col) or (grid[x][y] == -1):
                elev_cost = 0
                current_cost = 0
                continue

            elev_cost = 0
            current_cost = 0

            if grid[-current[1][0]][-current[1][1]] < grid[x][y]:
                elev_cost = -grid[-current[1][0]][-current[1][1]] + grid[x][y]
            current_cost = elev_cost + math.dist([x, y], [end[0], end[1]]) + cost + 1

            heapq.heappush(que, [current_cost, (-x, -y)])
            pnt[(x, y)] = (-current[1][0], -current[1][1])

            if (x, y) == end:
                return



def print_grid():

    if len(visited)==0:
        print("null")

    else:
        for x in range(len(grid)):
            for y in range(len(grid[x])):

                
                current=(x,y)

                
                if(current==start) or (current in visited):
                    print("*", end="")
                elif grid[x][y]==-1:
                    print("X", end="")
                else:
                    print(grid[x][y], end="")

                
                if y!=len(grid[x])-1:
                    print(" ", end="")

            
            print("")
    return



def get_input():

    
    with open(file_path, 'r') as file:
        input = file.read().splitlines()


    num_cols=int(input[0].split()[1])
    num_rows=int(input[0].split()[0])
    s1=int(input[1].split()[0])-1
    e1=int(input[2].split()[0])-1
    s2=int(input[1].split()[1])-1
    e2=int(input[2].split()[1])-1

    
    list=[]
    count=0
    for i in range(num_rows):
        list.append(input[3+count].split())
        count=count+1

    return [(s1,s2),(e1,e2),num_rows,num_cols,list] 



file_path=sys.argv[1]
algorithm=sys.argv[2]


list=get_input()
start=list[0]
end=list[1]
num_rows=list[2]
num_cols=list[3]

grid=[]
for x in range (num_rows):
    grid.append([])
    for y in range (num_cols):
        if list[4][x][y]=='X':
            grid[x].append(-1)
        else:
            grid[x].append(int(list[4][x][y]))




algorithm = sys.argv[2]
heuristic = sys.argv[3] if algorithm == "astar" else None

if algorithm == "bfs":
    bfs()
elif algorithm == "ucs":
    ucs()
elif algorithm == "astar":
    if heuristic == "euclidean":
        euclidean()
    if heuristic == "manhattan":
        manhattan()

path_finder()
print_grid()