###
# A tree may only be cut down if diameter >50cm
# check for circumference
# to test: Tree 1: 160 Tree 2: 90 Tree 3: 230 Tree 4: 120

import math

circumference = int(input('Enter circumference of the tree '))
diameter = circumference / math.pi
can_be_cut_down = diameter > 50
print(f'Tree can be cut down: {can_be_cut_down}')

# 1 - true, 2 - false, 3 - true, 4 - false