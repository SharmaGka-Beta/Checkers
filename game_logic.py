current_player = 1      #for turn based play
flag = []            #flag for multiple captures in a row

def valid_moves(i, j, player, location):        #get a list of avalible moves
    
    if (player == 1):
        new_position = [[i-1, j-1], [i-1, j+1]]         #availible moves
    elif player == 0:
        new_position = [[i+1, j-1], [i+1, j+1]]
    elif player == 2 or player == 3:
        new_position = [[i-1, j-1], [i-1, j+1], [i+1, j-1], [i+1, j+1]]     #king case



    new_position = capture(i, j, location, player, new_position)       #update valid moves if capture is possible

    
    new_position = list(filter(lambda x: -1 < x[0] < 8 and -1 < x[1] < 8, new_position))        #filter out of range moves
    new_position = list(filter(lambda x: location[x[0]][x[1]] == None, new_position))           #filter moves if there is a piece present there

    r = False

    for a in new_position:
        if any(x is True for x in a):           #capture detect
            r = True
            break

    if r:
        temp_new_position = new_position[:]
        for a in temp_new_position:
            if any(x is True for x in a):           #if capture possible then remove all other moves
                continue
            else:
                new_position.remove(a)


    return new_position


def update_location(event, location, i, j, new_i, new_j, redraw, position_holder, player, draw_pieces, player_panel, side_frame, board_size):       #for updating location matrix

    global current_player   
    global flag                                

    new_position = valid_moves(i, j, player, location)  

    r = False    #detect capture

    if abs(new_i - i) == 2:                         
        
        temp_i_location = int((new_i + i)/2)                    #incase of capture
        temp_j_location = int((new_j + j)/2)
        location[temp_i_location][temp_j_location] = None
        r = True


    location[new_i][new_j] = location[i][j]                 #update main matrix
    location[i][j] = None

    if player == 1:
        if new_i == 0:              #reached board end
            location[new_i][new_j] = 3              #made a king
    elif player == 0:
        if new_i == 7:              #reached board end
            location[new_i][new_j] = 2 

    if r:       #capture occured
        again_move_check = valid_moves(new_i, new_j, player, location)      #check if another capture is possible from same piece

        
        flag.clear()            #flag used for multiple capture case

        for x in again_move_check:
            if any(y is True for y in x):
                current_player = current_player ^ 1
                flag.append(new_i)                      #if another capture is possible from same piece then keep turn same and only allow that capture
                flag.append(new_j)
                break


    

    current_player = current_player ^ 1                 #change turn

    player_panel(side_frame, current_player)            #update player panel yellow highlight
    
    redraw(i, j, new_i, new_j, position_holder, new_position, draw_pieces, location, side_frame, board_size)        #update frontend
            
def capture(i, j, location, player, new_position):      #changes incase of capture

    new_position = list(filter(lambda x: -1 < x[0] < 8 and -1 < x[1] < 8, new_position))    #filter out of range moves

    if player > 1:                      #normalize for processing
        player = player - 2
    
    for k in new_position:
        if location[k[0]][k[1]] == (player ^ 1) or location[k[0]][k[1]] == (player ^ 1) + 2:

            k.append(True)          #keep true to track capture for later

            if k[0] == i - 1:
                k[0] = k[0] - 1
            
            elif k[0] == i + 1:
                k[0] = k[0] + 1             #update moves for capture. if capture if blocked by another piece further, it will be filtered out in valid_moves

            if k[1] == j - 1:
                k[1] = k[1] - 1

            elif k[1] == j + 1:
                k[1] = k[1] + 1

    return new_position


def capture_check(location, player):            #check if any capture is possible for player

    capture_moves = []

    if player > 1:                                #normalize for processing
        player = player - 2

    for m in range(8):
        if player in location[m] or player + 2 in location[m]:
            
            
            for n in range(8):                                      #check only lists where player is present
                
                if location[m][n] == None or location[m][n] == (player ^ 1) or location[m][n] == (player ^ 1) + 2:                          
                    continue


                capture_list = valid_moves(m, n, location[m][n], location)      #get valid moves

                
                
                
                for move in capture_list:
                    if any(x is True for x in move):            #if capture is present store move
                        capture_moves.append((m, n))
                
    
    return capture_moves


def winning(location):
    for m in range(8):
        for n in range(8):
            if location[m][n] == 0 or location[m][n] == 2:    #breaks out of loop if red piece is found with legal move     
                valid_red = valid_moves(m, n, location[m][n], location)
                if len(valid_red) > 0:
                    break
        else:
            continue        #return 0 if red has no legal moves
        break
    else:
        return 0

    for m in range(8):
        for n in range(8):
            if location[m][n] == 1 or location[m][n] == 3:    #breaks out of loop if black piece is found with legal move       
                valid_black = valid_moves(m, n, location[m][n], location)
                if len(valid_black) > 0:
                    break
        else:
            continue        #return 1 if black has no legal moves
        break
    else:
        return 1
    
    
    return None
    

    
        





    
