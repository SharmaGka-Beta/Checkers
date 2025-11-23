from tkinter import *
from tkinter import font
from gamestate import click, current_player_save
from colours import *

root = Tk()

board_size = int((root.winfo_screenheight()*0.8))       #relative to screen


game_font = font.Font(family = 'Consolas', size = 40)
button_font = font.Font(family = 'Consolas', size = 20)


root.title('Checkers')
root.geometry(f'{int(board_size*1.5)}x{board_size}')
root.resizable(False, False)



def player_panel(side_frame , current_player):      #player names

    if current_player == 1:                     #highlight the respective player yellow
        panel_black_colour = panel_colour
        panel_red_colour = frame_colour
    else:
        panel_red_colour = panel_colour
        panel_black_colour = frame_colour

    player_red = Canvas(side_frame, bg = panel_red_colour, highlightthickness = 0, width = int(0.4*board_size), height = int(0.1*board_size))
    
    player_red.create_text(int(0.2*board_size), int(0.05*board_size), text = 'Player 0', font = game_font)
    player_red.place(x = int(0.05*board_size), y = int(0.01*board_size))

    player_black = Canvas(side_frame, bg = panel_black_colour, highlightthickness = 0, width = int(0.4*board_size), height = int(0.1*board_size))
    
    player_black.create_text(int(0.2*board_size), int(0.05*board_size), text = 'Player 1', font = game_font)
    player_black.place(x = int(0.05*board_size), y = int(0.89*board_size))




        

def side_maker(location, side_frame, initial_screen, current_player):     #side panel

    player_panel(side_frame, current_player)    #write the players

    new_button = Canvas(side_frame, bg = frame_colour, highlightthickness = 0, width = int(0.2*board_size), height = int(0.1*board_size))
    new_oval = new_button.create_oval(0, 0, int(0.2*board_size), int(0.1*board_size), fill = button_colour, outline = button_colour)        #main menu button
    new_text = new_button.create_text(int(0.1*board_size), int(0.05*board_size), text = 'MAIN MENU', font = button_font, fill = button_text_colour)
    
    new_button.tag_bind(new_oval, '<Button-1>', lambda event: initial_screen(root, board_size, draw_board))
    new_button.tag_bind(new_text, '<Button-1>', lambda event: initial_screen(root, board_size, draw_board))

    new_button.place(x = int(0.15*board_size), y = int(0.34*board_size))


    save_button = Canvas(side_frame, bg = frame_colour, highlightthickness = 0, width = int(0.2*board_size), height = int(0.1*board_size))
    save_oval = save_button.create_oval(0, 0, int(0.2*board_size), int(0.1*board_size), fill = button_colour, outline = button_colour)          #save button
    save_text = save_button.create_text(int(0.1*board_size), int(0.05*board_size), text = 'SAVE GAME', font = button_font, fill = button_text_colour)
    
    save_button.tag_bind(save_oval, '<Button-1>', lambda event: current_player_save(event, root, location, side_frame, board_size))
    save_button.tag_bind(save_text, '<Button-1>', lambda event: current_player_save(event, root, location, side_frame, board_size))
    
    save_button.place(x = int(0.15*board_size), y = int(0.45*board_size))
    
    
    exit_button = Canvas(side_frame, bg = frame_colour, highlightthickness = 0, width = int(0.2*board_size), height = int(0.1*board_size))
    exit_oval = exit_button.create_oval(0, 0, int(0.2*board_size), int(0.1*board_size), fill = button_colour, outline = button_colour)
    exit_text = exit_button.create_text(int(0.1*board_size), int(0.05*board_size), text = 'QUIT', font = button_font, fill = button_text_colour)

    exit_button.tag_bind(exit_oval, '<Button-1>', lambda event: root.quit())            #exit button
    exit_button.tag_bind(exit_text, '<Button-1>', lambda event: root.quit())
    
    exit_button.place(x = int(0.15*board_size), y = int(0.56*board_size))


def draw_pieces(i, j, location, position_holder, side_frame):       #draw the pieces
    
    if location[i][j] == 1:             #draw the pieces using the location matrix
        black_piece = position_holder[i][j].create_oval(int(board_size/80), int(board_size/80), int((9*board_size)/80), int((9*board_size)/80), fill = player1colour, outline = player1colour)
        position_holder[i][j].tag_bind(black_piece, '<Button-1>', lambda event, i=i, j=j: click(event, i, j, 1, position_holder, location, board_size, draw_pieces, player_panel, side_frame, root))
    
    elif location[i][j] == 0:
        red_piece = position_holder[i][j].create_oval(int(board_size/80), int(board_size/80), int((9*board_size)/80), int((9*board_size)/80), fill = player0colour, outline = player0colour)
        position_holder[i][j].tag_bind(red_piece, '<Button-1>',lambda event, i=i, j=j: click(event, i, j, 0, position_holder, location, board_size, draw_pieces, player_panel, side_frame, root))
    
    elif location[i][j] == 3:
        black_piece = position_holder[i][j].create_oval(int(board_size/80), int(board_size/80), int((9*board_size)/80), int((9*board_size)/80), fill = player1colour, outline = outline_colour, width = 6)
        position_holder[i][j].tag_bind(black_piece, '<Button-1>', lambda event, i=i, j=j: click(event, i, j, 3, position_holder, location, board_size, draw_pieces, player_panel, side_frame, root))
    
    elif location[i][j] == 2:
        red_piece = position_holder[i][j].create_oval(int(board_size/80), int(board_size/80), int((9*board_size)/80), int((9*board_size)/80), fill = player0colour, outline = outline_colour, width = 6)
        position_holder[i][j].tag_bind(red_piece, '<Button-1>', lambda event, i=i, j=j: click(event, i, j, 2, position_holder, location, board_size, draw_pieces, player_panel, side_frame, root))
        

def draw_board(location, initial_screen, current_player):       #draw the main board and side frames
    
    position_holder = [[None for _ in range(8)] for _ in range(8)]      #used to hold canvas ids

    main_frame = Frame(root, width = int(1.5*board_size), height = board_size)
    main_frame.grid(column = 0, row = 0)

    side_frame = Frame(main_frame, width = int(0.5*board_size), height = board_size, bg = frame_colour)
    side_frame.grid(column = 1, row = 0)

    side_maker(location, side_frame, initial_screen, current_player)        #draw the side frame
    
    board_frame = Frame(main_frame, width = board_size, height = board_size)
    board_frame.grid(column = 0, row = 0)

    temp_frame = Frame(main_frame, width = int(1.5*board_size), height = board_size)    #double buffer
    temp_frame.grid(column = 0, row = 0)
    temp_frame.tkraise()
    
    for i in range(8):

        for j in range(8):

            if (i+j)%2 == 0:
                colour = bgColour1
            else:
                colour = bgColour2          #draw the sqaures
            
            position = Canvas(board_frame, bg = colour, height = int(board_size/8), width = int(board_size/8), highlightthickness = 0, bd = 0)

            position_holder[i][j] = position        #store the canvas ids for later access
            
            position.grid(column = j, row = i)
            
            draw_pieces(i, j, location, position_holder, side_frame)        #draw the piece


    root.after(100, lambda: temp_frame.destroy())       #display board after it has been drawn(double buffer)
    

    
    

    


