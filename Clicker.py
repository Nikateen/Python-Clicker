import pyautogui

coordinates=[(527,419),(527,419),(539,457)]
findcoords=False
inputcoords=True
executemove=True
moveDuration=0.1
iterations=1



pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True
if findcoords:
    print(pyautogui.position())
if inputcoords:
    f=open('Coords.txt','w')
    for i in coordinates:
        x,y=i
        f.write(str(x)+' '+str(y)+"\n")
    f.close()

if executemove:
    for _ in range(iterations):
        f=open('Coords.txt','r')
        coordList=f.readlines()
        for i in coordList:
            x,y=i.split()
            pyautogui.moveTo(int(x), int(y), duration=moveDuration)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
