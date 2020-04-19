# Keep Presence

This program moves the mouse 1 pixel or press the shift keyboard key when it detects that you are away. It won't do anything if you are using your computer. Useful to trick your machine to think you are still working with it. 

## Installation

- You need `python3` and `pip3` installed on your computer.
- Execute `pip3 install pynput`

## Run

- `python3 keep-presence.py`

### Command arguments

- `python3 keep-presence.py --seconds 300`. Default is `300` seconds. This define in seconds the allowed idle time. After that time, if mouse wasn't moved, it will move the mouse 1 pixel or press the shift key on the keyboard.
- `python3 keep-presence.py --mode mouse`. Default is `mouse`. modes allowed are `mouse` | `keyboard` | `both`. After idle is detected, what action is needed? Move the mouse, press the shift key or both. 
