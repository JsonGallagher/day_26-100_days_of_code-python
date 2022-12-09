from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  print()
  print("Playing some tunes!")
  while True:
    # Start taking user input and doing something with it
    stop_playback = int(input("Press 0 to stop playback and return to the menu. "))
    if stop_playback == 0:
      source.paused = True
      print("Playback stopped. Returning to main menu.")
      time.sleep(1)
      return
    else:
      continue
      
# check whether you should call the play() subroutine depending on user's input
while True:
  # clear the screen 
  os.system("clear")
  # Show the menu
  # take user's input
  print("🎵 MyPOD Music Player 🎵")
  print()
  time.sleep(1)
  print("Press 1 to play music")
  time.sleep(.5)
  print("Press 2 to exit")
  time.sleep(.5)
  print("Press 3 to reload the menu")
  print()
  time.sleep(.5)
  control = int(input(">>> "))
  if control == 1:
    play()
  elif control == 2:
    exit()
  elif control == 3:
    continue
  else:
    print("Input invalid.")