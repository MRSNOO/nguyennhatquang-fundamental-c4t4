map = {
    "size_x":5,
    "size_y":5

}
player = {"x": 1,"y":2}
enemies = [{"x":3,"y":0},{"x":3,"y":3}]
island = {"x":2,"y":2}
playing = True 
enemie_on_island = 0
while playing : 
    for y in range (map["size_y"]):
        for x in range(map["size_x"]):
            
            player_is_here_doc = False 
            if x==player["x"] and y == player["y"]:
                player_is_here_doc = True

            enemies_is_here = False 
            for enemie in enemies :
                if x == enemie["x"] and y == enemie["y"]:
                    enemies_is_here = True
            
            island_is_here = False
            if x == island["x"] and y == island["y"]:
                island_is_here = True

            if player_is_here_doc == True:
                print("| ",end = " ")
            elif (enemies_is_here == True and enemie_on_island == 0):
                print("E ",end = " ")
            elif island_is_here == True:
                print("S ",end = " ")
            else :
                print("x ",end = " ")
        print() #xuong dong 
    
    # for box in boxes :
    #     if(box["x"] == 0 and box["y"] == map["size_y"]-1) \
    #     or (box["x"] == 0 and box["y"] == 0)\
    #     or (box["x"]== map["size_x"]-1 and box["y"] == 0)\
    #     or (box["x"]==map["size_x"]-1 and box["y"] == map["size_y"]-1):
    #         playing = False 
    #         print("You Lose")

    
    move = input("Your next move? A/W/S/D or Fire(F)").lower() 

    dx = 0
    dy = 0
    if (move == "a"): 
        dx = dx - 1
    elif (move == "w"):
        dy = dy - 1 
    elif (move == "s"):
        dy = dy + 1 
    elif (move == "d"):
        dx = dx + 1 
    elif (move == "f"):
        if (player_is_here_doc == True) :
            for i in range(map["size_x"]):
                for enemie in enemies:
                    if (i == enemie["x"]) : 
                        enemie["x"] = player["x"]
                        enemie["y"] = player["y"]                                                     
    else : 
        playing = False 

    xmove = player["x"] + dx 
    ymove = player["y"] + dy 


    if ((0<= xmove < map["size_x"]) and (0<= ymove <map["size_y"])) : 
        player["x"] += dx 
        player["y"] += dy 
        for enemie in enemies:
            enemie["x"] += dx
            enemie["y"] += dy
            if(enemie["x"]>=map["size_x"]):
                enemie["x"] -= 2*dx
            elif(enemie["y"]>=map["size_y"]):
                enemie["y"] -= 2*dy
            elif(enemie["x"]<0):
                enemie["x"] -= 2*dx
            elif(enemie["y"]<0):
                enemie["y"] -= 2*dy
            # elif(enemie["x"]==island["x"] and enemie["y"]==island["y"]):
            #     enemie_on_island = 1


        
    
        
            
        
    
          