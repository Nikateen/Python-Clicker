import sys
import pyautogui
from pynput.keyboard import Key, Listener
import threading



thread_list =[]

def clicker(numberOfIterations, coords):

    for _ in range(numberOfIterations):
        for i in coords:
            x = i[0]
            y = i[1]
            n = i[2]

            for __ in range(int(n)):
                pyautogui.moveTo(int(x), int(y), duration=0.1)
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                print("clicked (" + str(x) + "," + str(y) +")")


def listen():
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def on_press(key):
    #print('{0} pressed'.format(key))
    pass


def on_release(key):
    #print('{0} release'.format(key))

    if str(key) == "'p'":
        thread = threading.Thread(target=clicker,args=( numberOfIterations ,coords, ) )
        thread_list.append(thread)
        thread.start()

    if key == Key.esc:
        # Stop listener
        return False


numberOfIterations = 1
coords = []

if len(sys.argv) > 1:
    if( sys.argv[1].isdigit() ):
        numberOfIterations = sys.argv[1]
    else:
        print("Error!\nnumber of iterations must be a valid number!")
        exit(0)

try:
    f = open("Coordinates.txt","r")

    try:
        for i in f.readlines():
            coords.append(i.split())
    except:
        print("Error!\nCoordinates.txt file is empty!")
        exit(0)

except:
    print("Error!\nCoordinates.txt file not found!")
    exit(0)

thread1 = threading.Thread(target=listen)
thread_list.append(thread1)
thread1.start()






