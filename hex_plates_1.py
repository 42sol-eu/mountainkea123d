# %% [Import]
from build123d import *     # https://build123d.readthedocs.io
from ocp_vscode import *
from copy import copy, deepcopy
from math import sqrt

set_port(3939)
set_defaults(reset_camera=Camera.KEEP)

# % % [Parameter]
p_width = 10
p_height = 1
p_width_part = 2*32

# %% [Functions]

def height_triangle(width):
    return width * sqrt(3)/2

def create_6_holes(width, factor, start_angle=0.):
    r_circle_h = (width - p_width) * factor
    if start_angle == 0.:
        rotation = 30
    else:
        rotation = 120
    with PolarLocations(r_circle_h, 6, start_angle=start_angle) as the_locations:
        for loc in the_locations:
            RegularPolygon(p_width/12, 6, rotation=rotation, mode=Mode.SUBTRACT).locate(loc)


def create_12_holes(width, factor):
        a = height_triangle(width)
        b = (width + a ) * .5
        
        create_6_holes(b, factor, start_angle=0.)
        create_6_holes(b, factor, start_angle=30.)

def create_24_holes(width, factor):
        a = height_triangle(width)
        b = (width + a ) * .5
        create_6_holes(b, factor, start_angle=0.)
        create_6_holes(b, factor, start_angle=15.)
        create_6_holes(b, factor, start_angle=30.)
        create_6_holes(b, factor, start_angle=45.)



# %  % [Main]
with BuildPart() as plate:
    with BuildSketch() as the_element:
        element1 = RegularPolygon(p_width_part/2, 6, rotation=30)
        r_circle_h = (height_triangle(p_width_part) - height_triangle(p_width)) * .5
        with PolarLocations(r_circle_h, 6, start_angle=0.) as the_locations:
            for loc in the_locations:
                RegularPolygon(p_width/2, 6, rotation=30, mode=Mode.SUBTRACT).locate(loc)
    extrude(amount=p_height, taper=0.1)

top_face = (
    plate.faces()
    .filter_by(GeomType.PLANE)
    .sort_by(Axis.Z)[-1]
)
# Create a workplane from the face
top_plane = Plane(
    origin=top_face.center(), x_dir=(1, 0, 0), z_dir=top_face.normal_at()
)

with BuildPart(top_plane) as top_plate:
    with BuildSketch(top_plane) as the_element:
        element2 = RegularPolygon(p_width_part/2, 6, rotation=30)

        for factor in range(1, 8, 1):
            the_f = (factor-1)*0.1
            if factor <= 2:
                create_6_holes(p_width_part, the_f)
            elif factor <= 3:
                create_12_holes(p_width_part, the_f)
            elif factor <=6:
                create_24_holes(p_width_part, the_f)
            else:
                create_6_holes(height_triangle(p_width_part), the_f, start_angle=30.)
        
    extrude(amount=p_height, taper=0.1)


show(plate,top_plate,top_face)
# %%