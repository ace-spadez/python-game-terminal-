import numpy as np
import settings
from colorama import Fore, Back, Style
import state
import random
import  futils

class Brick:
    brick_length = int(settings.brick_length)
    
    def __init__(self,power,posx,posy):
        self.power = power
        self.pos = [int(posx),int(posy)]
        
        self.length = self.brick_length
    def getblock(self):
        if self.power==1:
            return  Fore.WHITE
        elif self.power==2:
            return  Fore.YELLOW
        elif  self.power==3:
            return  Fore.MAGENTA
        elif self.power==4:
            return  Fore.RED
        else:
            return Fore.BLACK

    def build_block(self):
        return [self.getblock()+"\u2588"+Style.RESET_ALL for i in range(int(settings.brick_length))]
    def reducePower(self):
        if self.power==4:
            return
        self.power-=1
        if self.power == 0:
            state.pus.addPowerup(self.pos[0],self.pos[1])
    def destroy(self):
       
        self.power=0
        state.pus.addPowerup(self.pos[0],self.pos[1])
    def render(self):
        if self.power==0:
            return
        cnvs = state.cnvs
        for idx,  item in enumerate(self.build_block()):
            cnvs.canvas[self.pos[1]][self.pos[0]+idx] = item
    
    def clear(self):
        cnvs = state.cnvs

        for idx,  item in enumerate(self.build_block()):
            cnvs.canvas[self.pos[1]][self.pos[0]+idx] = settings.build_block


class BrickComplex:
    width = int(settings.width)
    brick_length =  int(settings.brick_length)
    height = int(settings.height)
    def __init__(self):
        self.complex = [

        ]
        for j in range(10):
            for i in range(-j,j+1,1):
                self.complex.append(Brick(random.randint(1,4),self.width/2-self.brick_length/2-i*self.brick_length,self.height/2-j))

    
    def render(self):
        for item  in self.complex:
            item.render()
    

    def clear(self):
        for item  in self.complex:
            item.clear()