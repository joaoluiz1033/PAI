# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 22:33:12 2022

@author: danyz
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
from PyQt5.QtGui import QPixmap, QColor, QBrush
from PyQt5.QtCore import Qt


app = QApplication(sys.argv)
window = QWidget()


layout = QGridLayout()
window.setLayout(layout)


white_square = QPixmap(100, 100)
white_square.fill(QColor(Qt.white))


black_square = QPixmap(100, 100)
black_square.fill(QColor(160,82,45))
# Load the images for the chess pieces
white_pawn = QPixmap("white_pawn.png")
white_knight = QPixmap("white_knight.png")
white_bishop = QPixmap("white_bishop.png")
white_rook = QPixmap("white_rook.png")
white_queen = QPixmap("white_queen.png")
white_king = QPixmap("white_king.png")
black_pawn = QPixmap("black_pawn.png")
black_knight = QPixmap("black_knight.png")
black_bishop = QPixmap("black_bishop.png")
black_rook = QPixmap("black_rook.png")
black_queen = QPixmap("black_queen.png")
black_king = QPixmap("black_king.png")

# Add the squares and pieces to the grid layout in the correct order
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            square = QLabel()
            square.setPixmap(white_square)
            layout.addWidget(square, i, j)
        else:
            square = QLabel()
            square.setPixmap(black_square)
            layout.addWidget(square, i, j)

# Add the white pieces to the bottom of the board
for j in range(8):
    piece = QLabel()
    if j == 0 or j == 7:
        piece.setPixmap(white_rook)
    elif j == 1 or j == 6:
        piece.setPixmap(white_knight)
    elif j == 2 or j == 5:
        piece.setPixmap(white_bishop)
    elif j == 3:
        piece.setPixmap(white_queen)
    elif j == 4:
        piece.setPixmap(white_king)
    else:
        piece.setPixmap(white_pawn)
    

# Create the main window


# Show the main window
window.show()

# Run the main loop
app.exec_()

