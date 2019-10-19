# Python-Clicker

_Uses python to automate mouse clicks._

## SETUP:
1. Download and install python3: <br />

2. Clone the directory: <br />
run  ```git clone https://github.com/Nikateen/Python-Clicker.git```

3. install requirements: <br />
locate the directory you cloned to on terminal and run  ```pip3 install -f requirements.txt```

## FINDING AND ENTERING COORDINATES:

Each line in the Coordinates.txt file contains the following: <br />
x y n <br />
<br />
this will click the point (x,y) on your screen 'n' times before moving on to the next coordinate <br />
<br />
<br />

**Example:** <br />
10 10 1 <br />
20 20 2 <br />
will click (10,10) 1 time then will click (20,20) 2 times during each iteration of the program.

**To find coordinates on your screen:**
1.  Run the coordFinder script: <br />
    * On Linux/MacOS: ```python3 coordFinder.py```
    * On Windows: ```py coordFinder.py```
2.  hover your mouse over any place on the screen and click 'p' on your keyboard. <br /> This will print the coordinates of your mouse onto the terminal, you can enter these coordinates in Coordinates.txt in the correct format 


## USAGE:
1. Make sure you have entered the coordinates in the correct format (refer above)

3. run click.py:<br />
    * linux/MacOS: ```python3 click.py < number of iterations >```
    * Windows: ```py click.py < number of iterations >```
    * **number of iterations:** specifies how many times the program should repeat the clicks in Coordinates.txt 

4. while script is running, press p to start the clicker.


## IMPORTANT:

1. You may need to grant keyboard and mouse permissions to the script for it to work properly
2. Failsafes: (to stop the clicker at any point of time)
    * Failsafe #1 : press the esc key to end the script
    * Failsafe #2 : quickly move the mouse to the top left of the screen to stop the program
 
