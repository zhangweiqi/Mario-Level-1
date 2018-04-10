__author__ = 'justinarmstrong'

# 屏幕高度和宽度
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

# 屏幕尺寸
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 原始标题
ORIGINAL_CAPTION = "Super Mario Bros 1-1"

## COLORS ##

# 定义颜色
#            R    G    B
GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FOREST_GREEN = (31, 162, 35)
BLUE = (0, 0, 255)
SKY_BLUE = (39, 145, 251)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
NEAR_BLACK = (19, 15, 48)
COMBLUE = (233, 232, 255)
GOLD = (255, 215, 0)

# 背景色
BGCOLOR = WHITE

# 放大尺寸
SIZE_MULTIPLIER = 2.5
# 砖放大的尺寸
BRICK_SIZE_MULTIPLIER = 2.69
# 背景放大尺寸
BACKGROUND_MULTIPLER = 2.679
# 背景高度
GROUND_HEIGHT = SCREEN_HEIGHT - 62

# MARIO FORCES
# mario加速
WALK_ACCEL = .15
# 跑步加速
RUN_ACCEL = 20
# 小转向
SMALL_TURNAROUND = .35

# 重力
GRAVITY = 1.01
# 跳时重力
JUMP_GRAVITY = .31
# 跳的反向速度
JUMP_VEL = -10
# 最快跳的速度
FAST_JUMP_VEL = -12.5
# 最大竖直速度
MAX_Y_VEL = 11

# 最快奔跑速度
MAX_RUN_SPEED = 800
# 最快走路速度
MAX_WALK_SPEED = 6

# Mario States

STAND = 'standing'
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'
SMALL_TO_BIG = 'small to big'
# 变得可以发射子弹
BIG_TO_FIRE = 'big to fire'
BIG_TO_SMALL = 'big to small'
# 接触旗杆
FLAGPOLE = 'flag pole'
# 走向城堡
WALKING_TO_CASTLE = 'walking to castle'
# 失败结束
END_OF_LEVEL_FALL = 'end of level fall'

# GOOMBA Stuff
# 走地怪物运动状态
LEFT = 'left'
RIGHT = 'right'
JUMPED_ON = 'jumped on'
DEATH_JUMP = 'death jump'

# KOOPA STUFF
# 乌龟滑行
SHELL_SLIDE = 'shell slide'

# BRICK STATES
# 砖块的状态
# 静止
RESTING = 'resting'
# 凸起的
BUMPED = 'bumped'

# COIN STATES
# 金币状态
OPENED = 'opened'
# 旋转
SPIN = 'spin'

# MUSHROOM STATES
# 蘑菇状态
# 揭开
REVEAL = 'reveal'
# 滑行
SLIDE = 'slide'

# STAR STATES
# 星星状态：闪烁
BOUNCE = 'bounce'

# FIRE STATES
# 火焰状态
FLYING = 'flying'
BOUNCING = 'bouncing'
EXPLODING = 'exploding'

# Brick and coin box contents
# 盒子的内容
MUSHROOM = 'mushroom'
STAR = 'star'
FIREFLOWER = 'fireflower'
SIXCOINS = '6coins'
COIN = 'coin'
LIFE_MUSHROOM = '1up_mushroom'

# 火球
FIREBALL = 'fireball'

# LIST of ENEMIES
# 蘑菇怪和乌龟怪
GOOMBA = 'goomba'
KOOPA = 'koopa'

# LEVEL STATES

FROZEN = 'frozen'
NOT_FROZEN = 'not frozen'
IN_CASTLE = 'in castle'
FLAG_AND_FIREWORKS = 'flag and fireworks'

# FLAG STATE
# 旗帜的状态
TOP_OF_POLE = 'top of pole'
SLIDE_DOWN = 'slide down'
BOTTOM_OF_POLE = 'bottom of pole'

# 1UP score
ONEUP = '379'

# MAIN MENU CURSOR STATES
# 主菜单指针状态
PLAYER1 = '1 player'
PLAYER2 = '2 player'

# OVERHEAD INFO STATES
# 状态的过度
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'loading screen'
LEVEL = 'level'
GAME_OVER = 'game over'
FAST_COUNT_DOWN = 'fast count down'
END_OF_LEVEL = 'end of level'

# GAME INFO DICTIONARY KEYS
# 游戏中要统计的信息
# 金币数
COIN_TOTAL = 'coin total'
# 当前分数
SCORE = 'score'
# 最高分数
TOP_SCORE = 'top score'
# 几条命
LIVES = 'lives'
# 当前时间
CURRENT_TIME = 'current time'
# 第几关
LEVEL_STATE = 'level state'
#
CAMERA_START_X = 'camera start x'
# 马里奥死亡数
MARIO_DEAD = 'mario dead'

# STATES FOR ENTIRE GAME
# 整个游戏中的不同状态，应该是状态机一样
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'load screen'
TIME_OUT = 'time out'
GAME_OVER = 'game over'
LEVEL1 = 'level1'

# SOUND STATEZ
# 音乐状态
# 正常
NORMAL = 'normal'
# 时间紧张，加速
STAGE_CLEAR = 'stage clear'
# 胜利
WORLD_CLEAR = 'world clear'
# 时间特别紧张
TIME_WARNING = 'time warning'
# 加速
SPED_UP_NORMAL = 'sped up normal'
# 加速
MARIO_INVINCIBLE = 'mario invincible'
