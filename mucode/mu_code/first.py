# Write your code here :-)
act1 = Actor('dog')
act1.pos = 200, 500

global xSpeed, ySpeed
xSpeed = 4
ySpeed = 4

WIDTH = 900
HEIGHT = 700

def draw():
    screen.clear()
    act1.draw()

def update():
    global xSpeed, ySpeed
    act1.x += xSpeed
    act1.y += ySpeed
    if act1.x > WIDTH:
        xSpeed *= -1
    if act1.x < 0:
        xSpeed *= -1
    if act1.y > HEIGHT:
        ySpeed *= -1
    if act1.y < 0:
        ySpeed *= -1