"""An interpreter that reads and executes user-created routines."""

import threading
import time
# import git
import cv2
# import inspect
# import importlib
# import traceback
# from os.path import splitext, basename
# from src.common import config, utils, settings
from src.common import config, settings, utils
# from src.detection import detection
# from src.routine import components
# from src.routine.routine import Routine
# from src.command_book.command_book import CommandBook
# from src.routine.components import Point
from src.common.vkeys import press, click
# from src.common.interfaces import Configurable
import requests
import json
import numpy as np

RUNE_BUFF_TEMPLATE = cv2.imread('assets/rune_buff_template.jpg', 0)


class Bot():


    def __init__(self):
        config.bot = self

        self.map_rune_active = False
        self.in_rune_buff = False
        self.rune_pos = (0, 0)
        self.rune_closest_pos = (0, 0)      # Location of the Point closest to rune

        self.ready = False
        self.thread = threading.Thread(target=self._main)
        self.thread.daemon = True

    def start(self):
        print('\n[~] Started main bot loop')
        self.thread.start()

    def _main(self):
        config.listener.enabled = True
        
        self.ready = True

        while True:
            if config.enabled:
                if self.map_rune_active:
                    if self._solve_rune():
                        pass
                # custom rotation goes here. 
                print(f'{config.player_pos=}')
                time.sleep(.1)
            else:
                time.sleep(0.03)

    def runesolver3(self,screenshot):
        # now=perf_counter()
        print('solving rune2 ..')
        # hwnd = win32gui.FindWindow(None, "MapleStory")
        # position = win32gui.GetWindowRect(self.maplehwnd)
        # x, y, w, h = position
        # runepos = (x+121, y+143, x+697, y+371) # 800x600
        # runepos = (x+221, y+143, x+797, y+371) # 1074x768
        # runepos = (x+341, y+143, x+917, y+371) # 1280x720
        # runepos = (x+381, y+143, x+957, y+371) # 1366x768
        # runepos = (x+631, y+143, x+1207, y+371) # 1920x1080 # if this coordinate not work, lemme know!
        # print(x,y,w,h)
        # screenshot = ImageGrab.grab(runepos,all_screens=True)
        # screenshot.show()
        # time.sleep(5)
        img = np.array(screenshot)
        sendjson = {
            'image': img.tolist()
        }
        # link = 'http://'+self.ipaddress+':8001/'
        link = 'http://'+'127.0.0.1'+':8001/'
        link = link + 'predict'
        print(f'sending requests ..')
        r = requests.post(url=link, json=sendjson)
        print(f'received response ..')
        # time.sleep(.1)
        json_data = json.loads(r.text)
        print(json_data['prediction'])
        sms = json_data['prediction']
        # print(f"{sms}")
        for i in range(len(sms)):
            print(sms[i:i+1])
            # PressKey(captchadict[sms[i:i+1]])
            # if sms[i:i+1] == 'u':
            #     print('up')
            #     await self.upp(3,11)
            #     await self.upr(101,171)
            # if sms[i:i+1] == 'd':
            #     print('down')
            #     await self.downp(3,11)
            #     await self.downr(101,171)
            # if sms[i:i+1] == 'l':
            #     print('left')
            #     await self.leftp(3,11)
            #     await self.leftr(101,171)
            # if sms[i:i+1] == 'r':
            #     print('right')
            #     await self.rightp(3,11)
            #     await self.rightr(101,171)
            time.sleep(0.001)
        # print(f'{perf_counter()-now=}')
        return sms



    @utils.run_if_enabled
    def _solve_rune(self):        
        if self.in_rune_buff:
            print('in rune buff, quit solving rune')
            return True
        for _ in range(2):
            move = self.command_book['move']
            move(*self.rune_pos).execute()
            adjust = self.command_book['adjust']
            adjust(*self.rune_pos).execute()
        time.sleep(0.5)   
        for ii in range(2):
            if ii == 1:
                press("left", 1, down_time=0.1,up_time=0.3) 
            elif ii == 2:
                press("right", 1, down_time=0.2,up_time=0.3)
            time.sleep(0.8) # stop moving 
            pre_rune_frame = config.capture.frame 
            cv2.imwrite('./recording/s_' + str(time.time()) + '_pre.png',pre_rune_frame)
            press(self.config['Interact'], 1, down_time=0.013,up_time=0.1) # Inherited from Configurable
            print('\nSolving rune:')
            time.sleep(1.00) # reduce this time as much as possible 
            for _ in range(1):
                if self.map_rune_active == False:
                    break
                frame = config.capture.frame
                # cv2.imshow('img',frame)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                height, width, _n = frame.shape
                solution_frame = frame[height//2-300:height//2-72, width //2-288:width//2+288]
                print(f'why hello {type(solution_frame)} {solution_frame.shape}, {height=}, {width=}, {_n=}')
                # cv2.imshow('img',solution_frame)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                solution_frame = cv2.cvtColor(solution_frame,cv2.COLOR_RGBA2RGB)
                # solution = self.runesolver3(solution_frame)
                solution = utils.async_callback(self,self.runesolver3(solution_frame))
                print(f'{solution=}')
                if solution:
                    print(', '.join(solution))
                    if len(solution) == 4:
                        print('Solution found, entering result')
                        for arrow in solution:
                            print(f'{arrow=}')
                            # # press(arrow, 1, down_time=0.1)
                            # if arrow=='u':
                            #     press('up', 1, down_time=0.003)
                            # elif arrow=='d':
                            #     press('down', 1, down_time=0.003)
                            # elif arrow=='l':
                            #     press('left', 1, down_time=0.003)
                            # elif arrow=='r':
                            #     press('right', 1, down_time=0.003)
                        time.sleep(1)
                        find_rune_buff = False
                        for _ in range(2):
                            time.sleep(0.2)
                            frame = config.capture.frame
                            rune_buff = utils.multi_match(frame[:95, :],
                                                        RUNE_BUFF_TEMPLATE,
                                                        threshold=0.93)
                            print('rune_buff matched : ',len(rune_buff))
                            if len(rune_buff) >= 2:
                                config.latest_solved_rune = time.time()
                                config.should_solve_rune = False
                                self.map_rune_active = False
                                self.in_rune_buff = True
                                find_rune_buff = True
                            if len(rune_buff) >= 3:
                                rune_buff_pos = min(rune_buff, key=lambda p: p[0])
                                print('rune_buff_pos : ', rune_buff_pos)
                                target = (
                                    round(rune_buff_pos[0]),
                                    round(rune_buff_pos[1])
                                )
                                utils.game_window_click(target, button='right')
                                config.latest_solved_rune = time.time()
                                config.should_solve_rune = False
                                self.map_rune_active = False
                                self.in_rune_buff = True
                                find_rune_buff = True
                                utils.game_window_click((700,120), button='right')
                        if find_rune_buff:
                            return True
            press("left", 1, down_time=0.05,up_time=0.1)
            press("right", 1, down_time=0.05,up_time=0.1)
            if self.map_rune_active == False:
                break
            time.sleep(2.8) 
        return False
