from getch import KBHit
import state
kbh   = KBHit()

def onKeyPress():
    char = kbh.getinput()
    if char=='d':
        state.slider.moveRight()
    if char=='a':
        state.slider.moveLeft()
