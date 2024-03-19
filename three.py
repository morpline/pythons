# gui "library"
from turtle import *
from copy import *
tirtle = Turtle()
tirtle.hideturtle()
tirtle.speed(0)
tirtle.color("#244224")
tirtle.fillcolor("#feeffe")
screensize(800,600)

def Box ( x, y, w, h) :
    tirtle.teleport(x,y)
    tirtle.seth(90)
    tirtle.begin_fill()
    tirtle.forward(h)
    tirtle.right(90)
    tirtle.forward(w)
    tirtle.right(90)
    tirtle.forward(h)
    tirtle.right(90)
    tirtle.forward(w)
    tirtle.right(90)
    tirtle.end_fill()

def TextBox (text,l,b,x,y,w,h):
    Box(x,y,w,h)
    tirtle.teleport(x+l,y+h-(b+5))
    tirtle.write(text,False,"left",("Monospace",14,"normal"))

# oldList = [{"ohno":"dfsfs"}]
# global changed 
changed = False
guilist = []

def checkClick (x,y) :
    print(f"check click at {x},{y}")
    for g in guilist:
        if(g["type"]=="clickable"):
            if(
                x>g["x"] and
                x<g["x"]+g["w"] and
                y>g["y"] and
                y<g["y"]+g["h"]
            ):
                g["f"]()

def checkGUI () :
    global changed
    # print(changed)
    if(changed):
        changed=False
        return True
    else :
        return False
def addBox (x,y,w,h) :
    global changed
    changed = True
    guilist.append({
        "type":"box",
        "x":x,
        "y":y,
        "w":w,
        "h":h
    })
def addClickableBox (test,x,y,w,h,f) :
    global changed
    changed = True
    guilist.append({
        "type":"clickable",
        "text":test,
        "f":f,
        "x":x,
        "y":y,
        "w":w,
        "h":h
    })
def addTextBox (text,x,y,w,h) :
    global changed
    changed = True
    guilist.append({
        "type":"TextBox",
        "x":x,
        "y":y,
        "w":w,
        "h":h,
        "text":text
    })
def drawGUI () :
    print("drawing GUI")
    tirtle.fillcolor("#feeffe")
    tirtle.color("#244224")
    for g in guilist :
        if g["type"] == "box":
            Box(g["x"],g["y"],g["w"],g["h"])
        else :
            if g["type"] == "TextBox" :
                TextBox(g["text"],5,5,g["x"],g["y"],g["w"],g["h"])
            else:
                if g["type"] == "clickable":
                    tirtle.color("#FFFFFF")
                    tirtle.fillcolor("#000000")
                    TextBox(g["text"],5,5,g["x"],g["y"],g["w"],g["h"])
def drawThree ():
    # tirtle.clearscreen()
    # if(checkGUI()):
    drawGUI()

def doon () :
    tirtle.onclick(checkClick,1,True)
    done()