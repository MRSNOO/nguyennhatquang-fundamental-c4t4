map = { 
    "size_x":6,
    "size_y":6


}
player = {"x" : 1,"y" :1}

boxes = [
    {"x":0,"y":2},
    {"x":1,"y":2},
    {"x":3,"y":2},
    {"x":4,"y":2}

]

destinations = [
    {"x":0,"y":3},
    {"x":0,"y":5},
    {"x":1,"y":4},
    {"x":3,"y":5}



]

obstacle = [
    {"x":1,"y":3},
    {"x":4,"y":5}

]
playing = True
while playing : 
    # des_box1 = False
    # des_box2 = False
    # des_box3 = False
    # for des in destinations:
    #     if des["x"] == boxes[0]["x"] and des["y"] == boxes[0]["y"]:
    #         des_box1 = True
    #     elif des["x"] == boxes[1]["x"] and des["y"] == boxes[1]["y"]:
    #         des_box2 = True
    #     elif des["x"] == boxes[2]["x"] and des["y"] == boxes[2]["y"]:
    #         des_box3 = True
    # if des_box1 == True and des_box1 == True and des_box1 == True:
    #     playing = False
    #     print("You win ")
    #     break
    for y in range (map["size_y"]):
        for x in range(map["size_x"]):
            
            box_is_here = False
            for box in boxes:
                if x== box["x"] and y==box["y"]:
                    box_is_here = True
            
            player_is_here = False 
            if x == player["x"] and y == player["y"]:
                player_is_here = True

            destination_is_here = False 
            for des in destinations:
                if x == des["x"] and y ==des["y"]:
                    destination_is_here = True
            obstacle_is_here = False
            for ob in obstacle:
                if x == ob["x"] and y == ob["y"]:
                    obstacle_is_here = True

            if player_is_here == True :
                print("P ",end=" ")
            elif box_is_here == True :
                print("B ", end=" ")
            elif destination_is_here == True:
                print("D ",end=" ")
            elif obstacle_is_here == True:
                print("O ",end=" " )
            else : 
                print("- ", end= " ")

        print()
    # checkwin
    win = True
    for box in boxes:
        if box not in destinations:
            win = False

    if win == True :
        print("You win")
        break
    # checkwin

    for box in boxes:
        if (box["x"] == 0 and box["y"] == map["size_y"]-1)\
        or (box["x"] == 0 and box["y"] == 0)\
        or (box["x"] == map["size_x"]-1 and box["y"] == 0)\
        or (box["x"] == map["size_x"]-1 and box["y"] == map["size_y"]-1):
            playing = False
            print("You Lose")


    move = input("What is your next move: W/A/S/D or Undo(Z)?").lower()

    dx = 0
    dy = 0 

    if move == "w":
        dy = -1 
    elif move == "s":
        dy = 1
    elif move == "a":
        dx = -1
    elif move == "d":
        dx = 1
    else :
        print("Ezzz")
        playing = False
    xmove = player["x"] + dx
    ymove = player["y"] + dy 

    box_is_next = False 
    
    if ((0 <=xmove < map["size_x"]) and ( 0<= ymove < map["size_y"])) :
        # and  ((0 <=box["x"] + dx < map["size_x"])  and ( 0<= box["y"] + dy < map["size_y"])):
        player["x"] += dx
        player["y"] += dy 
    
    
    for box in boxes:
        if box["x"] == player["x"] and box["y"] == player["y"]:
            box["x"] += dx    
            box["y"] += dy
            

        
        if box["x"]>=map["size_x"] or box["x"]<0 or box["y"]>=map["size_y"] or box["y"]<0:
            player["x"] -= dx
            player["y"] -= dy
            box["x"] -= dx    
            box["y"] -= dy
    for box in boxes:
        for ob in obstacle:
            if box["x"] + dx ==ob["x"] and box["y"] + dy==ob["y"]:
                box["x"] -= dx 
                box["y"] -= dy
                player["x"] -= dx
                player["y"] -= dy  
    for ob in obstacle:
        if ob["x"] == player["x"] and ob["y"] == player["y"] :
            player["x"] -= dx
            player["y"] -= dy           
    
        
    
    



        
    
            
        


