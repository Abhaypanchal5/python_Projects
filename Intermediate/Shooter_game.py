import turtle
import random
import math

# ─────────────────────────────────────────────
#  SETUP
# ─────────────────────────────────────────────
screen = turtle.Screen()
screen.title("Space Shooter — Boss Edition")
screen.bgcolor("#0a0a0f")
screen.setup(width=700, height=750)
screen.tracer(0)

# ─────────────────────────────────────────────
#  GAME STATE
# ─────────────────────────────────────────────
score        = 0
lives        = 3
level        = 1
kill_count   = 0
bullet_cooldown = 0
player_dx    = 0
game_over_flag = False

PLAYER_SPEED = 20
BULLET_SPEED = 20
ENEMY_SPEED  = 3
GRID_BOUND   = 320
TOP_BOUND    = 380

# ─────────────────────────────────────────────
#  HUD
# ─────────────────────────────────────────────
hud = turtle.Turtle()
hud.hideturtle()
hud.penup()
hud.color("white")
hud.goto(0, 330)

def update_hud():
    hud.clear()
    hud.write(
        f"Score: {score}    Lives: {'♥ ' * lives}   Level: {level}",
        align="center",
        font=("Courier", 13, "bold")
    )

# ─────────────────────────────────────────────
#  PLAYER
# ─────────────────────────────────────────────
player = turtle.Turtle()
player.shape("triangle")
player.color("#00FF88")
player.shapesize(1.2, 0.8)
player.penup()
player.speed(0)
player.setheading(90)
player.goto(0, -300)

# ─────────────────────────────────────────────
#  CONTROLS
# ─────────────────────────────────────────────
def move_left():
    global player_dx
    player_dx = -PLAYER_SPEED

def move_right():
    global player_dx
    player_dx = PLAYER_SPEED

def stop_move():
    global player_dx
    player_dx = 0

def shoot():
    global bullet_cooldown
    if bullet_cooldown > 0:
        return
    b = turtle.Turtle()
    b.shape("circle")
    b.color("#FFD700")
    b.shapesize(0.3)
    b.penup()
    b.speed(0)
    b.setheading(90)
    b.goto(player.xcor(), player.ycor() + 20)
    bullets.append(b)
    bullet_cooldown = 8

screen.listen()
screen.onkeypress(move_left,  "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_left,  "a")
screen.onkeypress(move_right, "d")
screen.onkeyrelease(stop_move, "Left")
screen.onkeyrelease(stop_move, "Right")
screen.onkeyrelease(stop_move, "a")
screen.onkeyrelease(stop_move, "d")
screen.onkeypress(shoot, "space")
screen.onkeypress(shoot, "Up")
screen.onkeypress(shoot, "w")

# ─────────────────────────────────────────────
#  BULLETS
# ─────────────────────────────────────────────
bullets = []

# ─────────────────────────────────────────────
#  ENEMIES
# ─────────────────────────────────────────────
enemies = []

def spawn_enemy():
    e = turtle.Turtle()
    e.shape("square")
    e.color("#FF4757")
    e.shapesize(1.2)
    e.penup()
    e.speed(0)
    e.setheading(270)
    e.goto(random.randint(-300, 300), TOP_BOUND)
    enemies.append(e)

for _ in range(5):
    spawn_enemy()

# ─────────────────────────────────────────────
#  EXPLOSIONS
# ─────────────────────────────────────────────
explosions = []

def explode(x, y):
    e = turtle.Turtle()
    e.hideturtle()
    e.penup()
    e.goto(x, y)
    e.color("#FF922B")
    e.write("✦", align="center", font=("Arial", 20, "bold"))
    explosions.append([e, 8])

# ─────────────────────────────────────────────
#  GAME OVER SCREEN
# ─────────────────────────────────────────────
def show_game_over():
    msg = turtle.Turtle()
    msg.hideturtle()
    msg.penup()

    msg.color("#FF4757")
    msg.goto(0, 60)
    msg.write("GAME OVER", align="center",
              font=("Courier", 40, "bold"))

    msg.color("white")
    msg.goto(0, 0)
    msg.write(f"Final Score: {score}",
              align="center", font=("Courier", 18, "normal"))

    msg.color("#FFD700")
    msg.goto(0, -50)
    msg.write(f"Level Reached: {level}",
              align="center", font=("Courier", 14, "normal"))

    msg.color("#444444")
    msg.goto(0, -110)
    msg.write("Close window to exit",
              align="center", font=("Courier", 11, "normal"))

# ─────────────────────────────────────────────
#  GAME LOOP
# ─────────────────────────────────────────────
def game_loop():
    global score, lives, level, game_over_flag
    global bullet_cooldown, ENEMY_SPEED, kill_count, player_dx

    if game_over_flag:
        return

    # -- Move player --
    new_x = player.xcor() + player_dx
    new_x = max(-GRID_BOUND, min(GRID_BOUND, new_x))
    player.setx(new_x)

    # -- Move bullets --
    for b in bullets[:]:
        b.sety(b.ycor() + BULLET_SPEED)
        if b.ycor() > TOP_BOUND:
            b.hideturtle()
            bullets.remove(b)

    # -- Fire rate cooldown --
    if bullet_cooldown > 0:
        bullet_cooldown -= 1

    # -- Move enemies --
    for e in enemies[:]:
        e.sety(e.ycor() - ENEMY_SPEED)
        if e.ycor() < -TOP_BOUND:
            lives -= 1
            e.goto(random.randint(-300, 300), TOP_BOUND)
            update_hud()
            if lives <= 0:
                game_over_flag = True
                show_game_over()
                screen.update()
                return

    # -- Bullet vs enemy collision --
    for b in bullets[:]:
        for e in enemies[:]:
            dist = math.sqrt(
                (b.xcor() - e.xcor()) ** 2 +
                (b.ycor() - e.ycor()) ** 2
            )
            if dist < 20:
                explode(e.xcor(), e.ycor())
                score      += 10
                kill_count += 1

                b.hideturtle()
                if b in bullets:
                    bullets.remove(b)

                e.goto(random.randint(-300, 300), TOP_BOUND)
                update_hud()

                # level up every 5 kills
                if kill_count % 5 == 0:
                    level        += 1
                    ENEMY_SPEED  += 1
                    spawn_enemy()

                break

    # -- Tick down explosions --
    alive = []
    for item in explosions:
        item[1] -= 1
        if item[1] <= 0:
            item[0].clear()
            item[0].hideturtle()
        else:
            alive.append(item)
    explosions[:] = alive

    # -- Render --
    screen.update()
    screen.ontimer(game_loop, 16)   # ~60fps

# ─────────────────────────────────────────────
#  START
# ─────────────────────────────────────────────
update_hud()
screen.ontimer(game_loop, 16)
turtle.done()