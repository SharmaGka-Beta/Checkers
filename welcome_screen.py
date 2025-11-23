from tkinter import *
from tkinter import font
from colours import *
import game_logic

def resume(event, welcome_frame, draw_board, initial_screen):
    welcome_frame.destroy()

    try:
        location = []                               #if something is in save file use that
        with open("checkers_save.txt", "r") as f:
            t = 0
            while t <= 7:
                row = []
                for i in f.readline().strip().split(","):
                    if i == 'None':
                        row.append(None)
                    else:
                        row.append(int(i))
                t = t + 1
                        
                location.append(row)
            game_logic.current_player = int(f.readline())
    except:                                         #otherwise play like a new game
        
        location = [[None, 0, None, 0, None, 0, None, 0],
                    [ 0, None, 0, None, 0, None, 0, None ],
                    [None, 0, None, 0, None, 0, None, 0],
                    [None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None],
                    [ 1, None, 1, None, 1, None, 1, None],
                    [None, 1, None, 1, None, 1, None, 1],
                    [ 1, None, 1, None, 1, None, 1, None]]
    
        game_logic.current_player = 1
            
        

    draw_board(location, initial_screen, game_logic.current_player)
        


def start(event, welcome_frame, draw_board, initial_screen):       #start game
    welcome_frame.destroy()


    open("checkers_save.txt", "w").close()                  #clear any previous saved data


    location = [[None, 0, None, 0, None, 0, None, 0],
                [ 0, None, 0, None, 0, None, 0, None ],
                [None, 0, None, 0, None, 0, None, 0],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [ 1, None, 1, None, 1, None, 1, None],
                [None, 1, None, 1, None, 1, None, 1],
                [ 1, None, 1, None, 1, None, 1, None]]
    
    
    
    
    game_logic.current_player = 1
    
    draw_board(location, initial_screen, game_logic.current_player)

def initial_screen(root, board_size, draw_board):       #frontend for main menu

    game_font = font.Font(family = 'Consolas', size = 30)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    welcome_frame = Frame(root, width = int(1.5*board_size), height = board_size, bg = frame_colour)
    welcome_frame.tkraise()
    welcome_frame.grid(column = 0, row = 0, sticky = 'nsew')
    welcome_frame.grid_propagate(False)

    game_name = Canvas(welcome_frame, bg = frame_colour, highlightthickness = 0, width = int(0.8*board_size), height = int(0.15*board_size))
    game_name.create_text(int(0.4*board_size), int(0.075*board_size), text = 'CHECKERS', font = ('Consolas', 80))
    game_name.place(x = int(0.35*board_size), y = int(0.1*board_size))      #big checkers text
    
    new_game = Canvas(welcome_frame, bg = frame_colour, highlightthickness = 0, width = int(0.3*board_size), height = int(0.1*board_size))
    new_game_button = new_game.create_oval(0, 0, int(0.3*board_size), int(0.1*board_size), fill = button_colour, outline = button_colour)
    new_game_text = new_game.create_text(int(0.15*board_size), int(0.05*board_size), text = 'START', font = game_font, fill = button_text_colour)

    new_game.tag_bind(new_game_button, '<Button-1>', lambda event: start(event, welcome_frame, draw_board, initial_screen))
    new_game.tag_bind(new_game_text, '<Button-1>', lambda event: start(event, welcome_frame, draw_board, initial_screen))
    
    new_game.place(x = int(0.6*board_size), y = int(0.35*board_size))       #start button


    resume_game = Canvas(welcome_frame, bg = frame_colour, highlightthickness = 0, width = int(0.3*board_size), height = int(0.1*board_size))
    resume_game_button = resume_game.create_oval(0, 0, int(0.3*board_size), int(0.1*board_size), fill = button_colour, outline = button_colour)
    resume_game_text = resume_game.create_text(int(0.15*board_size), int(0.05*board_size), text = 'RESUME', font = game_font, fill = button_text_colour)

    resume_game.tag_bind(resume_game_button, '<Button-1>', lambda event: resume(event, welcome_frame, draw_board, initial_screen))
    resume_game.tag_bind(resume_game_text, '<Button-1>', lambda event: resume(event, welcome_frame, draw_board, initial_screen))
    
    resume_game.place(x = int(0.6*board_size), y = int(0.5*board_size))     #resume button

    quit_game = Canvas(welcome_frame, bg = frame_colour, highlightthickness = 0, width = int(0.3*board_size), height = int(0.1*board_size))
    quit_game_button = quit_game.create_oval(0, 0, int(0.3*board_size), int(0.1*board_size), fill = button_colour, outline = button_colour)
    quit_game_text = quit_game.create_text(int(0.15*board_size), int(0.05*board_size), text = 'QUIT', font = game_font, fill = button_text_colour)

    quit_game.tag_bind(quit_game_button, '<Button-1>', lambda event: root.quit())
    quit_game.tag_bind(quit_game_text, '<Button-1>', lambda event: root.quit())
    
    quit_game.place(x = int(0.6*board_size), y = int(0.65*board_size))      #quit button

    credit1 = Canvas(welcome_frame, bg = frame_colour, highlightthickness = 0, width = int(0.3*board_size), height = int(0.1*board_size))
    credit1.create_text(int(0.15*board_size), int(0.025*board_size), text = 'NAMAN', font = game_font)
    credit1.create_text(int(0.15*board_size), int(0.075*board_size), text = 'SHARMA', font = game_font)
    credit1.place(x = int(0.06*board_size), y = int(0.85*board_size))       #team member names

    credit2 = Canvas(welcome_frame, bg = frame_colour, highlightthickness = 0, width = int(0.3*board_size), height = int(0.1*board_size))
    credit2.create_text(int(0.15*board_size), int(0.025*board_size), text = 'PRATYUSH', font = game_font)
    credit2.create_text(int(0.15*board_size), int(0.075*board_size), text = 'PRASAD', font = game_font)
    credit2.place(x = int(0.42*board_size), y = int(0.85*board_size))

    credit3 = Canvas(welcome_frame, bg = frame_colour, highlightthickness = 0, width = int(0.3*board_size), height = int(0.1*board_size))
    credit3.create_text(int(0.15*board_size), int(0.025*board_size), text = 'RUSSEL', font = game_font)
    credit3.create_text(int(0.15*board_size), int(0.075*board_size), text = 'GANDHI', font = game_font)
    credit3.place(x = int(0.78*board_size), y = int(0.85*board_size))

    credit4 = Canvas(welcome_frame, bg = frame_colour, highlightthickness = 0, width = int(0.3*board_size), height = int(0.1*board_size))
    credit4.create_text(int(0.15*board_size), int(0.025*board_size), text = 'PARTH', font = game_font)
    credit4.create_text(int(0.15*board_size), int(0.075*board_size), text = 'PANCHAL', font = game_font)
    credit4.place(x = int(1.14*board_size), y = int(0.85*board_size))
