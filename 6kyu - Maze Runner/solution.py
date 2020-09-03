#https://www.codewars.com/kata/58663693b359c4a6560001d6/train/python
def maze_runner(maze, directions):
    action ={"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)} #setting up the directions of the maze in a dictionary
    for a in range(len(maze)):            #locate the starting point of the maze
        for b in range(len(maze)):
            if maze[a][b] == 2:
                y = a
                x = b        
    for d in directions:
        (y2, x2) = action.get(d) #going through the directions and pulling from dictionary the change in coordinates
        y += y2 #new coordinates for X and Y
        x += x2
        if x < 0 or y < 0: #indexing a negative number should be considered dead
            return "Dead"
        try:
            if maze[y][x] == 1: #using "try" to avoid index issues, if the maze hits a wall,we die. If maze hits finish line we win"
                return "Dead"
            elif maze[y][x] == 3:
                return "Finish"
        except:
            return "Dead"
    return "Lost" #if all the directions have been followed but still not dead or finish, then we are lost.
