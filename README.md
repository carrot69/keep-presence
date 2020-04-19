# Keep Presence

This is a Python tool that allows you to move the mouse or press the shift keyboard key if it detects that you didn't move the mouse in a settled space of time.

## Installation

- You need `python3` and `pip3` installed on your computer.
- Execute `pip3 install pynput`

## Run

- `python3 keep-presence.py`

### Command arguments

- `python3 keep-presence.py --seconds 300`. Default is `300` seconds. This define in seconds the allowed idle time. After that time, if mouse wasn't moved, it will move the mouse 1 pixel or press the shift key on the keyboard.
- `python3 keep-presence.py --mode mouse`. Default is `mouse`. modes allowed are `mouse` | `keyboard` | `both`. After idle is detected, what action is needed? Move the mouse, press the shift key or both. 
