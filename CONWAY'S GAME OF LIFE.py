#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### "Conways Game of Life by Faarah"
import copy
import random
import sys
import time

WIDTH = 79
HEIGHT = 20
ALIVE = '*'
DEAD = ' '

# Initialize the nextCells dictionary
nextCells = {}

# Populate nextCells with random values
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE
        else:
            nextCells[(x, y)] = DEAD

while True:
    print('\n' * 50)
    cells = copy.deepcopy(nextCells)

    # Display the cells
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end='')
        print()
    print('Press Ctrl-C to quit.')

    # Calculate the next generation
    for x in range(WIDTH):
        for y in range(HEIGHT):
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            # Count the number of living neighbors
            numNeighbors = 0
            if cells[(left, above)] == ALIVE:
                numNeighbors += 1
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1
            if cells[(right, above)] == ALIVE:
                numNeighbors += 1
            if cells[(left, y)] == ALIVE:
                numNeighbors += 1
            if cells[(right, y)] == ALIVE:
                numNeighbors += 1
            if cells[(left, below)] == ALIVE:
                numNeighbors += 1
            if cells[(x, below)] == ALIVE:
                numNeighbors += 1
            if cells[(right, below)] == ALIVE:
                numNeighbors += 1

            # Set cell based on Conway's Game of Life rules
            if cells[(x, y)] == ALIVE and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and numNeighbors == 3:
                nextCells[(x, y)] = ALIVE
            else:
                nextCells[(x, y)] = DEAD

    # Pause for 1 second
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        print("By Faarah")
        sys.exit()


# In[ ]:





# In[ ]:




