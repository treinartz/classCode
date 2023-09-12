import py5_tools  # first line 

def setup():
    size(600, 400)

def draw():
    background(0, 68, 119)  # Dark blue background
    no_fill()
    stroke_weight(30)
    
    stroke(255, 0, 0)  # Red
    arc(300, 400, 560, 600, -radians(180), radians(0))
    
    stroke(255, 255, 0)  # Yellow
    arc(300, 400, 500, 540, -radians(180), radians(0)) 
    
    stroke(0, 255, 0)  # Green
    arc(300, 400, 440, 480, -radians(180), -radians(90))  # Adjust the size and position of the green arc

py5_tools.animated_gif('rainbow.gif', 100, 0.05, 0.05)   #last line of code


"""
the negative radian value for the starting angle is used to ensure
that the red arc starts from the left side and proceeds to the right
side (clockwise), creating the appearance of a rainbow.
"""
