import sys
import pdb

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import interface_function as inter_fun

from chess_control import Controler


def add_piece(y):
    if y == "wp":
        return QPixmap("./images/wp.png")
    elif y == "wn":
        return QPixmap("./images/wn.png")
    elif y == "wb":
        return QPixmap("./images/wb.png")
    elif y == "wr":
        return QPixmap("./images/wr.png")
    elif y == "wq":
        return QPixmap("./images/wq.png")
    elif y == "wk":
        return QPixmap("./images/wk.png")
    elif y == "bp":
        return QPixmap("./images/bp.png")
    elif y == "bn":
        return QPixmap("./images/bn.png")
    elif y == "bb":
        return QPixmap("./images/bb.png")
    elif y == "br":
        return QPixmap("./images/br.png")
    elif y == "bq":
        return QPixmap("./images/bq.png")
    elif y == "bk":
        return QPixmap("./images/bk.png")