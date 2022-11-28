# Keep Presence

This program moves the mouse or press a key when it detects that you are away.  
It won't do anything if you are using your computer.  
Useful to trick your machine to think you are still working with it. 

## Demo

[![Demo](demo/demo.gif)](https://github.com/carrot69/keep-presence)

## Install with Snap

```
sudo snap install keep-presence
```

<a href="https://snapcraft.io/keep-presence" target="_blank">
  <img alt="Get it from the Snap Store"
       src="https://snapcraft.io/static/images/badges/en/snap-store-black.svg"
       align="center"
       height="50">
</a>

##### Run

```
keep-presence
```

If you don't have the `snap` command available, you might be able to find instructions for your distro [here](https://docs.snapcraft.io/core/install).

## Manual installation

```
git clone https://github.com/carrot69/keep-presence.git
cd keep-presence
pip3 install pynput
python3 src/keep-presence.py
```

## Optional arguments

```
-h, --help                        show this help message and exit
            
-s SECONDS, --seconds SECONDS     Define in seconds how long to wait after a user is
                                  considered idle. Default 300.

-p PIXELS, --pixels PIXELS        Set how many pixels the mouse should move. Default 1.

-c, --circular                    Move mouse in a circle. Default move diagonally.

-m MODE, --mode MODE              Available options: keyboard, mouse, both; default is mouse. 
                                  This is the action that will be executed when the user is idle. 
                                  If keyboard is selected, the program will press the shift key. 
                                  If mouse is selected, the program will move the mouse. 
                                  If both is selected, the program will do both actions.

-r RANDOM RANDOM, --random RANDOM RANDOM
                                  Usage: two numbers (ex. -r 3 10). Execute actions based on a 
                                  random interval between start and stop seconds. 
                                  Note: Overwrites the seconds argument.

```
