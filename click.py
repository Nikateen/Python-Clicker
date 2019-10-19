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



def listen():
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def on_press(key):
    print('{0} pressed'.format(
        key))


def on_release(key):
    #print('{0} release'.format(key))

    if str(key) == "'p'":
        thread = threading.Thread(target=clicker,args=( 20 ,[ [10,10,1 ] ], ) )
        thread_list.append(thread)
        thread.start()

    if key == Key.esc:
        # Stop listener
        return False


numberOfIterations = 1


if len(sys.argv) > 1:
    if( sys.argv[1].isdigit() ):
        numberOfIterations = 1
    else:
        print("Error!\nnumber of iterations must be a valid number!")
        exit(0)

thread1 = threading.Thread(target=listen)
thread_list.append(thread1)
thread1.start()






