# Write your code here :-)
actor1 = Actor('elephant')
actor1.pos = 300, 500

WIDTH = 800
HEIGHT = 600

def draw():
    screen.clear()
    #screen.fill(WHITE)
    actor1.draw()
    animate(actor1, tween='bounce_start', duration=5, on_finished=None,pos = (100,100))
