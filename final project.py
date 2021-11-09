import numpy as np
import matplotlib.pyplot as plt

# Define Grid
grid_length = 5
grid = np.zeros([grid_length, grid_length]) # initialize grid
print(grid)

# Define State Space, Action Space
S = size(grid)
print(S)
A = 4 # up, down, left, right

# Define Reward Model
R = np.zeros([S, A])
goal = 15 # element in grid where goal is
rock1 = 8 # element in grid where rock1 is (in future, make this random?)
rock2 = 23 # element in grid where rock2 is (random in future?)
seaweed = 10 # position of seaweed
R[goal,:] = 10
R[seaweed,:] = -2
R[rock1,:] = -10
R[rock2,:] = -10
