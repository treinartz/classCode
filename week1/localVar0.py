import py5_tools

w = 40
local_var="I am a local variable."


def setup():
    size(400, 400)


def draw():
    background(220)
    fill(0)
    text_size(20)
    text(local_var, 50, 50)
    fill(255, 0, 0)
    ellipse(200, 200, w, w)

    
py5_tools.animated_gif('housewithvar.gif', 100, 0.05, 0.05) 

