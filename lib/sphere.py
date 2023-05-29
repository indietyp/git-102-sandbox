"""
Code taken from <https://rosettacode.org/wiki/Draw_a_sphere#Python>

Licenced under
[GNU Free Documentation License](https://www.gnu.org/licenses/fdl-1.3.en.html).
"""

import math

shades = ('.', ':', '!', '*', 'o', 'e', '&', '#', '%', '@')


def normalize(vertex):
    length = math.sqrt(vertex[0] ** 2 + vertex[1] ** 2 + vertex[2] ** 2)

    return vertex[0] / length, vertex[1] / length, vertex[2] / length


def dot(x, y):
    d = x[0] * y[0] + x[1] * y[1] + x[2] * y[2]
    return -d if d < 0 else 0


def draw_sphere(*, radius, bias, ambient, light):
    for i in range(int(math.floor(-radius)), int(math.ceil(radius) + 1)):
        x = i + 0.5
        line = ''

        start = int(math.floor(-2 * radius))
        end = int(math.ceil(2 * radius) + 1)

        for j in range(start, end):
            y = j / 2 + 0.5
            if x * x + y * y <= radius * radius:
                vec = normalize((x, y, math.sqrt(radius * radius - x * x - y * y)))
                b = dot(light, vec) ** bias + ambient
                intensity = int((1 - b) * (len(shades) - 1))
                line += shades[intensity] if 0 <= intensity < len(shades) else shades[0]
            else:
                line += ' '

        print(line)


light = normalize((30, 30, -50))

draw_sphere(radius=20, bias=4, ambient=0.1, light=light)
draw_sphere(radius=10, bias=2, ambient=0.4, light=light)
