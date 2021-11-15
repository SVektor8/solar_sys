# coding: utf-8
# license: GPLv3

from typing import List
import pygame as pg
from solar_vis import scale_y, scale_x

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


class SpaceObject:

    def __init__(self, line: str):
        """Считывает данные о звезде из строки.

        Входная строка должна иметь слеюущий формат:

        Object <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
        """
        parsed = line.lower().split()

        self.type = parsed[0]
        self.R = float(parsed[1])
        self.color = parsed[2]
        self.m = float(parsed[3])
        self.x = float(parsed[4])
        self.y = float(parsed[5])
        self.Vx = float(parsed[6])
        self.Vy = float(parsed[7])

    def __str__(self):
        """Возвращает строку данных об объекте."""
        sep = ' '
        parameters = [self.type, str(self.R), self.color, str(self.m),
                      str(self.x), str(self.y), str(self.Vx), str(self.Vy)]
        line = sep.join(parameters)
        return line

    def move(self, space_objects, dt=1):
        Fx = Fy = 0
        x_sign =  1  # направление оси X у программы (1 - если вправо, -1 - если влево)
        y_sign = -1  # направление оси Y у программы (1 - если вверх, -1 - если вниз)

        for obj in space_objects:
            if self == obj:
                continue
            r = ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5 \
 \
            # FIXED вариант небольшого фикса обработки аномалий при прохождении
            # планет друг через друга
            r = max(r, self.R + obj.R)
            x, y = obj.x - self.x, obj.y - self.y  # векторы расстояний от тела до другого объекта
            force = gravitational_constant * self.m * obj.m / r ** 2
            Fx += x_sign * force * x / r
            Fy += y_sign * force * y / r
        ax, ay = Fx / self.m, Fy / self.m
        self.x += self.Vx * dt + 0.5 * ax * dt ** 2
        self.y += y_sign * self.Vy * dt + 0.5 * ay * dt ** 2
        self.Vx += ax * dt
        self.Vy += ay * dt
        # FIXED write simple move func like solar_model.py move_space_object()
        # FIXED планеты почему-то двигаются не вокруг Солнца, а по другим траекториям

    def draw(self, surface):
        pg.draw.circle(surface, (255, 255, 255),
                           (scale_x(self.x), scale_y(self.y)), self.R)

        # FIXME добавить рисование объектов цветами, указанными в self.color, используя colors из config.py
