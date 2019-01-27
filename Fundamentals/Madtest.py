map = {
    "size_x":5,
    "size_y":5

}
player = {"x": 1,"y":2}
# enemies = [{"x":3,"y":0},{"x":3,"y":3}]
enemy1 = {"x":3,"y":0}
enemy2 = {"x":3,"y":3}
island = {"x":2,"y":2}
playing = True 
player_is_here_doc = True
statusExplodePlayer = False
statusExplodeEnemy1 = False
statusExplodeEnemy2 = False
Enemy1Shot = False
Enemy2Shot = False
# if xp == xs and yp == ys:
#     statusExplodePlayer = True
# if statusExplodePlayer == True
    
while playing :   
    for y in range (map["size_y"]):
        for x in range(map["size_x"]):
            if x==player["x"] and y == player["y"]:
                if (player_is_here_doc == True and statusExplodePlayer == False): #moi thang enemy phai thoa man 2 dieu kien thi moi in ra ko thi sela else roi print ra "x"
                    print("| ", end=" ")
                elif (player_is_here_doc == False and statusExplodePlayer == False):
                    print("- ", end=" ")
                else:
                    print("X ",end=" ")
            

            elif ((x == enemy1["x"] and y == enemy1["y"] and statusExplodeEnemy1 == False and Enemy1Shot == False) \
            or (x == enemy2["x"] and y == enemy2["y"] and statusExplodeEnemy2 == False and Enemy2Shot == False)) :
                    print("E ",end = " ")

            elif x == island["x"] and y == island["y"]:
                print("S ",end = " ")
            else :
                print("X ",end = " ")
                #shift tab
        print() #xuong dong 
    
    
    
    # for box in boxes :
    #     if(box["x"] == 0 and box["y"] == map["size_y"]-1) \
    #     or (box["x"] == 0 and box["y"] == 0)\
    #     or (box["x"]== map["size_x"]-1 and box["y"] == 0)\
    #     or (box["x"]==map["size_x"]-1 and box["y"] == map["size_y"]-1):
    #         playing = False 
    #         print("You Lose")

    
    move = input("Your next move? A/W/S/D or Fire(F)").lower() 
    dx = 
    dy = 0
    if (move == "a"):
        dx = dx - 1
        player_is_here_doc = False
    elif (move == "w"):
        dy = dy - 1
        player_is_here_doc = True
    elif (move == "s"):
        dy = dy + 1
        player_is_here_doc = True
    elif (move == "d"):
        player_is_here_doc = False
        dx = dx + 1 
    elif (move == "f"): 
        if player_is_here_doc == True :
            if (player["y"] == enemy1["y"]) : 
                Enemy1Shot = True 
            if (player["y"] == enemy2["y"]) :
                Enemy2Shot = True  
        elif player_is_here_doc == False :
            if (player["x"] == enemy1["x"]) : 
                Enemy1Shot = True 
            if (player["x"] == enemy2["x"]) :
                Enemy2Shot = True          



                                                 
    else : 
        playing = False 

    xmove = player["x"] + dx          
    ymove = player["y"] + dy 
# xu ly 1 thang enemy
    if (player["x"]<enemy1["x"]) :
        if dx < 0 : 
            enemy1movex = enemy1["x"] + dx
        else:
            enemy1movex = enemy1["x"] - dx 
    else :
        if dx < 0:
            enemy1movex = enemy1["x"] - dx 
        else:
            enemy1movex = enemy1["x"] + dx  
    if (player["y"]<enemy1["y"]) :
        if dy < 0 : 
            enemy1movey = enemy1["y"] + dy
        else:
            enemy1movey = enemy1["y"] - dy 
    else :
        if dy < 0:
            enemy1movey = enemy1["y"] - dy 
        else:
            enemy1movey = enemy1["y"] + dy
# xu ly thang enemy so 2 
    if (player["x"]<enemy2["x"]) :
        if dx < 0 : 
            enemy2movex = enemy2["x"] + dx
        else:
            enemy2movex = enemy2["x"] - dx 
    else :
        if dx < 0:
            enemy2movex = enemy2["x"] - dx 
        else:
            enemy2movex = enemy2["x"] + dx  
    if (player["y"]<enemy2["y"]) :
        if dy < 0 : 
            enemy2movey = enemy2["y"] + dy
        else:
            enemy2movey = enemy2["y"] - dy 
    else :
        if dy < 0:
            enemy2movey = enemy2["y"] - dy 
        else:
            enemy2movey = enemy2["y"] + dy


    if ((0<= xmove < map["size_x"]) and (0<= ymove <map["size_y"])) : 
        player["x"] += dx 
        player["y"] += dy
    if ((0<= enemy1movex < map["size_x"]) and (0<= enemy1movey <map["size_y"])):      
        enemy1["x"] += dx
        enemy1["y"] += dy
    if ((0<= enemy2movex < map["size_x"]) and (0<= enemy2movey <map["size_y"])): 
        enemy2["x"] += dx
        enemy2["y"] += dy
    if (enemy1["x"] == island["x"] and enemy1["y"] == island["y"]):
        statusExplodeEnemy1 = True
    if (enemy2["x"] == island["x"] and enemy2["y"] == island["y"]):
        statusExplodeEnemy2 = True 
    if (player["x"] == island["x"] and player["y"] == island["y"]):   
        statusExplodePlayer = True  
    
    if(Enemy1Shot == True and Enemy2Shot == True) or (Enemy1Shot == True and statusExplodeEnemy2 == True)\
    or (Enemy2Shot == True and statusExplodeEnemy1 == True) or (statusExplodeEnemy2 == True and statusExplodeEnemy1 == True) :
        print("You Won")
        break
    if (player["y"] == enemy1["y"] and (move == "a" or move == "d")) or \
    (player["y"] == enemy2["y"] and (move == "a" or move == "d")) or \
    (player["x"] == enemy1["x"] and (move == "w" or move == "s")) or \
    (player["x"] == enemy2["x"] and (move == "w" or move == "s")) or\
    (statusExplodePlayer == True):
        print("You lose")
        break 



        
    
        
            
        
    
          