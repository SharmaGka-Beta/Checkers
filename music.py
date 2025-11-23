import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'       #hide pygame welcome message

try:
    import pygame
    sound = True
except:
    sound = False

song = 'playback.mp3'

def play_music():
    if sound == False:      #no need if pygame not installed
        return
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(song)       #play music
        pygame.mixer.music.play(-1)

    except:
        pass

def stop_music(root):
    if sound == True:           #no need if pygame not installed

        try:
            pygame.mixer.music.fadeout(2000)
        except:
            pass

    root.destroy()              #remove root on exiting
