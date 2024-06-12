# %% [Import]
from build123d import *     # https://build123d.readthedocs.io
from ocp_vscode import *
from copy import copy, deepcopy
from math import sqrt

set_port(3939)
# % % [Parameter]
p_width = 10
p_height = 1
p_width_part = 2*32

# %% [Functions]

def height_triangle(width):
    return width * sqrt(3)/2

def generate_object(width, height, factor=1.0, overlap=0, do_cuts=False, do_part=True):
    real_width = width * factor
    h = height_triangle(real_width)
    the_distance = width * (1-overlap) 
    
    with BuildPart() as the_template:
        
        with BuildSketch() as the_element:
            element1 = RegularPolygon(real_width/2, 6, rotation=30)
            
        height1 = height
        if not do_part:
            height1 = 0.001
        extrude(amount=height1, taper=0.1)

        if do_cuts:
            r_circle_h = height_triangle(width) * (1.0-factor)
            r_circle_w = width * (1.0-factor)
            r_cuts = real_width/16
            with BuildSketch() as the_element:
                with PolarLocations(r_circle_h, 6, start_angle=0.) as the_locations:
                    cut_a = RegularPolygon(r_cuts, 6, rotation=90)
            extrude(amount=2*height, taper=0.1, mode=Mode.ADD)

            with BuildSketch() as the_element:
                with PolarLocations(r_circle_w, 6, start_angle=30.) as the_locations:
                    cut_b = RegularPolygon(r_cuts, 6, rotation=120)
            extrude(amount=2*height, taper=0.1, mode=Mode.ADD)
    
    with BuildPart() as the_object:
        locations = [Location((height_triangle(the_distance)/2, 0, 0)),Location((-height_triangle(the_distance)/2, 0, 0))]

        refs = [copy(the_template.part).locate(loc) for loc in locations]
        for item in refs:
            add(item)
    
    return the_object

# %  % [Main]
p_overlap = 0.01
a = generate_object(p_width, p_height, factor=1.0, overlap=p_overlap)
b = generate_object(p_width, 1.2*p_height, factor=0.6, overlap=p_overlap, do_cuts=True)
c = generate_object(p_width_part, p_height*2., factor=1.0, do_cuts=False)
d = generate_object(p_width_part, p_height*2., factor=0.6, do_cuts=True, do_part=False)

with BuildPart() as connector:
    add(a)
    add(b,mode=Mode.SUBTRACT)


with BuildPart() as plate:
    add(c)
    add(d,mode=Mode.SUBTRACT)

show(connector, plate)
# %%