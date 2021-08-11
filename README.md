# QSwitchControl
## Custom toggle-switch widget implemented in PyQt5 for PyQt5 applications!


https://user-images.githubusercontent.com/67240789/128912103-b24d7321-a7d6-4b1b-bbdc-562dbd20b358.mp4



### An easy-to-use and modern toggle switch for Qt Python binding PyQt
QSwitchControl is a custom toggle-switch widget inherited from 'QCheckBox' class, and acts as a checkbox alternative widget in your PyQt5 application.

## How to use?
### Installation
The package is available on [PyPi](https://pypi.org) so as always use pip for installation:
```
pip install QSwitchControl
```

### Usage in your Python application
First of all, as expected, you need to import the package.
Import 'SwitchControl' class from the package:
```python
from QSwitchControl import SwitchControl
```
Now the class is ready to use!
SwitchControl is an alternative widget for QCheckBox from Qt framework, same methods, same usage and that's how it works.
There are things you can define for your SwitchControl, like the circle color, background color, active color, animation easing curve, animation duration and some other things, but you can use default values. The package contains a '__main__' script so you can test the widget easily:
```
python -m QSwitchControl
```
Bellow is the '__main__' script:
```python
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout

from QSwitchControl import SwitchControl


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.resize(400, 400)
		self.setWindowTitle("SwitchControl test")
		self.setStyleSheet("""
		background-color: #222222;
		""")
		switch_control = SwitchControl()
		hbox = QHBoxLayout()
		hbox.addWidget(switch_control, Qt.AlignCenter, Qt.AlignCenter)
		self.setLayout(hbox)
		self.show()


app = QApplication(sys.argv)
form = Form()
if __name__ == '__main__':
	sys.exit(app.exec_())
```
In this script we used the default values for our widget:
```python
switch_control = SwitchControl()
```
You can define the values yourself. Bellow is an example:
```python
switch_control = SwitchControl(bg_color="#777777", circle_color="#DDD", active_color="#aa00ff", animation_curve=QtCore.QEasingCurve.InOutCubic, animation_duration=300, checked=True, change_cursor=False)
```
# Qt Designer integration
Qt Designer is a very extensible tool, even can support your custom widgets! It means you can interact with your custom widget just as you do with Qt widgets, like QPushButton, QCheckBox, you can drag and drop them on your form, change their sizes, set properties and so on.
Qt Designer can load plugins, and you can load your custom widgets through plugins, then your custom widget is available in Qt Designer Widget Box. In C++, using Qt Creator IDE you can create your custom widgets and compile them to .dll file, then you put the dll file (your plugin) into Qt Designer's relative path for plugins, and that's it you can use your widget in Designer. But, here in python the story is a little different. PyQt supports this plugin developement and integrate *Python based* Qt custom widgets in Qt Designer. [Learn more about integrating PyQt custom widgets in Qt Designer](https://wiki.python.org/moin/PyQt/Using_Python_Custom_Widgets_in_Qt_Designer) There is the Qt Designer plugin for QSwitchControl in package, [QSwitchControlplugin.py](https://github.com/Prx001/QSwitchControl/blob/main/QSwitchControlplugin.py). You can load it to your Qt Designer.
