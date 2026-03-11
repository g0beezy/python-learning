import pygame
import sys
import random
import math

# 初始化
pygame.init()

# 常量
TILE = 24
COLS = 28
ROWS = 31
WIDTH = TILE * COLS
HEIGHT = TILE * ROWS + 50  # 底部留空显示分数
FPS = 60
PACMAN_SPEED = 2

# 颜色
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLUE = (33, 33, 222)
PINK = (255, 184, 255)
DOT_COLOR = (255, 183, 174)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)
GHOST_BLUE = (33, 33, 255)
GHOST_SPEED = 2

# 地图 (0=空 1=墙 2=豆子 3=大力丸 4=空地无豆子)
LEVEL = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
    [1,3,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,3,1],
    [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1],
    [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1],
    [1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,2,1,1,1,1,1,4,1,1,4,1,1,1,1,1,2,1,1,1,1,1,1],
    [1,1,1,1,1,1,2,1,1,1,1,1,4,1,1,4,1,1,1,1,1,2,1,1,1,1,1,1],
    [1,1,1,1,1,1,2,1,1,4,4,4,4,4,4,4,4,4,4,1,1,2,1,1,1,1,1,1],
    [1,1,1,1,1,1,2,1,1,4,1,1,1,4,4,1,1,1,4,1,1,2,1,1,1,1,1,1],
    [1,1,1,1,1,1,2,4,4,4,1,4,4,4,4,4,4,1,4,4,4,2,1,1,1,1,1,1],
    [4,4,4,4,4,4,2,1,1,4,1,4,4,4,4,4,4,1,4,1,1,2,4,4,4,4,4,4],
    [1,1,1,1,1,1,2,1,1,4,1,4,4,4,4,4,4,1,4,1,1,2,1,1,1,1,1,1],
    [1,1,1,1,1,1,2,1,1,4,1,1,1,1,1,1,1,1,4,1,1,2,1,1,1,1,1,1],
    [1,1,1,1,1,1,2,1,1,4,4,4,4,4,4,4,4,4,4,1,1,2,1,1,1,1,1,1],
    [1,1,1,1,1,1,2,1,1,4,1,1,1,1,1,1,1,1,4,1,1,2,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
    [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
    [1,3,2,2,1,1,2,2,2,2,2,2,2,4,4,2,2,2,2,2,2,2,1,1,2,2,3,1],
    [1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1],
    [1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1],
    [1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1],
    [1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1],
    [1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

# 复制地图用于游戏
game_map = [row[:] for row in LEVEL]

# 屏幕
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("吃豆人 Pac-Man")
clock = pygame.time.Clock()

# 吃豆人状态
pac_x = 13 * TILE
pac_y = 22 * TILE
pac_dir = 'STOP'
pac_next_dir = 'STOP'
pac_frame = 0
pac_anim_timer = 0

score = 0
lives = 3
dots_total = sum(row.count(2) + row.count(3) for row in LEVEL)
dots_eaten = 0


def get_tile(px, py):
    """像素坐标转格子坐标"""
    return px // TILE, py // TILE


def can_move(px, py, direction):
    """检查某方向是否可以移动"""
    if direction == 'STOP':
        return False

    speed = PACMAN_SPEED
    if direction == 'LEFT':
        nx, ny = px - speed, py
    elif direction == 'RIGHT':
        nx, ny = px + speed, py
    elif direction == 'UP':
        nx, ny = px, py - speed
    elif direction == 'DOWN':
        nx, ny = px, py + speed
    else:
        return False

    # 隧道传送允许
    if nx < 0 or nx + TILE > WIDTH:
        return True

    # 检查四个角是否碰墙
    margin = 1
    corners = [
        (nx + margin, ny + margin),
        (nx + TILE - 1 - margin, ny + margin),
        (nx + margin, ny + TILE - 1 - margin),
        (nx + TILE - 1 - margin, ny + TILE - 1 - margin),
    ]
    for cx, cy in corners:
        col = int(cx) // TILE
        row = int(cy) // TILE
        if row < 0 or row >= ROWS or col < 0 or col >= COLS:
            return False
        if game_map[row][col] == 1:
            return False
        # 吃豆人不能进入幽灵屋内部
        if 12 <= row <= 16 and 11 <= col <= 16:
            return False
    return True


def is_aligned():
    """检查吃豆人是否对齐到格子"""
    return pac_x % TILE == 0 and pac_y % TILE == 0


def draw_map():
    """绘制地图"""
    for row in range(ROWS):
        for col in range(COLS):
            x = col * TILE
            y = row * TILE
            cell = game_map[row][col]
            if cell == 1:
                pygame.draw.rect(screen, BLUE, (x, y, TILE, TILE))
            elif cell == 2:
                # 小豆子
                pygame.draw.circle(screen, DOT_COLOR, (x + TILE // 2, y + TILE // 2), 3)
            elif cell == 3:
                # 大力丸（闪烁）
                if pygame.time.get_ticks() % 400 < 200:
                    pygame.draw.circle(screen, WHITE, (x + TILE // 2, y + TILE // 2), 8)


def draw_pacman():
    """绘制吃豆人"""
    # 张嘴动画
    mouth_angles = [45, 30, 10, 0, 10, 30, 45]
    mouth = mouth_angles[pac_frame % len(mouth_angles)]

    if pac_dir == 'RIGHT':
        start_angle = mouth
    elif pac_dir == 'LEFT':
        start_angle = 180 + mouth
    elif pac_dir == 'UP':
        start_angle = 90 + mouth
    elif pac_dir == 'DOWN':
        start_angle = 270 + mouth
    else:
        start_angle = mouth

    arc_angle = 360 - 2 * mouth
    if arc_angle <= 0:
        arc_angle = 1

    center_x = pac_x + TILE // 2
    center_y = pac_y + TILE // 2
    radius = TILE // 2 - 1

    # 画扇形
    points = [(center_x, center_y)]
    for angle in range(int(start_angle), int(start_angle + arc_angle) + 1, 5):
        rad = math.radians(angle)
        px = center_x + radius * math.cos(rad)
        py = center_y - radius * math.sin(rad)
        points.append((px, py))
    points.append((center_x, center_y))

    if len(points) > 2:
        pygame.draw.polygon(screen, YELLOW, points)


def draw_hud():
    """绘制底部信息"""
    font = pygame.font.SysFont("microsoftyahei", 20)
    score_text = font.render(f"分数: {score}", True, WHITE)
    screen.blit(score_text, (10, HEIGHT - 40))

    lives_text = font.render(f"生命: {lives}", True, WHITE)
    screen.blit(lives_text, (WIDTH - 120, HEIGHT - 40))


# --- 幽灵类 ---
class Ghost:
    def __init__(self, col, row, color, name, release_delay=0):
        self.x = col * TILE
        self.y = row * TILE
        self.color = color
        self.name = name
        self.dir = 'UP'
        self.speed = GHOST_SPEED
        self.home_x = col * TILE
        self.home_y = row * TILE
        self.release_delay = release_delay  # 延迟出屋帧数
        self.release_timer = release_delay
        self.exiting = True  # 出屋阶段

    def get_target(self):
        """根据幽灵性格计算目标位置"""
        if self.name == 'blinky':
            # 红：直接追吃豆人
            return pac_x, pac_y
        elif self.name == 'pinky':
            # 粉：追吃豆人前方4格
            tx, ty = pac_x, pac_y
            if pac_dir == 'LEFT':
                tx -= 4 * TILE
            elif pac_dir == 'RIGHT':
                tx += 4 * TILE
            elif pac_dir == 'UP':
                ty -= 4 * TILE
            elif pac_dir == 'DOWN':
                ty += 4 * TILE
            return tx, ty
        elif self.name == 'inky':
            # 蓝：随机+追踪混合
            if random.random() < 0.3:
                return random.randint(0, WIDTH), random.randint(0, ROWS * TILE)
            return pac_x, pac_y
        elif self.name == 'clyde':
            # 橙：远了追，近了跑
            dist = math.sqrt((self.x - pac_x) ** 2 + (self.y - pac_y) ** 2)
            if dist > 8 * TILE:
                return pac_x, pac_y
            else:
                return self.home_x, self.home_y
        return pac_x, pac_y

    def ghost_can_move(self, px, py, direction):
        """幽灵的碰墙检测"""
        if direction == 'LEFT':
            nx, ny = px - self.speed, py
        elif direction == 'RIGHT':
            nx, ny = px + self.speed, py
        elif direction == 'UP':
            nx, ny = px, py - self.speed
        elif direction == 'DOWN':
            nx, ny = px, py + self.speed
        else:
            return False

        if nx < -TILE or nx >= WIDTH:
            return True

        margin = 1
        corners = [
            (nx + margin, ny + margin),
            (nx + TILE - 1 - margin, ny + margin),
            (nx + margin, ny + TILE - 1 - margin),
            (nx + TILE - 1 - margin, ny + TILE - 1 - margin),
        ]
        for cx, cy in corners:
            c = int(cx) // TILE
            r = int(cy) // TILE
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            if game_map[r][c] == 1:
                return False
            # 已出屋的幽灵不能再进入幽灵屋内部（行12-16，列11-16）
            if not self.exiting and 12 <= r <= 16 and 11 <= c <= 16:
                return False
        return True

    def get_opposite(self):
        opp = {'LEFT': 'RIGHT', 'RIGHT': 'LEFT', 'UP': 'DOWN', 'DOWN': 'UP'}
        return opp.get(self.dir, 'STOP')

    def update(self):
        """每帧更新幽灵位置"""
        # 延迟出屋
        if self.release_timer > 0:
            self.release_timer -= 1
            return

        # 出屋阶段：优先往上走，堵了就往左，直到离开幽灵屋
        if self.exiting:
            if self.y // TILE < 11:  # 已经出了幽灵屋区域
                self.exiting = False
            else:
                if self.x % TILE == 0 and self.y % TILE == 0:
                    for try_dir in ['UP', 'LEFT', 'RIGHT', 'DOWN']:
                        if self.ghost_can_move(self.x, self.y, try_dir):
                            self.dir = try_dir
                            break
                if self.ghost_can_move(self.x, self.y, self.dir):
                    if self.dir == 'LEFT': self.x -= self.speed
                    elif self.dir == 'RIGHT': self.x += self.speed
                    elif self.dir == 'UP': self.y -= self.speed
                    elif self.dir == 'DOWN': self.y += self.speed
                return

        if self.x % TILE == 0 and self.y % TILE == 0:
            target_x, target_y = self.get_target()
            directions = ['LEFT', 'RIGHT', 'UP', 'DOWN']
            opposite = self.get_opposite()
            # 不能掉头
            possible = [d for d in directions if d != opposite and self.ghost_can_move(self.x, self.y, d)]

            if not possible:
                possible = [d for d in directions if self.ghost_can_move(self.x, self.y, d)]

            if possible:
                best_dir = possible[0]
                best_dist = float('inf')
                for d in possible:
                    nx, ny = self.x, self.y
                    if d == 'LEFT': nx -= TILE
                    elif d == 'RIGHT': nx += TILE
                    elif d == 'UP': ny -= TILE
                    elif d == 'DOWN': ny += TILE
                    dist = (nx - target_x) ** 2 + (ny - target_y) ** 2
                    if dist < best_dist:
                        best_dist = dist
                        best_dir = d
                self.dir = best_dir

        if self.ghost_can_move(self.x, self.y, self.dir):
            if self.dir == 'LEFT': self.x -= self.speed
            elif self.dir == 'RIGHT': self.x += self.speed
            elif self.dir == 'UP': self.y -= self.speed
            elif self.dir == 'DOWN': self.y += self.speed

        # 隧道传送
        if self.x < -TILE: self.x = WIDTH - TILE
        elif self.x >= WIDTH: self.x = 0

    def draw(self):
        """绘制幽灵"""
        cx = self.x + TILE // 2
        cy = self.y + TILE // 2
        r = TILE // 2 - 1
        # 头部半圆
        pygame.draw.circle(screen, self.color, (cx, cy - 1), r)
        # 身体矩形
        pygame.draw.rect(screen, self.color, (self.x + 1, cy - 1, TILE - 2, r))
        # 底部锯齿
        w = (TILE - 2) // 3
        for i in range(3):
            bx = self.x + 1 + i * w
            pygame.draw.polygon(screen, self.color, [
                (bx, cy + r - 2),
                (bx + w // 2, cy + r + 2),
                (bx + w, cy + r - 2),
            ])
        # 眼睛
        eye_r = 3
        pygame.draw.circle(screen, WHITE, (cx - 4, cy - 3), eye_r)
        pygame.draw.circle(screen, WHITE, (cx + 4, cy - 3), eye_r)
        # 瞳孔（看向移动方向）
        dx, dy = 0, 0
        if self.dir == 'LEFT': dx = -1
        elif self.dir == 'RIGHT': dx = 1
        elif self.dir == 'UP': dy = -1
        elif self.dir == 'DOWN': dy = 1
        pygame.draw.circle(screen, BLACK, (cx - 4 + dx, cy - 3 + dy), 2)
        pygame.draw.circle(screen, BLACK, (cx + 4 + dx, cy - 3 + dy), 2)


# 创建4个幽灵（错开时间出屋：0/2/4/6秒）
ghosts = [
    Ghost(13, 13, RED,    'blinky', release_delay=120),
    Ghost(14, 13, PINK,   'pinky',  release_delay=240),
    Ghost(13, 14, CYAN,   'inky',   release_delay=360),
    Ghost(14, 14, ORANGE, 'clyde',  release_delay=480),
]


# 死亡重置
def reset_positions():
    global pac_x, pac_y, pac_dir, pac_next_dir
    pac_x = 13 * TILE
    pac_y = 22 * TILE
    pac_dir = 'STOP'
    pac_next_dir = 'STOP'
    for g in ghosts:
        g.x = g.home_x
        g.y = g.home_y
        g.dir = 'UP'
        g.exiting = True
        g.release_timer = g.release_delay


def check_ghost_collision():
    """检测吃豆人是否碰到幽灵"""
    pac_rect = pygame.Rect(pac_x + 2, pac_y + 2, TILE - 4, TILE - 4)
    for ghost in ghosts:
        ghost_rect = pygame.Rect(ghost.x + 2, ghost.y + 2, TILE - 4, TILE - 4)
        if pac_rect.colliderect(ghost_rect):
            return True
    return False


def draw_game_over():
    font_big = pygame.font.SysFont("microsoftyahei", 48)
    font_small = pygame.font.SysFont("microsoftyahei", 24)
    text1 = font_big.render("GAME OVER", True, RED)
    text2 = font_small.render(f"最终分数: {score}", True, WHITE)
    text3 = font_small.render("按 R 重新开始", True, YELLOW)
    screen.blit(text1, (WIDTH // 2 - text1.get_width() // 2, HEIGHT // 2 - 60))
    screen.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT // 2))
    screen.blit(text3, (WIDTH // 2 - text3.get_width() // 2, HEIGHT // 2 + 40))


# 游戏状态
game_over = False
death_timer = 0  # 死亡后短暂停顿

# 游戏主循环
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_r:
                # 重新开始
                game_over = False
                score = 0
                lives = 3
                dots_eaten = 0
                game_map[:] = [row[:] for row in LEVEL]
                reset_positions()
                continue
            if event.key == pygame.K_LEFT:
                pac_next_dir = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                pac_next_dir = 'RIGHT'
            elif event.key == pygame.K_UP:
                pac_next_dir = 'UP'
            elif event.key == pygame.K_DOWN:
                pac_next_dir = 'DOWN'

    # 死亡停顿
    if death_timer > 0:
        death_timer -= 1
        screen.fill(BLACK)
        draw_map()
        draw_pacman()
        for ghost in ghosts:
            ghost.draw()
        draw_hud()
        pygame.display.flip()
        continue

    if game_over:
        screen.fill(BLACK)
        draw_game_over()
        pygame.display.flip()
        continue

    # 移动吃豆人
    if is_aligned():
        # 优先走玩家新按的方向
        if can_move(pac_x, pac_y, pac_next_dir):
            pac_dir = pac_next_dir
        # 新方向走不了，当前方向也走不了，就什么都不做（等玩家按新方向）

    if can_move(pac_x, pac_y, pac_dir):
        if pac_dir == 'LEFT':
            pac_x -= PACMAN_SPEED
        elif pac_dir == 'RIGHT':
            pac_x += PACMAN_SPEED
        elif pac_dir == 'UP':
            pac_y -= PACMAN_SPEED
        elif pac_dir == 'DOWN':
            pac_y += PACMAN_SPEED

    # 隧道传送
    if pac_x < -TILE:
        pac_x = WIDTH - TILE
    elif pac_x >= WIDTH:
        pac_x = 0

    # 吃豆子
    col, row = get_tile(pac_x + TILE // 2, pac_y + TILE // 2)
    if 0 <= row < ROWS and 0 <= col < COLS:
        if game_map[row][col] == 2:
            game_map[row][col] = 4
            score += 10
            dots_eaten += 1
        elif game_map[row][col] == 3:
            game_map[row][col] = 4
            score += 50
            dots_eaten += 1

    # 嘴巴动画
    pac_anim_timer += 1
    if pac_anim_timer >= 4:
        pac_anim_timer = 0
        pac_frame += 1

    # 更新幽灵
    for ghost in ghosts:
        ghost.update()

    # 碰撞检测
    if check_ghost_collision():
        lives -= 1
        if lives <= 0:
            game_over = True
        else:
            reset_positions()
            death_timer = 60  # 停顿1秒

    # 绘制
    screen.fill(BLACK)
    draw_map()
    draw_pacman()
    for ghost in ghosts:
        ghost.draw()
    draw_hud()
    pygame.display.flip()

pygame.quit()
sys.exit()
