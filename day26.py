import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()

def pause():
  pygame.mixer.pause()

pause()

def play():
  # Play the sound
  pygame.mixer.unpause()
 
#print("🎵 MyPOD Music Player")
os.system("clear")
while True:
  # clear the screen
  
  

  # Show the menu
  print("🎼MyPOD Music Player🎼")
  print("""Library
  Press 1 to Play
  Press 2 to Pause
  Press 3 to Exit""")

  # take user's input
  print()
  userResponse = input("\033[32mEnter your choice: \033[00m")

  # check whether you should call the play() subroutine depending on user's input
  
  if userResponse == "1":
    play()
    os.system("clear")
    print("\033[34mPlaying some proper tunes!\033[00m")
  elif userResponse == "2":
    pause()
    os.system("clear")
    print("\033[33mPausing the music!\033[00m")
  elif userResponse == "3":
    os.system("clear")
    print("\033[35mExiting the music player!\033[00m")
    break
    
  else:
    print("Invalid input")
    time.sleep(3)
    os.system("clear")
  time.sleep(3)
  os.system("clear")