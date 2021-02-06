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
    while True:
 
        slider.clear()
        ball.clear()
        pus.clear()
        if state.dp_ball!=None:
            state.dp_ball.clear()
        ball.update()
        pus.update()

        if state.dp_ball!=None:
            state.dp_ball.update()
        print('\033c')
        input.onKeyPress()
        bc.render()
        pus.render()
        ball.render()
        if state.dp_ball!=None:
            state.dp_ball.render()
        slider.render()

        cnvs.render()
        
        time.sleep(0.03)

