#!/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr

tk = TkDrawer()
try:
    for name in ["cube_test", "tetrahedron", "octahedron", "ccc", "cube", "box", "king", "cow"]:
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        Poly = Polyedr(f"data/{name}.geom")
        Poly.draw(tk)
        delta_time = time() - start_time
        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
        print("сумма площадей проекций "
        "«граней с полностью видимыми рёбрами», "
        "образующих с горизонтальной плоскостью "
        "угол не более π/7, центр которых находится"
        "строго вне куба единичного объёма с центром"
        "в начале координат", Poly.sum_area)
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
