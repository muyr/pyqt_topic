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

class MSignalMap(QWidget):
    def __init__(self, parent = None):
        super(MSignalMap, self).__init__(parent)

        self.data = ["pPyramid", "pCone", "pCube","pCylinder","pHelix","pTorus", "pSphere","pPrism","pSolid"]
        self.cnLabel = ["Èý½Ç", "Ô²×¶", "·½¿é", "Ô²Öù", "ÂÝÐý", "Ô²»·", "Ô²Çò", "ÀâÖù", "°ËÃæÌå"]
        self.initUI()

    def initUI(self):
        lay = QVBoxLayout()
        mapper = QSignalMapper(self)
        for i in range(len(self.cnLabel)):
            button = QPushButton((self.cnLabel[i]).decode('gbk'))
            self.connect(button, SIGNAL('clicked()'), mapper, SLOT('map()'))
            mapper.setMapping(button, i)
            lay.addWidget(button)
        self.connect(mapper, SIGNAL('mapped(int)'), self.buttonClicked)
        self.setLayout(lay)
        
    def buttonClicked(self, index):
        objName = self.data[index]
        print objName
        #-------------------< do some process >--------------------#
        '''
        results = cmds.ls('*' + objName + '*')

        cmds.select(cl = True)
        cmds.select(results[0])
        '''

##     ##    ###    #### ##    ## 
###   ###   ## ##    ##  ###   ## 
#### ####  ##   ##   ##  ####  ## 
## ### ## ##     ##  ##  ## ## ## 
##     ## #########  ##  ##  #### 
##     ## ##     ##  ##  ##   ### 
##     ## ##     ## #### ##    ## 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MSignalMap()
    test.show()
    sys.exit(app.exec_())
