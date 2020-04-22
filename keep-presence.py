import argparse
import time
from datetime import datetime
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

mouse = MouseController()
keyboard = KeyboardController()

MOVE_MOUSE = False
PRESS_SHIFT_KEY = False
PIXELS_TO_MOVE = 1

move_mouse_every_seconds = 300


def define_custom_seconds():
    global move_mouse_every_seconds, PIXELS_TO_MOVE, PRESS_SHIFT_KEY, MOVE_MOUSE

    parser = argparse.ArgumentParser(
        description="This program moves the mouse or press a key when it detects that you are away. "
                    "It won't do anything if you are using your computer. "
                    "Useful to trick your machine to think you are still working with it.")

    parser.add_argument(
        "-s", "--seconds", type=int,
        help="Define in seconds how long to wait after a user is considered idle. ")

    parser.add_argument(
        "-p", "--pixels", type=int,
        help="Set how many pixels the mouse should move.")

    parser.add_argument(
        "-m", "--mode",
        help="Available options: keyboard, mouse, both; default is mouse. "
             "This is the action that will be executed when the user is idle: "
             "If keyboard is selected, the program will press the shift key. "
             "If mouse is selected, the program will move the mouse. "
             "If both is selected, the program will do both actions. ")

    args = parser.parse_args()
    mode = args.mode

    if args.seconds:
        move_mouse_every_seconds = int(args.seconds)

    if args.pixels:
        PIXELS_TO_MOVE = int(args.pixels)

    is_both_enabled = 'both' == mode
    is_keyboard_enabled = 'keyboard' == mode or is_both_enabled
    is_mouse_enabled = 'mouse' == mode or is_both_enabled or mode is None

    print('--------')
    if is_keyboard_enabled:
        PRESS_SHIFT_KEY = True
        print(get_now_timestamp(), "Keyboard is enabled")

    if is_mouse_enabled:
        MOVE_MOUSE = True
        print(get_now_timestamp(), "Mouse is enabled, moving", PIXELS_TO_MOVE, 'pixels')

    print(get_now_timestamp(), 'Running every', str(move_mouse_every_seconds), 'seconds')
    print('--------')


def move_mouse_when_unable_to_move(expected_mouse_position):
    if expected_mouse_position != mouse.position:
        mouse.position = (0, 0)


def move_mouse():
    new_x = currentPosition[0] + PIXELS_TO_MOVE
    new_y = currentPosition[1] + PIXELS_TO_MOVE

    new_position = (new_x, new_y)
    mouse.position = new_position

    move_mouse_when_unable_to_move(new_position)

    current_position = mouse.position

    print(get_now_timestamp(), 'Moved mouse to: ', current_position)

    return current_position


def press_shift_key():
    keyboard.press(Key.shift)
    keyboard.release(Key.shift)
    print(get_now_timestamp(), 'Shift key pressed')


def get_now_timestamp():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


def execute_keep_awake_action():
    print(get_now_timestamp(), 'Idle detection')

    if MOVE_MOUSE:
        move_mouse()

    if PRESS_SHIFT_KEY:
        press_shift_key()


define_custom_seconds()
lastSavePosition = (0, 0)

while 1:
    currentPosition = mouse.position
    is_user_away = currentPosition == lastSavePosition

    if is_user_away:
        execute_keep_awake_action()
        currentPosition = mouse.position

    if not is_user_away:
        print(get_now_timestamp(), 'User activity detected')

    lastSavePosition = currentPosition

    print('--------')
    time.sleep(move_mouse_every_seconds)
