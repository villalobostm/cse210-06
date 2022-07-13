import pathlib
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "EL PONG"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "pong/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "pong/assets/sounds/boing.wav"
WELCOME_SOUND = "pong/assets/sounds/start.wav"
OVER_SOUND = "pong/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
P1_UP = "w"
P1_DOWN = "s"
P2_UP = "up"
P2_DOWN = "down"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4
MENU = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP_P1 = "p1_stats"
STATS_GROUP_P2 = "p2_stats"
POINT_VALUE = 1
MAXIMUM_SCORE = 11
POINTS_TO_WIN = 2
DEFAULT_LIVES = 0

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP_P1 = "p1_score"
SCORE_P1_X_POSITION = 100
SCORE_P2_X_POSITION = SCREEN_WIDTH - 100
SCORE_GROUP_P2 = "p2_score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "pong/assets/images/000.png"
BALL_WIDTH = 14
BALL_HEIGHT = 14
BALL_VELOCITY = 4

# RACKET
RACKET_GROUP_P1 = "p1_paddle"
RACKET_GROUP_P2 = "p2_paddle"
RACKET_IMAGES = [f"pong/assets/images/{n:03}.png" for n in range(100, 103)]
RACKET_WIDTH = 14 
RACKET_HEIGHT = 100
RACKET_RATE = 6
RACKET_VELOCITY = 7
RACKET_POSITION_P1 = 5
RACKET_POSITION_P2 = (SCREEN_WIDTH - RACKET_WIDTH) - 5

BRICK_WIDTH = 80
BRICK_HEIGHT = 28
BRICK_DELAY = 0.5
BRICK_RATE = 4
BRICK_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"

## MENU
# BUTTON 1
BUTTON_1_GROUP = "button_1"
BUTTON_1_TEXT = "New Game"
BUTTON_1_IMAGE = "pong/assets/images/start.png"
BUTTON_1_HEIGHT = 41 
BUTTON_1_WIDTH =  147
BUTTON_1_X_POSITION = CENTER_X - (BUTTON_1_WIDTH / 2)
BUTTON_1_Y_POSITION = CENTER_Y - BUTTON_1_HEIGHT

# BUTTON 2
BUTTON_2_GROUP = "button_2"
BUTTON_2_TEXT = "How to Play"
BUTTON_2_IMAGE = "pong/assets/images/help.png"
BUTTON_2_HEIGHT = 41 
BUTTON_2_WIDTH = 147 
BUTTON_2_X_POSITION = CENTER_X - (BUTTON_2_WIDTH / 2)
BUTTON_2_Y_POSITION = BUTTON_1_Y_POSITION + (BUTTON_2_HEIGHT * 2)

# BUTTON 3
BUTTON_3_GROUP = "button_3"
BUTTON_3_TEXT = "Credits"
BUTTON_3_IMAGE = "pong/assets/images/credits.png"
BUTTON_3_HEIGHT = 41 
BUTTON_3_WIDTH = 147 
BUTTON_3_X_POSITION = CENTER_X - (BUTTON_3_WIDTH / 2)
BUTTON_3_Y_POSITION = BUTTON_2_Y_POSITION + (BUTTON_3_HEIGHT * 2)
