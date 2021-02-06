from colorama import Fore, Back, Style
import sys, time
import canvas

import random
import state


import input

if __name__=='__main__':
    cnvs = state.cnvs
    slider  = state.slider
    ball = state.ball
    bc = state.bc
    pus =  state.pus
    while not state.quit:
        if cnvs.pause==False and not cnvs.gameover:
            slider.clear()
            ball.clear()
            pus.clear()
            if state.dp_ball!=None:
                state.dp_ball.clear()
            ball.update()
            pus.update()
            input.onKeyPress()

            if state.dp_ball!=None:
                state.dp_ball.update()
            print('\033c')
            bc.render()
            pus.render()
            ball.render()
            if state.dp_ball!=None:
                state.dp_ball.render()
            slider.render()
        else:
            print('\033c')

            input.onKeyPress()
        
        cnvs.render()
        if cnvs.gameover==True:
            slider.clear()
            ball.clear()
            pus.clear()
            cnvs = state.cnvs
            slider  = state.slider
            ball = state.ball
            bc = state.bc
            pus =  state.pus
        
        time.sleep(0.03)

    print('\033c')
