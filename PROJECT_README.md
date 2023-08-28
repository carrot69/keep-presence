# Keep Presence

This program **moves the mouse** or presses a key when it detects that you are **away** from your computer.

It does nothing if you are using your computer, making it useful for **tricking your machine into thinking you are still using it**.

## Demo

[![Demo](https://raw.githubusercontent.com/carrot69/keep-presence/master/demo/demo.gif)](https://github.com/carrot69/keep-presence)

# Install from Pypi

```
python3 -m pip install keep_presence
```
https://pypi.org/project/keep-presence/


### Run

```
keep-presence

# or

python3 -m keep_presence
```

# Install with Snap

```
sudo snap install keep-presence
```

<a href="https://snapcraft.io/keep-presence" target="_blank">
  <img alt="Get it from the Snap Store"
       src="https://snapcraft.io/static/images/badges/en/snap-store-black.svg"
       align="center"
       height="50">
</a>

### Run

```
keep-presence
```

# Manual installation

```
git clone https://github.com/carrot69/keep-presence.git

cd keep-presence

python3 -m pip install pynput

python3 src/keep-presence.py
```

## Optional arguments

```
-h, --help                        show this help message and exit
            
-s SECONDS, --seconds SECONDS     Define in seconds how long to wait after a user is
                                  considered idle. Default 300.

-p PIXELS, --pixels PIXELS        Set how many pixels the mouse should move. Default 1.

-c, --circular                    Move mouse in a circle. Default move diagonally.

-m MODE, --mode MODE              Available options: keyboard, mouse, both (mouse & keyboard) and scroll. 
                                  Default is mouse. 
                                  This is the action that will be executed when the user is idle. 
                                  If keyboard is selected, the program will press the shift key. 
                                  If mouse is selected, the program will move the mouse. 
                                  If both is selected, the program will do both actions.

-r RANDOM RANDOM, --random RANDOM RANDOM
                                  Usage: two numbers (ex. -r 3 10). Execute actions based on a 
                                  random interval between start and stop seconds. 
                                  Note: Overwrites the seconds argument.

```

# Donations:

If you've found Keep Presence to be helpful, you can buy me a coffee, thanks!

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/keep_presence)