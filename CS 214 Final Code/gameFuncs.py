import stddraw, screens
from math import pi
from ship import Bullet

def keyBoardProccess(keys, s0, scale, bullets, fireRate):
    if keys[stddraw.K_e]: 
        s0.rotate(1)
    elif keys[stddraw.K_q]: 
        s0.rotate(-1)
    elif keys[stddraw.K_w]:
        s0.setAngle(pi/2)
        s0.setPos(37)
    if keys[stddraw.K_a]:
        if s0.getX() > (-scale+0.2): 
            s0.move(-1)
        else: 
            s0.rotate()
    elif keys[stddraw.K_d]:
        if s0.getX() < (scale-0.2):
            s0.move(1)
        else: 
            s0.rotate()
    else: 
        s0.rotate()

    if keys[stddraw.K_SPACE] and s0.getFireRate() <= 0:
        bullet = Bullet(s0.getX(), s0.getY(), s0.getAngle(), '1',  True)
        bullets.append(bullet)
        s0.setFireRate(fireRate)
    else: s0.setFireRate(s0.getFireRate()-1)

    if keys[stddraw.K_h]:
        while stddraw.hasNextKeyTyped(): stddraw.nextKeyTyped()
        while not stddraw.hasNextKeyTyped(): screens.startScreen()
    
    if keys[stddraw.K_x]: return 1

def keyBoardProccessP2(keys, s1, scale, bullets, fireRate):
    if keys[stddraw.K_o]:
        s1.rotate(1)
    elif keys[stddraw.K_u]:
        s1.rotate(-1)
    elif keys[stddraw.K_i]:
        s1.setAngle(pi/2)
        s1.setPos(37)
    if keys[stddraw.K_j]:
        if s1.getX() > (-scale+0.2):
            s1.move(-1)
        else:
            s1.rotate()
    elif keys[stddraw.K_l]:
        if s1.getX() < (scale-0.2):
            s1.move(1)
        else:
            s1.rotate()
    else:
        s1.rotate()
    
    if keys[stddraw.K_n] and s1.getFireRate() <= 0:
        bullet = Bullet(s1.getX(), s1.getY(), s1.getAngle(), '2',  True)
        bullets.append(bullet)
        s1.setFireRate(fireRate)
    else: s1.setFireRate(s1.getFireRate()-1)
    