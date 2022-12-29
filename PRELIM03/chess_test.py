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


white_square = QPixmap(50, 50)
white_square.fill(QColor(Qt.white))


black_square = QPixmap(50, 50)
black_square.fill(QColor(160,82,45))
# Load the images for the chess pieces
white_pawn = QPixmap("./images/wp.png")
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
piece = QLabel()
piece.setPixmap(white_pawn.size(1))

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
            layout.addWidget(piece, i,j)

# Add the white pieces to the bottom of the board
# for j in range(8):
#     piece = QLabel()
#     piece.setPixmap(white_pawn)    
#     layout.addWidget(piece, j)

# Create the main window


# Show the main window
window.show()

# Run the main loop
app.exec_()