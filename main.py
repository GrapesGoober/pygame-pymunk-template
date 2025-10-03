import pygame
import pymunk
import pymunk.pygame_util
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
background_color = (30, 30, 30)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame + Pymunk Template")
clock = pygame.time.Clock()
FPS = 60

# Initialize Pymunk
space = pymunk.Space()
space.gravity = (0, 900)  # Gravity pulls down

# Drawing options for debug rendering
draw_options = pymunk.pygame_util.DrawOptions(window)


def create_ball(space, position, radius=20, mass=1):
    """Creates a dynamic ball that falls under gravity."""
    body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius))
    body.position = position
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0.6
    shape.friction = 0.5
    space.add(body, shape)
    return shape


def create_static_floor(space, y_position=580):
    """Creates a static floor segment at the bottom."""
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    shape = pymunk.Segment(body, (0, y_position), (WIDTH, y_position), 5)
    shape.elasticity = 0.8
    shape.friction = 0.8
    space.add(body, shape)
    return shape


def handle_events():
    """Handle user input and system events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            create_ball(space, pos)


def update_physics(space, dt):
    """Step the physics simulation forward."""
    space.step(dt)


def draw(space, window):
    """Draw the space using Pymunk's debug draw."""
    window.fill(background_color)  # Dark background
    space.debug_draw(draw_options)
    pygame.display.flip()


def main():
    create_static_floor(space)  # Create the floor
    dt = 1.0 / FPS

    while True:
        handle_events()
        update_physics(space, dt)
        draw(space, window)
        clock.tick(FPS)


if __name__ == "__main__":
    main()
