y=500
def setup():
    size(1000,1000)
    strokeWeight(30)
    stroke(255,255,255)
def draw():
    global y
    background(0,0,0)
    point (500,y+50)
    point (540,y+80)
    point (900,y-59)
    point (50,y+5)
    point (777,y-77)
    point (111,y+50)
    point (303,y-5)
    point (888,y)
    point (666,y+66)
    point (300,y+100)
    point (90,y+110)
    point (350,y-400)
    if mousePressed == True:
        y=y-499
    else:
        y=y+20
        if y > 500:
            y=y-20
