from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define Vertices for the Prism
vertices = (
    (-1, -1, 1),
    (1, -1, 1),
    (0, -1, -1),
    (-1, 1, 1),
    (1, 1, 1),
    (0, 1, -1)
)

# Define Edges for the Prism
edges = (
    (0, 1),
    (1, 2),
    (2, 0),

    (3, 4),
    (4, 5),
    (5, 3),

    (0, 3),
    (1, 4),
    (2, 5)
)