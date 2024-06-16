'''
file: 1a2_dice_sides.py
file-id: 537d11a1-def1-4302-a38a-c919b9ebedab
project: mountainkea123d/young_kea
project-id: bcd73817-93d4-46a0-8e2e-60a1b1990183
created-by: felix@42sol.eu
description:
- GOAL: learning how to use `build123d` to write texton faces 
- 1 TASK: use your dice (W6) from 1a1_dice_core.py 
- 2 TASK: write a number on each side of the dice
- 3a OPTIONAL: replace the numbers by the face sides
- 3b OPTIONAL: rotate the text that F, R, L, B are upright
- 1 HINT: Now using the dice it might be helpful to assign it to a variable
- 2a HINT: If you add new features always start with Mode.ADD first to see where it is placed.
- 2b HINT: You need to sketch on the face!
- 3a HINT: You can utilize a list/tuple or dictionary to map the names
- 3b HINT: Rotate the text and not the face!


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

with BuildPart() as build_dice:
    dice = Box(p_length, p_length, p_length)

    for index, face in enumerate(dice.faces()):
        with BuildSketch(face):
            Text(p_map[index+1], font_size=p_length*.8, rotation=-90)
        extrude(amount=-2, mode=Mode.SUBTRACT)

show(build_dice, colors=["red"] )