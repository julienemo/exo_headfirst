def set_grid(length, width):
    grid = [0] * length
    for i in range(length):
        grid[i] = [0] * width
    return grid


# def count():


def decide_next(n, count):
    if n == 0:
        if count == 3:
            n = 1
        else:
            n = 0
    else:
        if (count > 3) or (count < 2):
            n = 0,
        else:
            n = 1
    return n


def draw_next():
    global grid
    global height
    global width
    for i in height:
        for i in width:
            grid[height][width] = decide_next()


height = 10
width = 10
grid = set_grid(height, width)
