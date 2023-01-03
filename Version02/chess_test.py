import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MovingObject(QGraphicsEllipseItem):
    def __init__(self, x, y, r,app):
        super().__init__(0, 0, r, r)
        self.setPos(x, y)
        self.setBrush(Qt.blue)
        self.setAcceptHoverEvents(True)
        self.app = app

    # mouse hover event
    def hoverEnterEvent(self, event):
        self.app.instance().setOverrideCursor(Qt.OpenHandCursor)

    def hoverLeaveEvent(self, event):
        self.app.instance().restoreOverrideCursor()

    # mouse click event
    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        orig_cursor_position = event.lastScenePos()
        updated_cursor_position = event.scenePos()

        orig_position = self.scenePos()

        updated_cursor_x = updated_cursor_position.x() - orig_cursor_position.x() + orig_position.x()
        updated_cursor_y = updated_cursor_position.y() - orig_cursor_position.y() + orig_position.y()
        self.setPos(QPointF(updated_cursor_x, updated_cursor_y))

    def mouseReleaseEvent(self, event):
        print('x: {0}, y: {1}'.format(self.pos().x(), self.pos().y()))

class GraphicView(QGraphicsView):
    def __init__(self,app):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)       
        self.setSceneRect(0, 0, 1200, 1000)
        self.moveObject = MovingObject(50, 50, 40,app)
        # self.moveObject2 = MovingObject(100, 100, 100)
        self.scene.addItem(self.moveObject)
        # self.scene.addItem(self.moveObject2)

class MainWindow(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.setWindowTitle("Xadrez")
        self.setWindowIcon(QIcon('./images/bk.png'))
        self.mainwidget = GraphicView(app)
        self.setCentralWidget(self.mainwidget)

def main():
    app = QApplication([])
    win = MainWindow(app)  
    win.show()
    app.exec()
    # app = QApplication(sys.argv)
    # view = GraphicView(app)
    # view.show()
    # sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()
    
