import py5_tools

def setup():
    size(300, 300)
    smooth()

def draw():
    background(187, 193, 127)
    
    # Draw the base of the house
    fill(206, 224, 14)
    rect(100, 150, 100, 100)
    
    # Draw the door
    fill(72, 26, 2)
    rect(135, 200, 30, 50)
    
    # Draw the roof
    fill(224, 14, 14)
    triangle(100, 150, 200, 150, 150, 100)
    
py5_tools.animated_gif('house.gif', 100, 0.05, 0.05) 

