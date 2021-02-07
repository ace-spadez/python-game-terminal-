import numpy as np
import settings
from colorama import Fore, Back, Style
import state
import random
import time
import futils
import Ball 
class Powerup:
    # build_block  = Fore.WHITE+"\u2588"+Style.RESET_ALL
    width = int(settings.width)
    height = int(settings.height)
    types = ['🌟','🌠','🌙','💫','💖','📌']
    type_names = ['Expand','Speed Up','Shorten','Double Ball','Break Thru','Ball Grab']
    # types = ['🌟','🌠','🌙','💫','💖','📌']
    def __init__(self,type,x,y):
        self.type = type
        self.pos = [x,y]
        self.speed = 1
        self.caught = False
        self.time = None
    
    def render(self):
        if self.caught ==True:
            return
        cnvs  = state.cnvs
        cnvs.canvas[self.pos[1]][self.pos[0]]= self.types[self.type]
        cnvs.canvas[self.pos[1]][self.pos[0]+1]= ''
    def clear(self):
        cnvs = state.cnvs
        cnvs.canvas[self.pos[1]][self.pos[0]]= settings.build_block
        cnvs.canvas[self.pos[1]][self.pos[0]+1]= settings.build_block
    def update(self):
        y = self.pos[1]+self.speed
        if y>=self.height:
            return 0
        if futils.ballSlidercollision(self.pos[0],y,state.slider) or futils.ballSlidercollision(self.pos[0]+1,y,state.slider):
            self.time  = time.time()
            self.caught = True
            self.attach()
            return 2
        self.pos[1]=y
        return 1
    def checkValidity(self):
        t =  time.time()
        if t-self.time>10.0:
            self.detach()
            
            return 0
        return 10-t+self.time
    def attach(self):
        
        if self.type==0:
            state.slider.changeLength(2*int(settings.board_length))
        elif self.type==1:
            state.ball.speed  = [2*state.ball.speed[0],2*state.ball.speed[0]]
        elif self.type==2:
            state.slider.changeLength(int(int(settings.board_length)/2))
        elif self.type==3:
            state.dp_ball =  Ball.Ball()
        elif self.type==4:
            state.ball.invincinble  =  True
        elif self.type==5:
            state.ball.stickable=   True

    def detach(self):
        if self.type==0:
            state.slider.changeLength(settings.board_length)
        elif self.type==1:
            state.ball.speed  = [state.ball.speed[0]//2,state.ball.speed[0]//2]
        elif self.type==2:
            state.slider.changeLength(settings.board_length)
        elif self.type==3:
            state.dp_ball =  None
        elif self.type==4:
            state.ball.invincinble  =  False
        elif self.type==5:
            state.ball.stickable = False
            state.ball.stuck  = False



class Powerups:
    def  __init__(self):
        self.active_powerups = []
        self.caught  = []

    
    def  render(self):
        cnvs= state.cnvs
        for powerup in self.active_powerups:
            powerup.render()

        for y in range(cnvs.height):
            for x in range(30):
                cnvs.sidebar[y][x]=cnvs.header_block    
        for  idx,powerup in enumerate(self.caught):
            rtn = powerup.checkValidity()
            if rtn==0:
                self.caught.remove(powerup)
            else:
                type = powerup.type
                typename =  powerup.type_names[type]
                st = Fore.BLACK+Back.WHITE    +f'{typename} {int(rtn)}'+Style.RESET_ALL
                
                for index,ch in enumerate(st):
                    cnvs.sidebar[idx+1][1+index] = ch


            
    def  clear(self):
        cnvs= state.cnvs
        for powerup in self.active_powerups:
            powerup.clear()
        
    def update(self):
        for powerup in self.active_powerups:
            rtn = powerup.update()
            if rtn==0:
                self.active_powerups.remove(powerup)
            if rtn==2:
                self.active_powerups.remove(powerup)
                self.caught.append(powerup)

    def addPowerup(self,x,y):
        self.active_powerups.append(Powerup(random.randint(0,5),x,y))
        