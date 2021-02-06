



def ballSlidercollision(bx,by,slider):

    sx1 = slider.pos[0]
    sx2  = slider.pos[0]+slider.length-1
    sy = slider.pos[1]

    if by==sy and bx>=sx1  and  bx<=sx2:
        return  True
    return False

def ballBrickcollision(bx,by,brick):
    
    sx1 = brick.pos[0]
    sx2  = brick.pos[0]+brick.length-1
    sy = brick.pos[1]

    if by==sy and bx>=sx1  and  bx<=sx2:
        return  True
    return False