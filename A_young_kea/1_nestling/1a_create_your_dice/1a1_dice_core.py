'''
file: 1a1_dice_core.py
file-id: f642221c-161e-4cda-b1d0-0625c70cf42c
project: mountainkea123d/young_kea
project-id: bcd73817-93d4-46a0-8e2e-60a1b1990183
created-by: felix@42sol.eu
description:
- GOAL: learning how to use `build123d` and `ocp_vscode` 
- 1 TASK: create a dice (W6) 
- 2 TASK: use the `show` function to display the dice and color its sides
- 3 OPTIONAL: show the side names and colors in the viewer
- 1 HINT: use the `names` and `colors` parameters of the `show` function
- 2 HINT: use the `faces` method of the `part` object to get the faces of the dice
- 3 HINT: this is a simple extension of the names adding colors Python strings

history:
-  2024-06-16: created

'''
# %% [Import]
from build123d import *     # https://build123d.readthedocs.io
from ocp_vscode import *

set_defaults(reset_camera=Camera.KEEP)

#%% [Parameter]
p_length = 12.0

#%% [Functions]


#%% [Main]

with BuildPart() as build_dice:
    Box(p_length, p_length, p_length)

#                        1        2         3         4 / -3    5 / -2     6 / -1
names_list =  ['dice',  'left',  'right',  'front',  'back',   'bottom',  'top']
colors_list = ['white', 'red',   'green',  'blue',   'yellow', 'purple',  'orange']
names_extended = []
sides_list = []
for count, face in enumerate(build_dice.part.faces()):
    sides_list.append(face)
    extended_name = f'{names_list[count]} ({colors_list[count]})'

    names_extended.append(extended_name)

show(build_dice, *sides_list, names=names_extended, colors=colors_list)