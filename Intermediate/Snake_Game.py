import turtle
import random

# ─── SETUP ────────────────────────────────────────────
screen = turtle.Screen()
screen.title("Snake — Boss Edition")
screen.bgcolor("#0d1117")
screen.setup(width=620, height=620)
screen.tracer(0)          # we control when to draw

# ─── SCORE DISPLAY ────────────────────────────────────
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("white")
score_display.goto(0, 270)

# ─── FOOD ─────────────────────────────────────────────
food = turtle.Turtle()
food.shape("circle")
food.color("#FF4757")
food.shapesize(0.8)
food.penup()
food.speed(0)
food.goto(100, 100)

# ─── GAME STATE ───────────────────────────────────────
snake_segments = []
score = 0
high_score = 0
direction = "Right"
next_direction = "Right"
game_running = True
speed = 150       # milliseconds per tick (lower = faster)

GRID = 20         # grid cell size in pixels
BOUNDS = 280      # wall boundary

# ─── BUILD INITIAL SNAKE (3 segments) ─────────────────
def create_segment(x, y):
    seg = turtle.Turtle()
    seg.shape("square")
    seg.color("#00FF88")
    seg.shapesize(0.9)
    seg.penup()
    seg.speed(0)
    seg.goto(x, y)
    return seg

for i in range(3):
    snake_segments.append(create_segment(-i * GRID, 0))

# ─── FOOD SPAWNER ─────────────────────────────────────
def spawn_food():
    while True:
        x = random.randint(-13, 13) * GRID
        y = random.randint(-13, 13) * GRID
        # Make sure food doesn't spawn on snake
        positions = [(s.xcor(), s.ycor()) for s in snake_segments]
        if (x, y) not in positions:
            food.goto(x, y)
            break

# ─── SCORE UPDATE ─────────────────────────────────────
def update_score():
    score_display.clear()
    score_display.write(
        f"Score: {score}   High Score: {high_score}",
        align="center",
        font=("Courier", 14, "bold")
    )

# ─── DIRECTION CONTROLS ───────────────────────────────
# Prevent reversing into yourself
def go_up():
    global next_direction
    if direction != "Down":
        next_direction = "Up"

def go_down():
    global next_direction
    if direction != "Up":
        next_direction = "Down"

def go_left():
    global next_direction
    if direction != "Right":
        next_direction = "Left"

def go_right():
    global next_direction
    if direction != "Left":
        next_direction = "Right"

screen.listen()
screen.onkey(go_up,    "Up")
screen.onkey(go_down,  "Down")
screen.onkey(go_left,  "Left")
screen.onkey(go_right, "Right")
screen.onkey(go_up,    "w")
screen.onkey(go_down,  "s")
screen.onkey(go_left,  "a")
screen.onkey(go_right, "d")

# ─── GAME OVER ────────────────────────────────────────
def game_over():
    global game_running
    game_running = False

    msg = turtle.Turtle()
    msg.hideturtle()
    msg.penup()
    msg.color("#FF4757")
    msg.goto(0, 30)
    msg.write("GAME OVER", align="center",
              font=("Courier", 36, "bold"))

    msg.color("white")
    msg.goto(0, -20)
    msg.write(f"Final Score: {score}",
              align="center", font=("Courier", 18, "normal"))

    msg.color("#555")
    msg.goto(0, -70)
    msg.write("Close and run again to restart",
              align="center", font=("Courier", 11, "normal"))

# ─── MAIN GAME LOOP ───────────────────────────────────
def game_loop():
    global direction, score, high_score, speed

    if not game_running:
        return

    direction = next_direction

    # Calculate new head position
    head = snake_segments[0]
    hx, hy = head.xcor(), head.ycor()

    if   direction == "Up":    hy += GRID
    elif direction == "Down":  hy -= GRID
    elif direction == "Right": hx += GRID
    elif direction == "Left":  hx -= GRID

    # ── Wall collision ──
    if abs(hx) > BOUNDS or abs(hy) > BOUNDS:
        game_over()
        return

    # ── Self collision ──
    for seg in snake_segments[1:]:
        if abs(seg.xcor() - hx) < 5 and abs(seg.ycor() - hy) < 5:
            game_over()
            return

    # ── Move: add new head, remove tail ──
    new_seg = create_segment(hx, hy)
    snake_segments.insert(0, new_seg)

    # ── Food eaten? ──
    if abs(head.xcor() - food.xcor()) < GRID and \
       abs(head.ycor() - food.ycor()) < GRID:
        score += 10
        if score > high_score:
            high_score = score
        update_score()
        spawn_food()
        speed = max(60, speed - 3)   # speed up, min 60ms
        # Don't remove tail — snake grows
    else:
        # Remove tail segment
        tail = snake_segments.pop()
        tail.hideturtle()
        del tail

    screen.update()
    screen.ontimer(game_loop, speed)   # schedule next tick

# ─── START ────────────────────────────────────────────
update_score()
spawn_food()
screen.ontimer(game_loop, speed)
turtle.done()