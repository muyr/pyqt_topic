# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.11
# Email : muyanru345@163.com
###################################################################
try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except ImportError:
    import sip
    sip.setapi("QString",  2)
    sip.setapi("QVariant",  2)
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
import sys

class MEventFilterWidget(QWidget):
    def __init__(self, parent = None):
        super(MEventFilterWidget, self).__init__(parent)
        self.setStyleSheet('font-family:Microsoft YaHei;font-size:12px;color:#cccccc')
        self.setWindowTitle('MEventFilterWidget')
        self.initUI()

    def initUI(self):
        #-------------------< Title >--------------------#
        titleLab = QLabel('I\'m the title widget')
        titleLay = QHBoxLayout()
        titleLay.setContentsMargins(5, 5, 5, 5)
        titleLay.addSpacing(10)
        titleLay.addWidget(titleLab)
        titleLay.addStretch()
        self.titleWidget = QWidget()
        self.titleWidget.setLayout(titleLay)

        #-------------------< Bottom >--------------------#
        self.bottomWidget = QWidget()
        authorLabel = QLabel('By Muyr')
        bottomLay = QHBoxLayout()
        bottomLay.setContentsMargins(5, 5, 5, 5)
        bottomLay.addStretch()
        bottomLay.addWidget(authorLabel)
        bottomLay.addSpacing(10)
        self.bottomWidget.setLayout(bottomLay)

        #-------------------< content widget >--------------------#
        contentWidget = QLabel('''eventFilter example
###################################################################
# Author: Mu yanru
# Date  : 2013.11
# Email : muyanru345@163.com
###################################################################
        	''')
        contentWidget.setStyleSheet('color:#000000')

        #-------------------< installEventFilter >--------------------#
        self.titleWidget.installEventFilter(self)
        self.bottomWidget.installEventFilter(self)

        mainLay = QVBoxLayout()
        mainLay.addWidget(self.titleWidget)
        mainLay.addStretch()
        mainLay.addWidget(contentWidget)
        mainLay.addStretch()
        mainLay.addWidget(self.bottomWidget)
        self.setLayout(mainLay)

    def eventFilter(self, object, event):
        if event.type() == QEvent.Paint:
            if object in [self.titleWidget, self.bottomWidget]:
                painter = QPainter(object)
                w = object.width()
                h = object.height()
                backgroudColor = QColor('#2a2a2a')
                brush = QBrush(backgroudColor)
                pen = QPen(backgroudColor)
                painter.setBrush(brush)
                painter.setPen(pen)
                painter.drawRect (0, 0, w, h)
                pen2 = QPen()
                pen2.setColor(QColor('#000000'))
                pen2.setWidth(1)
                painter.setPen(pen2)
                if object == self.titleWidget:
                    painter.drawLine (0, h-1, w, h-1)
                elif object == self.bottomWidget:
                    painter.drawLine (0, 0, w, 0)
                painter.end()
        return QWidget.eventFilter(self, object, event)


##     ##    ###    #### ##    ## 
###   ###   ## ##    ##  ###   ## 
#### ####  ##   ##   ##  ####  ## 
## ### ## ##     ##  ##  ## ## ## 
##     ## #########  ##  ##  #### 
##     ## ##     ##  ##  ##   ### 
##     ## ##     ## #### ##    ## 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MEventFilterWidget()
    test.show()
    sys.exit(app.exec_())
