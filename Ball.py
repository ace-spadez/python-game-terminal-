import numpy as np
import settings
from colorama import Fore, Back, Style
import state
import futils



class Ball:
    build_block  = Fore.RED+"\u2580"+Style.RESET_ALL
    width = int(settings.width)
    height = int(settings.height)
    def __init__(self):
        self.pos = [int(settings.board_length/2),int(settings.height-2)]
        self.speed = [1,-1]
        self.invincinble = False
        self.stuck = False
        self.stickable = False
    
    def render(self):
        cnvs  = state.cnvs
        cnvs.canvas[self.pos[1]][self.pos[0]]=self.build_block
    def clear(self):
        cnvs = state.cnvs
        cnvs.canvas[self.pos[1]][self.pos[0]]=settings.build_block
    def update(self):
        bc  = state.bc
        cnvs  = state.cnvs

        x = self.pos[0]+self.speed[0]
        y = self.pos[1]+self.speed[1]
        if x<0 or x>self.width-1:
            self.speed[0] = -1*self.speed[0]
        
        if y<0 or y>self.height-1:
            self.speed[1] = -1*self.speed[1]
        
        if y>self.height-1:
            cnvs.lives   -=1
            if cnvs.lives==-1:
                cnvs.gameover = True
            
        if futils.ballSlidercollision(x,y,state.slider):
            self.speed[1] = -1*self.speed[1]
            if self.stickable==True:
                self.stuck= True

        for brick in bc.complex:
            if brick.power==0 :
                continue
            
            if futils.ballBrickcollision(x,y,brick):

                if self.invincinble:
                    brick.destroy()
                    self.speed[1]= -1*self.speed[1]                    
                else:
                    brick.reducePower()
                if brick.power ==  0:
                    brick.clear()
                    state.cnvs.score+=1
                self.speed[1]= -1*self.speed[1]
                break
        if self.stuck==True:
            self.pos[0]=int(state.slider.pos[0]+state.slider.length/2)
            self.pos[1]=int(state.slider.pos[1]-1)
            return
                    
        self.pos[0]+=self.speed[0]
        self.pos[1]+=self.speed[1]
        