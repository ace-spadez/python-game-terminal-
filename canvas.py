import  numpy as np
import settings
from colorama import Fore, Back, Style
import time
class Canvas:
    width = int(settings.width)
    height = int(settings.height)
    build_block  = settings.build_block
    header_block  =  settings.header_block
    
    def __init__(self):
        self.canvas = np.array([[self.build_block for i in range(self.width)] for j in range(self.height)])
        self.center = np.array([[self.build_block for i in range(self.width)] for j in range(self.height)])
        self.header =  np.array([[self.header_block for i in range(int(self.width/2))] for j in range(3)])
        self.footer =  np.array([[self.header_block for i in range(int(self.width))] for j in range(1)])
        self.board_length = int(settings.board_length)
        self.score = 0
        self.lives = 10
        self.time= time.time()
        self.pause = False
        self.gameover = False
    
    def render(self):
        score_str = Fore.BLACK+Back.WHITE+f'Score: {self.score}'+Style.RESET_ALL
        time_str = Fore.BLACK+Back.WHITE+f'Time Passed: {int(time.time()-self.time)}'+Style.RESET_ALL
        lives_str   = Fore.BLACK+Back.WHITE+f'Lives: {self.lives}'+Style.RESET_ALL

        footer = Fore.BLACK+Back.WHITE+'a: move left  d:move right   p: pause/play   q: quit 💥💢'+Style.RESET_ALL


        for idx,ch in enumerate(score_str):
            self.header[0][1+idx] = ch
        for idx,ch in enumerate(time_str):
            self.header[1][1+idx] = ch
        for idx,ch in enumerate(lives_str):
            self.header[2][1+idx] = ch

        
        for idx,ch in enumerate(footer):
            self.footer[0][1+idx] = ch

        center =  Fore.WHITE+Back.BLACK+'Press p to resume, q to quit'+Style.RESET_ALL if not self.gameover else Fore.WHITE+Back.BLACK+'Game Over. Press r to  replay'+Style.RESET_ALL
        for idx,ch in enumerate(center):
            self.center[self.height//2][self.width//2-len(center)//2+idx] = ch



        pr = []
        for y  in  range(3):
            for  x in range(int(self.width/2)):
                pr.append(self.header[y][x])
            pr.append('\n')
        if self.pause==True or self.gameover==True:
            for y  in  range(self.height):
                for  x in range(self.width):
                    pr.append(self.center[y][x])
                pr.append('\n')
        else:
            for y  in  range(self.height):
                for  x in range(self.width):
                    pr.append(self.canvas[y][x])
                pr.append('\n')
        for y  in  range(1):
            for  x in range(self.width):
                pr.append(self.footer[y][x])
            pr.append('\n')
        print(''.join(pr),end='')