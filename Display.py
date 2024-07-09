import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import edges as cube_edges, vertices as cube_vertices
from Pyramid import edges as pyramid_edges, vertices as pyramid_vertices
from Prism import edges as prism_edges, vertices as prism_vertices

# Index to Track the Current Model being Displayed
current_model = 0

# Function to Draw a Cube
def Cube():
    glBegin(GL_LINES)
    for edge in cube_edges:
        for vertex in edge:
            glVertex3fv(cube_vertices[vertex])
    glEnd()

# Function to Draw a Pyramid
def Pyramid():
    glBegin(GL_LINES)
    for edge in pyramid_edges:
        for vertex in edge:
            glVertex3fv(pyramid_vertices[vertex])
    glEnd()

# Function to Draw a Prism
def Prism():
    glBegin(GL_LINES)
    for edge in prism_edges:
        for vertex in edge:
            glVertex3fv(prism_vertices[vertex])
    glEnd()

# Function to Translate the Object
def translate_obj(dx, dy, dz):
    glTranslatef(dx, dy, dz)

# Function to Rotate the Object
def rotate_obj(angle_x, angle_y, angle_z):
    glRotatef(angle_x, 1, 0, 0)
    glRotatef(angle_y, 0, 1, 0)
    glRotatef(angle_z, 0, 0, 1)

# Function to Scale the Object
def scale_obj(sx, sy, sz):
    glScalef(sx, sy, sz)

# Main Function to Set Up and Run the OpenGL Display
def main():
    global current_model
    # Initialize Transformation Parameters
    translate_x = 0
    translate_y = 0
    translate_z = 0
    rotate_x = 0
    rotate_y = 0
    rotate_z = 0
    scale_x = 1
    scale_y = 1
    scale_z = 1

    # Initialize Pygame and Set Up the Display
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Set Up Perspective Projection
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    # Move the Object Back so it's Visible
    glTranslatef(0, 0, -5)

    # Initial Rotation Set to Zero
    glRotatef(0, 0, 0, 0)

    # List of Models to Cycle Through
    models = [Cube, Pyramid, Prism]

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_model = (current_model + 1) % len(models)

        # Handle Keyboard Input for Transformations
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            translate_x -= 0.05
        if keys[pygame.K_d]:
            translate_x += 0.05
        if keys[pygame.K_w]:
            translate_y += 0.05
        if keys[pygame.K_s]:
            translate_y -= 0.05
        if keys[pygame.K_PAGEUP]:
            translate_z -= 0.05
        if keys[pygame.K_PAGEDOWN]:
            translate_z += 0.05
        if keys[pygame.K_UP]:
            rotate_x -= 1
        if keys[pygame.K_DOWN]:
            rotate_x += 1
        if keys[pygame.K_RIGHT]:
            rotate_y += 1
        if keys[pygame.K_LEFT]:
            rotate_y -= 1
        if keys[pygame.K_e]:
            rotate_z -= 1
        if keys[pygame.K_q]:
            rotate_z += 1
        if keys[pygame.K_z]:
            scale_x -= 0.05
        if keys[pygame.K_x]:
            scale_x += 0.05
        if keys[pygame.K_c]:
            scale_y -= 0.05
        if keys[pygame.K_v]:
            scale_y += 0.05
        if keys[pygame.K_b]:
            scale_z -= 0.05
        if keys[pygame.K_n]:
            scale_z += 0.05

        # Clear Buffers and Set Up Transformations
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        translate_obj(translate_x, translate_y, translate_z)
        rotate_obj(rotate_x, rotate_y, rotate_z)
        scale_obj(scale_x, scale_y, scale_z)
        models[current_model]()
        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(10)

# Starts the Program
main()