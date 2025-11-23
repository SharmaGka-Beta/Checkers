from board import root, draw_board, board_size
from music import *
from welcome_screen import initial_screen

#black = 1    king black = 3
#red = 0      king red = 2

play_music()        #music if possible

initial_screen(root, board_size, draw_board)        #make the welcome screen


root.protocol('WM_DELETE_WINDOW', lambda : stop_music(root))        #stop music on exiting
root.mainloop()