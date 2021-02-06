import numpy as np
import settings
from colorama import Fore, Back, Style
import state
class Slider:
    build_block  = Fore.LIGHTBLUE_EX+"\u2588"+Style.RESET_ALL
    width = int(settings.width)
    height = int(settings.height)
    def __init__(self):
        self.length = int(settings.board_length)
        self.array = [self.build_block for i in range(self.length)]
        self.pos = [0,self.height-1]
        self.speed = 2
    
    def render(self):
        cnvs  = state.cnvs
        for x,item in enumerate(self.array):
            cnvs.canvas[self.pos[1]][self.pos[0]+x]= item
    def clear(self):
        cnvs = state.cnvs
        for x,item in enumerate(self.array):
            cnvs.canvas[self.pos[1]][self.pos[0]+x]=settings.build_block
    def moveLeft(self):
        if  self.pos[0]-self.speed<0:
            self.pos[0]=0
        else:
            self.pos[0]-=self.speed
    def moveRight(self):
        if self.pos[0]+self.speed>=self.width-self.length:
            self.pos[0]=self.width-self.length
        else:
            self.pos[0]+=self.speed

    def changeLength(self,nl):
        self.length = nl
        self.array = [self.build_block for i in range(self.length)]

        