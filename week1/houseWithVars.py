import py5_tools

def setup():
    size(300, 300)


def draw():
    background(187, 193, 127)
    
    # Variables for the house base
    house_x = 100
    house_y = 100
    house_width = 100
    house_height = 100
    
    # Variables for the door
    door_x = house_x + 0.35 * house_width
    door_y = house_y + 0.5 * house_height
    door_width = 0.3 * house_width
    door_height = 0.5 * house_height
    
    # Variables for the roof
    roof_x1 = house_x
    roof_x2 = house_x + 0.5 * house_width
    roof_x3 = house_x + house_width
    roof_y = house_y
    
    # Draw the base of the house
    fill(206, 224, 14)
    rect(house_x, house_y, house_width, house_height)
    
    # Draw the door
    fill(72, 26, 2)
    rect(door_x, door_y, door_width, door_height)
    
    # Draw the roof
    fill(224, 14, 14)
    triangle(roof_x1, roof_y, roof_x2, roof_y - 0.5 * house_height, roof_x3, roof_y)
    
py5_tools.animated_gif('housewithvars.gif', 100, 0.05, 0.05) 
