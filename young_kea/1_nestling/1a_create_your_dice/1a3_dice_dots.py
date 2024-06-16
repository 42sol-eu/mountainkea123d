'''
file: 1a3_dice_dots.py
file-id: d60cae94-474b-46cb-bf99-62d4e253bea9
project: mountainkea123d/young_kea
project-id: bcd73817-93d4-46a0-8e2e-60a1b1990183
created-by: felix@42sol.eu
description:
- GOAL: learning how to use `build123d` draw dots on faces of the dice.
- 1 TASK: use your dice (W6) from 1a1_dice_core.py or 1a2_dice_faces.py 
- 2 TASK: create a grid of 3x3 dots on every face 
- 3 TASK: draw the representation of the dots on the face
- 4 TASK: create the correct order 6-1, 2-5, 3-4

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


#%% [Main]
dot_cuts = []
with BuildPart() as build_dice:
    dice = Box(p_length, p_length, p_length)

    for index, face in enumerate(dice.faces()):
        with BuildPart(face) as sketch:
            count = 0
            with GridLocations(p_length/4, p_length/4, 3, 3):
                count += 1
                if count <= index+1:
                    print(f'index: {index}, count: {count}')
                    dot_cuts.append(Sphere(p_length/10))
    
    for cut in dot_cuts:
        add(cut,mode=Mode.SUBTRACT)

show(build_dice, colors=["red"] )