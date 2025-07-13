import pygame
import time

# --- Configuration ---
SPRITE_SHEET_IMAGE = 'mj_sprite.png' # The name of your sprite sheet file
NUM_FRAMES = 10                  # The total number of dance moves in the image
FRAME_WIDTH = 49                 # The width of ONE dance move (you may need to adjust)
FRAME_HEIGHT = 70              # The height of ONE dance move (you may need to adjust)
ANIMATION_SPEED = 0.2            # Seconds between each frame (lower is faster)

# --- Screen Setup ---
SCREEN_WIDTH = 800               # Width of the new large window
SCREEN_HEIGHT = 600              # Height of the new large window
BG_COLOR = (255, 255, 255)       # RGB color for white

# --- Pygame Initialization ---
pygame.init()

# Create the large display window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Sheet Animation")

# Load the entire sprite sheet image
try:
    sprite_sheet = pygame.image.load(SPRITE_SHEET_IMAGE).convert_alpha()
except pygame.error:
    print(f"Error: Unable to load image '{SPRITE_SHEET_IMAGE}'.")
    print("Please make sure the image is named correctly and in the same folder as the script.")
    exit()


# --- Main Animation Loop ---
current_frame = 0
running = True

while running:
    # Event handler (to allow closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Define the rectangle area for the current frame on the sprite sheet
    rect = pygame.Rect(current_frame * FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT)
    
    # Create a new, blank image for the single frame
    frame_image = pygame.Surface(rect.size, pygame.SRCALPHA)
    
    # Copy the rectangular part from the sprite sheet onto the blank image
    frame_image.blit(sprite_sheet, (0, 0), rect)

    # --- Drawing ---
    # 1. Fill the entire background with white
    screen.fill(BG_COLOR)

    # 2. Calculate the center position to draw the character
    draw_x = (SCREEN_WIDTH - FRAME_WIDTH) / 2
    draw_y = (SCREEN_HEIGHT - FRAME_HEIGHT) / 2
    
    # 3. Draw the single frame onto the screen at the calculated position
    screen.blit(frame_image, (draw_x, draw_y))

    # Update the entire display to show the changes
    pygame.display.flip()

    # Move to the next frame in the sequence
    current_frame = (current_frame + 1) % NUM_FRAMES

    # Pause to control the speed of the animation
    time.sleep(ANIMATION_SPEED)

# Quit the program
pygame.quit()