# QSignalMapper
**By Muyr**
2013/12/5 17:53:42 

## 背景
如果有好多个QPushButton，每个button的text不同，点下每个button后需要传递一个数据，之后执行的内容什么的都相似。

常规的话，我们需要逐个创建出来，然后对应好多个槽函数（因为button的任何signal都没法传递数据）

但是采用QSignalMapper来实现，我们即可少些很多代码。
QSignalMapper就如一个转发器，它可以把一个无参数的信号翻译成带int参数、QString参数、QObject*参数或者QWidget*参数的信号，并将之转发

上代码

<pre>
class MSignalMap(QWidget):
    def __init__(self, parent = None):
        super(MSignalMap, self).__init__(parent)

        self.data = ["pPyramid", "pCone", "pCube","pCylinder","pHelix","pTorus", "pSphere","pPrism","pSolid"]
        self.cnLabel = ["三角", "圆锥", "方块", "圆柱", "螺旋", "圆环", "圆球", "棱柱", "八面体"]
        self.initUI()

    def initUI(self):
        lay = QVBoxLayout()
        # 实例化一个QSignalMapper
        mapper = QSignalMapper(self)
        for i in range(len(self.cnLabel)):
            button = QPushButton((self.cnLabel[i]).decode('gbk'))
            # 连接
            self.connect(button, SIGNAL('clicked()'), mapper, SLOT('map()'))
            # 设置数据
            mapper.setMapping(button, i)
            lay.addWidget(button)
        self.connect(mapper, SIGNAL('mapped(int)'), self.buttonClicked)
        self.setLayout(lay)
        
    def buttonClicked(self, index):
        objName = self.data[index]
        print objName
</pre>