import py5_tools
w = 10
growing = True

def setup():
    size(400, 400)

def draw():
    global w, growing
    background(220)
    fill(0)
    text_size(20)
    text("I am a local variable.", 50, 50)
    fill(255, 0, 0)
    ellipse(200, 200, w, w)

    if growing:
        w += 1
        if w > 200:
            growing = False
    else:
        w -= 1
        if w < 10:
            growing = True
            
py5_tools.animated_gif('localvar.gif', 100, 0.05, 0.05) 