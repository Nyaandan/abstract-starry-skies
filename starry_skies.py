from turtle import *
import random
import time

sky_color = "midnightblue"
star_colors = ["ivory", "gold", "cyan"]
max_density = 4
size_min = 6
size_max = 12
half_width = round(window_width()/2)
half_height = round(window_height()/2)
anim_speed = 0
stars_to_draw = 0

# Computes a random position within the screen's bounds
def random_position():
    pos_x = random.randint(-half_width, half_width)
    pos_y = random.randint(-half_height, half_height)
    return pos_x, pos_y

def draw_star(x, y, size):
    global stars_to_draw
    goto(x, y)
    dot(size)
    stars_to_draw -= 1

def draw_random_star():
    coords = random_position()
    size = random.randint(size_min, size_max)
    draw_star(coords[0], coords[1], size)

# A constellation is a collection of stars connected by a line
def draw_constellation(stars):
    global stars_to_draw
    color(random.choice(star_colors))

    pendown()
    # Draw the first star at the initial position
    dot(random.randint(size_min, size_max))
    stars_to_draw -= 1
    for s in range(1, stars):
        draw_random_star()
    penup()

def paint_sky(star_count):
    global stars_to_draw
    stars_to_draw = star_count
    bgcolor(sky_color)
    speed(anim_speed)
    hideturtle()

    while(stars_to_draw > 0):
        # Gives a random initial position to each constellation
        new_pos = random_position()
        goto(new_pos[0], new_pos[1])
        stars = random.randint(1, min(stars_to_draw, max_density))
        draw_constellation(stars)

# Test with <reps> random skies of <stars> stars each.
def benchmark(reps, stars):
    times = []
    time_debut = time.time()
    time_last = time_debut
    for _ in range(reps):
        clear()
        paint_sky(stars)
        times.append(time.time() - time_last)
        time_last = time.time()
    print("total:", time.time() - time_debut)
    print("avg:", sum(times)/ len(times))

penup()
paint_sky(24)
#benchmark(12, 24)
done()