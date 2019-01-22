from time import sleep
import keyboard
import os
map = {
    "size_x" : 6,
    "size_y" : 6,
}

player = {
    "x": 4,
    "y": 4,
}

boxes = [
    {"x":3,"y":1},
    {"x":1,"y":3},
    {"x":2,"y":2}
]

dests = [
    {"x":4,"y":1},
    {"x":2,"y":3},
    {"x":3,"y":2}
]
playing=True
while playing == True:
    os.system('cls')
    for y in range(map["size_y"]):
        for x in range (map["size_x"]):
            
            Boxhere=False
            for box in boxes:
                if box["x"]==x  and box["y"]==y:
                    Boxhere=True

            playerhere=False
            if x == player["x"] and y == player["y"]:
                playerhere=True
            
            desthere=False
            for destination in dests:
                if destination["x"]==x and destination["y"]==y:
                    desthere=True
            
            if playerhere==True:
                print("P",end=" ")
            
            elif Boxhere==True:
                print("B",end=" ")
            
            elif desthere==True:
                print("D",end=" ")
            
            else:    
                print("-",end=" ")
        print()    

    #inp=input("Input :").lower()
    sleep(0.1) #cái thứ 2 ngăn nó chạy    
    clicka=False
    clicks=False
    clickw=False
    clickd=False
    clicking=True
    while clicking==True:
        if keyboard.is_pressed('a'): 
            clicka=True
            #input() #Không có cái này nó chạy tới cuối map luôn ...
            clicking=False
        elif keyboard.is_pressed('s'):
            clicks=True
            #input()
            clicking=False
        elif keyboard.is_pressed('d'):
            clickd=True
            #input()
            clicking=False
        elif keyboard.is_pressed('w'):
            clickw=True
            #input()
            clicking=False
           
    if clicks:
        #player in map
        if player["y"]+1 <= map["size_y"]-1:
            box_near=False
            for box in boxes:
                
                if box["x"]==player["x"]  and box["y"]==player["y"]+1:
                    box_near=True
                    box_near_box=False
                    for box2 in boxes:
                        if box["x"]==box2["x"] and box["y"]==box2["y"]-1:
                            box_near_box=True
                    if box["y"]+1 <= map["size_y"]-1 and box_near_box==False:
                        player  ["y"] += 1
                        box  ["y"] += 1
            if box_near==False:
                player  ["y"]=player["y"]+1
    
    elif clickd:
        #player in map
        if player["x"]+1 <= map["size_x"]-1:
            box_near=False
            for box in boxes:
                
                if box["x"]==player["x"]+1  and box["y"]==player["y"]:
                    box_near=True
                    box_near_box=False
                    for box2 in boxes:
                        if box["x"]==box2["x"]-1 and box["y"]==box2["y"]:
                            box_near_box=True
                    if box["x"]+1 <= map["size_x"]-1 and box_near_box==False :
                        player  ["x"] += 1
                        box  ["x"] += 1
            if box_near==False:
                player  ["x"]=player["x"]+1
    
    elif clickw:
        #player in map
        if player["y"]-1 >=0 :
            box_near=False
            for box in boxes:
                
                if box["x"]==player["x"]  and box["y"]==player["y"]-1:
                    box_near=True
                    box_near_box=False
                    for box2 in boxes:
                        if box["x"]==box2["x"] and box["y"]==box2["y"]+1:
                            box_near_box=True
                    if box["y"]-1 >=0 and box_near_box==False:
                        player  ["y"] -= 1
                        box  ["y"] -= 1
            if box_near==False:
                player  ["y"]=player["y"]-1
    
    elif clicka:
        #player in map
        if player["x"]-1 >=0 :
            box_near=False
            for box in boxes:
                
                if box["x"]==player["x"]-1  and box["y"]==player["y"]:
                    box_near=True
                    box_near_box=False
                    for box2 in boxes:
                        if box["x"]==box2["x"]+1 and box["y"]==box2["y"]:
                            box_near_box=True
                    if box["x"]-1 >=0 and box_near_box==False:
                        player  ["x"] -= 1
                        box  ["x"] -= 1
            if box_near==False:
                player  ["x"]=player["x"]-1
    
    else:
        input()
        playing=False
    
    
    points=0
    for box_alpha in boxes:
        for dest_alpha in dests:
            if dest_alpha["x"] == box_alpha["x"] and dest_alpha["y"] == box_alpha["y"]:
                points=points+1
    if points==len(boxes):
        for y in range(map["size_y"]):
            for x in range (map["size_x"]):
                
                Boxhere=False
                for box in boxes:
                    if box["x"]==x  and box["y"]==y:
                        Boxhere=True

                playerhere=False
                if x == player["x"] and y == player["y"]:
                    playerhere=True
                
                desthere=False
                for destination in dests:
                    if destination["x"]==x and destination["y"]==y:
                        desthere=True
                
                if playerhere==True:
                    print("P",end=" ")
                
                elif Boxhere==True:
                    print("B",end=" ")
                
                elif desthere==True:
                    print("D",end=" ")
                
                else:    
                    print("-",end=" ")
            print()    
        print("You Won !!")

        playing=False            

