# import customtkinter
# import asyncio
# import tkinter
# from tkinter import Frame, Label
# from PIL import Image, ImageTk
import time

from src.modules.gui import GUI
from src.modules.bot import Bot
from src.modules.capture import Capture
from src.modules.notifier import Notifier
from src.modules.listener import Listener

if __name__ == "__main__":

    bot = Bot()
    capture = Capture()
    notifier = Notifier()
    listener = Listener()

    bot.start()
    while not bot.ready:
        time.sleep(.010)

    capture.start()
    while not capture.ready:
        time.sleep(0.01)

    notifier.start()
    while not notifier.ready:
        time.sleep(0.01)

    listener.start()
    while not listener.ready:
        time.sleep(0.01)

    gui = GUI()
    gui.start()







