# Qt事件过滤器
**By Muyr**
2013/12/5 16:20:39 
部分内容摘抄自《C++ GUI Qt编程 第二版》P133-134
## 应用背景
比如我们现在有两个widget，title和bottom，他们两个的需要重新定义绘图事件，来自定义绘制内容。

按照以往的方法，我们需要子类化每一个widget，然后重载他们的paintEvent事件.

如果只是因为绘图事件而子类化，或者这样的widget特别多的话，这时我们就需要事件过滤器

## 步骤
1. 通过对目标对象调用`installEventFilter()`来注册监视对象
2. 在监视对象的`eventFilter()`函数中处理目标对象的事件


<pre>
#-------------------< installEventFilter >--------------------#
class MEventFilterWidget(QWidget):
    def __init__(self, parent = None):
        super(MEventFilterWidget, self).__init__(parent)
		# ....
		# 安装注册事件过滤器
		self.titleWidget.installEventFilter(self)
		self.bottomWidget.installEventFilter(self)
		# ....

    def eventFilter(self, object, event):
        # 判断为绘图事件
        if event.type() == QEvent.Paint:
            # 事件对象是否为上面注册要监视的对象
            if object in [self.titleWidget, self.bottomWidget]:
                # widget的绘图事件的内容
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
        # 将控制权交给基类的eventFilter()
        return QWidget.eventFilter(self, object, event)
</pre> 

注意：如果在同一个对象上安装了多个事件处理器，那么就会按照安装顺序，从最近安装到最先安装的，依次激活这些事件处理器

