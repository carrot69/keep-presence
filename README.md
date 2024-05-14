# Keep Presence

This program **moves the mouse** or presses a key when it detects that you are **away** from your computer.

It does nothing if you are using your computer, making it useful for **tricking your machine into thinking you are still using it**.

## Demo

[![Demo](https://raw.githubusercontent.com/carrot69/keep-presence/master/demo/demo.gif)](https://github.com/carrot69/keep-presence)

## Table of Contents

- [Install from Pypi](#install-from-pypi)
- [Install with Snap](#install-with-snap)
- [Manual installation](#manual-installation)
- [Optional arguments](#optional-arguments)
- [FAQ](#faq)
    - [Does it work on Wayland?](#does-it-work-on-wayland)
    - [How can I stop the program after a certain amount of time?](#how-can-i-stop-the-program-after-a-certain-amount-of-time)
    - [Launch Keep-Presence on Startup](#launch-keep-presence-on-startup)
- [Supporting the project](#supporting-the-project)

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

## FAQ: 

### Does it work on Wayland?

No, currently the program doesn't support Wayland due to limitations in the underlying library (pynput). We're actively looking for solutions and will update this FAQ if/when Wayland support is available. You can track progress on the GitHub issue: [GitHub issue](https://github.com/carrot69/keep-presence/issues/2)

### How can I stop the program after a certain amount of time?

Linux offers the timeout command, which allows you to set a maximum runtime for any command.

Example:

```
timeout 30s keep-presence
```

### Launch Keep-Presence on Startup:

1. GNOME: Open "Startup Applications Preferences" (search for it in Activities).
2. KDE Plasma: Search for "Startup Applications" in the Kickoff menu.
3. Click "Add" to create a new entry.
4. In the "Command" field, enter the command to run keep-presence with your desired options. Here's just an example:
5. `keep-presence --circular --seconds 180 --pixels 1`
6. Change the command to fit your needs.

**Using Systemd:**

Alternatively, you can use Systemd to manage Keep-Presence as a startup service. Refer to the official Systemd documentation for detailed instructions on how to set this up.

# Supporting the project:

If you've found Keep Presence to be helpful, you can buy me a coffee, thanks!

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/keep_presence)
