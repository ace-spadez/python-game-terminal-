from getch import KBHit
import state
kbh   = KBHit()
import Ball
import canvas
import BrickComplex
import Slider
import powerup
def onKeyPress():
    char = kbh.getinput()
    if char=='d':
        state.slider.moveRight()
    if char=='a':
        state.slider.moveLeft()
    if char=='p':
        if state.cnvs.pause==True:
            state.cnvs.pause=False
        else:
            state.cnvs.pause=True
    if char=='q' and state.cnvs.pause==True:
        state.quit = True
    if  char=='q' and not state.cnvs.pause==True:
        state.cnvs.pause=True

    if char=='r' and state.cnvs.gameover==True:
        state.cnvs =  canvas.Canvas()
        state.slider = Slider.Slider()
        state.ball = Ball.Ball()
        state.bc =  BrickComplex.BrickComplex()
        state.pus = powerup.Powerups()
