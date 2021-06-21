from drawtool import DrawTool
import math

dt = DrawTool()
dt.set_XY_range(0, 10, -2, 2)
N = 20
x_spacing = 10 / N
x = 0
for k in range(1, N + 1):
    y = math.sin(x)
    dt.draw_point(x, y)
    x = x + x_spacing

dt.display()
