# -*- coding: utf-8 -*-
"""
Author: Kate Barnard
KUID: 3160224
Date: 9/16/2024
Last modified: 9/16/2024
Purpose: packaging soda
"""

num_sodas = int(input('How many sodas do you have?: '))
fridge_cubes = num_sodas // 24
print ('Fridge Cubes: ', fridge_cubes)
remaining_sodas = num_sodas % 24
six_packs = remaining_sodas // 6
print ('Six packs: ', six_packs)
singles = remaining_sodas % 6
print('Singles: ', singles)