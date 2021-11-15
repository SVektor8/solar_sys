# coding: utf-8
# license: GPLv3

#gravitational_constant = 6.67408E-11   более тут не нужна
"""Гравитационная постоянная Ньютона G"""

'''Now in SpaceObject.move():

def calculate_force(body, space_objects):
    pass
def move_space_object(body, dt):
    pass
'''


def recalculate_space_objects_positions(space_objects, dt): #теперь работает через SpaceObject.move()
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """
    for obj in space_objects:
        obj.move(space_objects, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
