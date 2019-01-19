map = {
    "size_x":4,
    "size_y":4

}
player = {"x": 1,"y":1}
boxes = {"x":2, "y":2}
storages = {"x":2,"y":3}
playing = True 
while playing : 
    for y in range (map["size_y"]):
        for x in range(map["size_x"]):
            player_is_here = False 
            if x==player["x"] and y == player["y"]:
                player_is_here = True

            box_is_here = False 
            if x == boxes["x"] and y == boxes["y"]:
                box_is_here = True
            
            storage_is_here = False
            if x == storages["x"] and y == storages["y"]:
                storage_is_here = True

            if player_is_here == True:
                print("P ",end = " ")
            elif box_is_here == True:
                print("B ",end = " ")
            elif storage_is_here == True:
                print("S ",end = " ")
            else :
                print("- ",end = " ")
        print() #xuong dong 
    win = True
    for box in boxes: 
        if box not in storages: 
            win = False 
    
    if win == True : 
        print("YOU WON !!")
        break
    for box in boxes :
        if(box["x"] == 0 and box["y"] == map["size_y"]-1) \
        or (box["x"] == 0 and box["y"] == 0)\
        or (box["x"]== map["size_x"]-1 and box["y"] == 0)\
        or (box["x"]==map["size_x"]-1 and box["y"] == map["size_y"]-1):
            playing = False 
            print("You Lose")
    move = input("Your next move? A/W/S/D").lower() 

    dx = 0
    dy = 0
    if (move == "A"): 
        dx = dx - 1
    elif (move == "W"):
        dy = dy - 1 
    elif (move == "S"):
        dy = dy + 1 
    elif (move == "D"):
        dx = dx + 1 
    else : 
        playing = False 
    
    xmove = player["x"] + dx 
    ymove = player["y"] + dy 


    if ((0<= xmove < map["size_x"]) and (0<= ymove <map["size_y"])) : 
        player["x"] += dx 
        player["y"] += dy 

    for box in boxes :
        if box["x"] == player["x"] and box["y"] == player["y"]:
            box["x"] += dx 
            box["y"] += dy 
        if box["x"]>=map["size_x"] or box["x"]<0 or box["y"]>=map["size_y"] or box["y"]<0:
            player["x"] -= dx
            player["y"] -= dy
            box["x"] -= dx    
            box["y"] -= dy
        
            
        
    


            