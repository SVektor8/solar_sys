# coding: utf-8
# license: GPLv3


class SpaceObject:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    m = 1
    """Масса планеты"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус планеты"""

    color = "green"

    def __init__(self, line):
        # FIXME look line 38 for star and 60 for planet of solar_input.py
        pass

    def __str__(self):
        # FIXME write like read_space_objects_data_from_file but write for solar_input.py
        pass

    def move(self):
        # FIXME write simple move func like solar_model.py move_space_object()
        pass

class Star(SpaceObject):
    color = "red"


class Planet(SpaceObject):
    color = "green"
