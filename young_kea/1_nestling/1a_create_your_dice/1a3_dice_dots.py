'''
file: 1a3_dice_dots.py
file-id: d60cae94-474b-46cb-bf99-62d4e253bea9
project: mountainkea123d/young_kea
project-id: bcd73817-93d4-46a0-8e2e-60a1b1990183
created-by: felix@42sol.eu
description:
- GOAL: learning how to use `build123d` draw dots on faces of the dice.
- 1 TASK: use your dice (W6) from 1a1_dice_core.py or 1a2_dice_faces.py 
- 2 TASK: draw the representation of the dots as a sphere and cut it in the dice
- 3 TASK: create the correct order 6-1, 2-5, 3-4
TODO: - 4 TASK: create a grid of 3x3 dots on every face 
- 4 HINT: use `GridLocation` on the face with a `BuildSketch` and extrude


history:
-  2024-06-16: created

'''
# %% [Import]
from build123d import *     # https://build123d.readthedocs.io
from ocp_vscode import *

set_defaults(reset_camera=Camera.KEEP)

#%% [Parameter]
p_length = 12.0
p_map = {1: 'L', 2: 'R', 3: 'F', 4: 'B', 5:'D', 6:'T'}

#%% [Functions]
def draw_dots(face, count):
    dot_cuts = []
    with BuildPart(face):
        # HINT: switch 5 and 1 to get the correct order
        # print(f'XX: {count}, {face.bounding_box()}, {Plane(face)}')
        x = p_length/4
        if count == 5:
            with BuildPart(Plane(face, z_dir=(0,0,-1))):
                dot_cuts.append(Sphere(p_length/10)) # .move(locations[4]))
        elif count == 2:
            with BuildPart(Plane(face, z_dir=(+1,0,0))):
                dot_cuts.append(Sphere(p_length/10).move(Location((0,-x,-x))))
                dot_cuts.append(Sphere(p_length/10).move(Location((0,+x,+x))))
        elif count == 3:
            with BuildPart(Plane(face, z_dir=(0,+1,0))):
                dot_cuts.append(Sphere(p_length/10).move(Location((-x,0,-x))))
                dot_cuts.append(Sphere(p_length/10))
                dot_cuts.append(Sphere(p_length/10).move(Location((+x,0,+x))))
        elif count == 4:
            with BuildPart(Plane(face, z_dir=(0,-1,0))):
                dot_cuts.append(Sphere(p_length/10).move(Location((-x,0,-x))))
                dot_cuts.append(Sphere(p_length/10).move(Location((-x,0,+x))))
                dot_cuts.append(Sphere(p_length/10).move(Location((+x,0,-x))))
                dot_cuts.append(Sphere(p_length/10).move(Location((+x,0,+x))))
        elif count == 1:
            with BuildPart(Plane(face, z_dir=(-1,0,0))):
                dot_cuts.append(Sphere(p_length/10).move(Location((0,-x,-x))))
                dot_cuts.append(Sphere(p_length/10).move(Location((0,-x,+x))))
                dot_cuts.append(Sphere(p_length/10).move(Location((0,+x,-x))))
                dot_cuts.append(Sphere(p_length/10).move(Location((0,+x,+x))))
                dot_cuts.append(Sphere(p_length/10))
        elif count == 6:
            with BuildPart(Plane(face, z_dir=(0,0,+1))):
                dot_cuts.append(Sphere(p_length/10).move(Location((-x,-x,0))))
                dot_cuts.append(Sphere(p_length/10).move(Location((-x,+x,0))))
                dot_cuts.append(Sphere(p_length/10).move(Location((-x,0,0))))
                dot_cuts.append(Sphere(p_length/10).move(Location((+x,0,0))))
                dot_cuts.append(Sphere(p_length/10).move(Location((+x,-x,0))))
                dot_cuts.append(Sphere(p_length/10).move(Location((+x,+x,0))))
        else:
            pass
    return dot_cuts

#%% [Main]
dot_cuts = []
with BuildPart() as build_dice:
    dice = Box(p_length, p_length, p_length)

    for index, face in enumerate(dice.faces()):
        new_dots = draw_dots(face, index+1)
        dot_cuts.extend(new_dots)
    for cut in dot_cuts:
        # print(cut.bounding_box())
        add(cut,mode=Mode.SUBTRACT)

if True:
    a = build_dice.part.rotate(axis=Axis.Z, angle=60).rotate(axis=Axis.X, angle=15)
    b = a.moved(Location((0,0,2*p_length)))
    show(a,b, colors=["blue", "green"] )
else:
    show(build_dice, *dot_cuts, colors=["yellow"] )