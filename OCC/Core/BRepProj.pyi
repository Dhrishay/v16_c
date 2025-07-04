from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.gp import *


class BRepProj_Projection:
    @overload
    def __init__(self, Wire: TopoDS_Shape, Shape: TopoDS_Shape, D: gp_Dir) -> None: ...
    @overload
    def __init__(self, Wire: TopoDS_Shape, Shape: TopoDS_Shape, P: gp_Pnt) -> None: ...
    def Current(self) -> TopoDS_Wire: ...
    def Init(self) -> None: ...
    def IsDone(self) -> bool: ...
    def More(self) -> bool: ...
    def Next(self) -> None: ...
    def Shape(self) -> TopoDS_Compound: ...

# harray1 classes
# harray2 classes
# hsequence classes

