"""A module for simulating low-level keyboard and mouse key presses."""

# import ctypes
# import time
# from cv2 import split
# import win32con
# import win32api
from src.common import utils, settings
# from ctypes import wintypes
# from random import random
import random
# from pynput.keyboard import Key, Controller
# import win32gui, win32ui, win32con, win32api
# import win32process

from src.bumblebee.initinterception import keydown, keyup, keyupall, keydown_arrow, keyup_arrow, keyupall_arrow, sleep, sleeplol


# record unreleased key for stopping script
unreleased_key = []

# https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes?redirectedfrom=MSDN
KEY_MAP = {
    'left': 0x25,   # Arrow keys
    'up': 0x26,
    'right': 0x27,
    'down': 0x28,

    'backspace': 0x08,      # Special keys
    'tab': 0x09,
    'enter': 0x0D,
    'shift': 0x10,
    'ctrl': 0x11,
    'alt': 0x12,
    'caps lock': 0x14,
    'esc': 0x1B,
    'space': 0x20,
    'pageup': 0x21,
    'pagedown': 0x22,
    'end': 0x23,
    'home': 0x24,
    'insert': 0x2D,
    'delete': 0x2E,

    '0': 0x30,      # Numbers
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,

    'a': 0x41,      # Letters
    'b': 0x42,
    'c': 0x43,
    'd': 0x44,
    'e': 0x45,
    'f': 0x46,
    'g': 0x47,
    'h': 0x48,
    'i': 0x49,
    'j': 0x4A,
    'k': 0x4B,
    'l': 0x4C,
    'm': 0x4D,
    'n': 0x4E,
    'o': 0x4F,
    'p': 0x50,
    'q': 0x51,
    'r': 0x52,
    's': 0x53,
    't': 0x54,
    'u': 0x55,
    'v': 0x56,
    'w': 0x57,
    'x': 0x58,
    'y': 0x59,
    'z': 0x5A,

    'f1': 0x70,     # Functional keys
    'f2': 0x71,
    'f3': 0x72,
    'f4': 0x73,
    'f5': 0x74,
    'f6': 0x75,
    'f7': 0x76,
    'f8': 0x77,
    'f9': 0x78,
    'f10': 0x79,
    'f11': 0x7A,
    'f12': 0x7B,
    'num lock': 0x90,
    'scroll lock': 0x91,

    ';': 0xBA,      # Special characters
    '=': 0xBB,
    ',': 0xBC,
    '-': 0xBD,
    '.': 0xBE,
    '/': 0xBF,
    '`': 0xC0,
    '[': 0xDB,
    '\\': 0xDC,
    ']': 0xDD,
    "'": 0xDE
}

@utils.run_if_enabled
def key_down(key,x=.031,y=.101):
    keydown(key); sleep(random.uniform(x,y))

def key_up(key,x=.031,y=.101):
    keyup(key); sleep(random.uniform(x,y))

@utils.run_if_enabled
def press(key, n=1, down_time=0.05, up_time=0.08):
    key_down(key)
    key_up(key)

def release_unreleased_key():
    print("release ",unreleased_key)
    for key in unreleased_key:
        key_up(key)
    
def click(position, button='left',click_time=1):
    pass