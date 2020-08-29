#https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python
def adjacency_checker(ardic):
    coord = set()
    for k in ardic:
        for v in ardic[k]: #check for collision and illegal placements, if so, break loop
            if v in coord:
                return False
        for x,y in ardic[k]: #adding all the collision points of current ship to check with future ships.
            coord.update({(x-1,y+1),(x,y+1),(x+1,y+1),(x-1,y),(x+1,y),(x-1,y-1),(x,y-1),(x+1,y-1)})
    return True

def validate_battlefield(field):
    ships_remaining = {"battleship" : 1, "cruiser" : 2, "destroyer" : 3, "submarine" : 4}
    occupied = {0:[],1:[], 2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
    ship = 0
    #We are going to process the board from left to right, and up to down.
    #Any spaces with ship component will be checked with x spaces to the right and y spaces down.
    #After length and direction of the ship is verified (and valid), we will subtract the count from the dictionary.
    for y in range(10):
        for x in range(10):
            if field[y][x] == 1: #ship component locked on; start checking process
                size = 1
                x_check = x + 1
                y_check = y + 1
                if x < 9 and y < 9:  #making sure its not the endpoint
                    if not any((x,y) in v for v in occupied.values()): #check to the skip counter to avoid duplicates
                        try:
                            occupied[ship].append((x,y))
                        except:
                            return False
                        if field[y][x+1] == 1 and field[y+1][x] == 0: #checking one to the right
                            try:
                                while field[y][x_check] == 1:
                                    occupied[ship].append((x_check,y))
                                    x_check += 1
                                    size += 1
                            except:
                                pass
                            if size == 2:
                                ships_remaining["destroyer"] -= 1
                            if size == 3:
                                ships_remaining["cruiser"] -= 1
                            if size == 4:
                                ships_remaining["battleship"] -= 1
                            ship += 1
                        if field[y+1][x] == 1 and field[y][x+1] == 0: #checking one below
                            try:
                                while field[y_check][x] == 1:
                                    occupied[ship].append((x,y_check))
                                    y_check += 1
                                    size += 1
                            except:
                                pass
                            if size == 2:
                                ships_remaining["destroyer"] -= 1
                            if size == 3:
                                ships_remaining["cruiser"] -= 1
                            if size == 4:
                                ships_remaining["battleship"] -= 1
                            ship += 1
                        if field[y+1][x] == 0 and field[y][x+1] == 0: #checking the same spot
                            ships_remaining["submarine"] -= 1
                            ship += 1
                elif x == 9 and y < 9: #If this is the right end bound.
                    if not any((x,y) in v for v in occupied.values()): #check to the skip counter to avoid duplicates
                        try:
                            occupied[ship].append((x,y))
                        except:
                            return False
                        if field[y+1][x] == 1: #checking one below
                            try:
                                while field[y_check][x] == 1:
                                    occupied[ship].append((x,y_check))
                                    y_check += 1
                                    size += 1
                            except:
                                pass
                            if size == 2:
                                ships_remaining["destroyer"] -= 1
                            if size == 3:
                                ships_remaining["cruiser"] -= 1
                            if size == 4:
                                ships_remaining["battleship"] -= 1
                            ship += 1
                        elif field[y+1][x] == 0: #checking the same spot
                            ships_remaining["submarine"] -= 1
                            ship += 1
                elif x < 9 and y == 9: #If this is the bottom bound.
                    if not any((x,y) in v for v in occupied.values()): #check to the skip counter to avoid duplicates
                        try:
                            occupied[ship].append((x,y))
                        except:
                            return False
                        if field[y][x+1] == 1: #checking one to the right
                            try:
                                while field[y][x_check] == 1:
                                    occupied[ship].append((x_check,y))
                                    x_check += 1
                                    size += 1
                            except:
                                pass
                            if size == 2:
                                ships_remaining["destroyer"] -= 1
                            if size == 3:
                                ships_remaining["cruiser"] -= 1
                            if size == 4:
                                ships_remaining["battleship"] -= 1
                            ship += 1
                        elif field[y][x+1] == 0: #checking the same spot
                            ships_remaining["submarine"] -= 1
                            ship += 1               
                elif x == 9 and y == 9: #If this is the bottom right corner.
                    if not any((x,y) in v for v in occupied.values()):
                        try:
                            occupied[ship].append((x,y))
                        except:
                            return False
                        ships_remaining["submarine"] -= 1
                        ship += 1
    return all([v == 0 for v in ships_remaining.values()]) and adjacency_checker(occupied)
