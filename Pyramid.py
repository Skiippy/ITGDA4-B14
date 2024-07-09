from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define Vertices for the Pyramid
vertices = (
    (0, 1, 0),
    (-1, -1, 1),
    (1, -1, 1),
    (0, -1, -1)
)

# Define Edges for the Pyramid
edges = (
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 2),
    (2, 3),
    (3, 1)
)