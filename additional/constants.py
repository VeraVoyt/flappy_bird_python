# all constants we will need


# screen parameters
SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
FPS = 30


## images
# general images
IMAGES_FOLDER = "additional/images/"
BACKGROUND_IMAGE = IMAGES_FOLDER + "background_day.png"
GROUND_IMAGE = IMAGES_FOLDER + "ground.png"

# bird images
BIRD_IMAGE = IMAGES_FOLDER + "bluebird_midflap.png"

# pipe images
PIPE_IMAGE = IMAGES_FOLDER + "pipe_green.png"

# positions of objects
GROUND_Y_COORD = SCREEN_HEIGHT * 0.79
BIRD_STARTING_POSITION = (SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.5)
PIPE_STARTING_POSITION_X = SCREEN_WIDTH * 1.2
PIPES_DISTANCE = SCREEN_WIDTH * 0.3
PIPE_GAP_CENTER_MIN = int(SCREEN_HEIGHT * 0.2)
PIPE_GAP_CENTER_MAX = int(SCREEN_HEIGHT * 0.5)
PIPE_HALF_GAP = int(SCREEN_HEIGHT * 0.1)

# kimematic constants
G = 0.0009
DELTA_T = 1000 / FPS
BIRD_FLAP_SPEED = 0.23
PIPE_VELOCITY = 0.1



