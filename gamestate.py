from tkinter import *
from tkinter import font
import game_logic
from game_logic import valid_moves, update_location, capture_check, winning
from colours import *

remember_move_oval = {}     #used to keep canvas properties that will be needed later
previous_click = []

def current_player_save(event, root, location, side_frame, board_size): #executed when save button is clocked

    save_label = Canvas(side_frame, bg = frame_colour, highlightthickness = 0, width = int(0.2*board_size), height= int(0.05*board_size))
    save_label.create_text(int(0.1*board_size), int(0.025*board_size), text = 'GAME SAVED', font = ('Consolas', 15))
    save_label.place(x = int(0.15*board_size), y = int(0.73*board_size))
    root.after(1000, save_label.destroy)            #flash game saved for 1 second

    with open('checkers_save.txt', 'w') as f:           #save location matrix and current_player
        for row in location:
            f.write(",".join(map(str, row)) + "\n")

        f.write(str(game_logic.current_player))


def capture_flash(capture_moves, position_holder, root):        #flash the capturing piece

    for m in capture_moves:
        position_holder[m[0]][m[1]].configure(bg = move_colour)

        root.after(100, lambda m = m: position_holder[m[0]][m[1]].configure(bg = bgColour2))

def win(win_condition, side_frame, board_size):

    if win_condition == None:       #nobody is winning
        return
    elif win_condition == 1:        #display red win
        red_win = Canvas(side_frame, bg = frame_colour, highlightthickness = 0,  width = int(0.3*board_size), height = int(0.075*board_size))
        red_win.create_text(int(0.15*board_size), int(0.0375*board_size), text = 'RED WINS', font = ('Consolas', 20), fill = player0colour)
        red_win.place(x = int(0.1*board_size), y = int(0.12*board_size))
    else:                           #display black_win
        black_win = Canvas(side_frame, bg = frame_colour, highlightthickness = 0,  width = int(0.3*board_size), height = int(0.075*board_size))
        black_win.create_text(int(0.15*board_size), int(0.0375*board_size), text = 'BLACK WINS', font = ('Consolas', 20), fill = player1colour)
        black_win.place(x = int(0.1*board_size), y = int(0.805*board_size))
        


def click(event, i, j, player, position_holder, location, board_size, draw_pieces, player_panel, side_frame, root):       #when click on a piece

    capture_moves = capture_check(location, player)               #list of possible captures
    
    if player != game_logic.current_player and (player - 2) != game_logic.current_player:   #dont allow clicks on opponents pieces during your move
        return
    
    if len(game_logic.flag)>0:                                      #flag activated meaning multiple capture present

        if i != game_logic.flag[0] or j != game_logic.flag[1]:      #only allow flag moves
            capture_flash([game_logic.flag], position_holder, root)
            root.after(200, lambda: capture_flash([game_logic.flag], position_holder, root))
            return
    
    if len(capture_moves)>0:                 #if capture is present you must capture
        for c in capture_moves:
            if c[0] == i and c[1] == j:
                break
        else:
            capture_flash(capture_moves, position_holder, root)                 #distinguish capture using flash
            root.after(200, lambda: capture_flash(capture_moves, position_holder, root))
            return
    
    new_position = valid_moves(i, j, player, location)

    position_holder[i][j].configure(bg = move_colour)       #change bg colour of clicked piecee
    
    if len(previous_click)>0:               #change bg colour back to normal of previously clicked piece
        position_holder[previous_click[0]][previous_click[1]].configure(bg = bgColour2)

    
    for canvas, things in remember_move_oval.items():               #clear previously clicked piece attributes
        canvas.delete(things[0])
        canvas.delete(things[1])
        
        
    remember_move_oval.clear()          #clear the disctionary to store the current clicked piece attributes for the next clicked


    if len(previous_click)>0 and previous_click[0] == i and previous_click[1] == j:
        previous_click.clear()              #if same piece is clicked twice, clear the list and return
        return
    else:
        previous_click.clear()

    previous_click.append(i)        #store the clicked piece location for the next click
    previous_click.append(j)

    
    for k in new_position:      #make new attributes
        
        new_i, new_j = k[0], k[1]
        
        #make the little green ovals and buttons on the possible moves
        move_oval = position_holder[new_i][new_j].create_oval(int(board_size/20), int(board_size/20), int((3*board_size)/40), int((3*board_size)/40), fill = move_colour, outline = move_colour)
        move_button = position_holder[new_i][new_j].create_rectangle(0, 0, int(board_size/8), int(board_size/8), outline = "")
        
        position_holder[new_i][new_j].tag_bind(move_button,'<Button-1>', lambda event, new_i = new_i, new_j = new_j, i = i, j = j: update_location(event, location, i, j, new_i, new_j, redraw, position_holder, player, draw_pieces, player_panel, side_frame, board_size))
        
        remember_move_oval[(position_holder[new_i][new_j])] = [move_oval, move_button]      #store the attributes in the dictionary
    

def redraw(i, j, new_i, new_j, position_holder, new_position, draw_pieces, location, side_frame, board_size):       #redraw after move

    for k in new_position:
        if len(k) == 3:                                         #capture is present
            temp_i = int((i + new_i)/2)                         #captured piece coordinates
            temp_j = int((j + new_j)/2)                         
            position_holder[temp_i][temp_j].delete('all')       #remove the captured piece using canvas id
            
    win_condition = winning(location)               #check if somebody has won

    win(win_condition, side_frame, board_size)
            
    
    position_holder[i][j].delete('all')                     #remove the previous piece
    position_holder[i][j].configure(bg = bgColour2)         #change bg colour to normal


    for k in new_position:                                  #remove the little green ovals
        position_holder[k[0]][k[1]].delete('all')


    draw_pieces(new_i, new_j, location, position_holder, side_frame)        #redraw at new location
    

    
    
    



