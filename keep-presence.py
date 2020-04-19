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
    global move_mouse_every_seconds, PRESS_SHIFT_KEY, MOVE_MOUSE

    parser = argparse.ArgumentParser()

    parser.add_argument("--seconds", "-s", help="define seconds to wait between actions")
    parser.add_argument("--mode", "-m", help="available options: keyboard, mouse, both; default is mouse")

    args = parser.parse_args()
    mode = args.mode

    if args.seconds:
        move_mouse_every_seconds = int(args.seconds)

    is_both_enabled = 'both' == mode
    is_keyboard_enabled = 'keyboard' == mode or is_both_enabled
    is_mouse_enabled = 'mouse' == mode or is_both_enabled or mode is None

    if is_keyboard_enabled:
        PRESS_SHIFT_KEY = True
        print("Keyboard is enabled")

    if is_mouse_enabled:
        MOVE_MOUSE = True
        print("Mouse is enabled")

    print('Running every', str(move_mouse_every_seconds), 'seconds')
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

    print(get_now_timestamp(), 'mouse moved to: ', current_position)

    return current_position


def press_shift_key():
    keyboard.press(Key.shift)
    keyboard.release(Key.shift)
    print(get_now_timestamp(), 'Shift key pressed')


def get_now_timestamp():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


def execute_keep_awake_action():
    if MOVE_MOUSE:
        move_mouse()

    if PRESS_SHIFT_KEY:
        press_shift_key()


define_custom_seconds()
lastSavePosition = (0, 0)

while 1:
    currentPosition = mouse.position

    print(get_now_timestamp(), currentPosition)

    if currentPosition == lastSavePosition:
        execute_keep_awake_action()
        currentPosition = mouse.position

    lastSavePosition = currentPosition

    print('--------')
    time.sleep(move_mouse_every_seconds)
