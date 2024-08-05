# SwitchControl for PyQt6 <br/> (forked from [Prx001/QSwitchControl](https://github.com/Prx001/QSwitchControl))
## Custom toggle-switch widget implemented for \*PyQt6\* applications!
## 

https://user-images.githubusercontent.com/67240789/128912103-b24d7321-a7d6-4b1b-bbdc-562dbd20b358.mp4



### An easy-to-use and modern toggle switch for Qt Python binding PyQt
PyQt6_SwitchControl is a custom toggle-switch widget inherited from 'QCheckBox' class, and acts as a checkbox alternative widget in your PyQt6 application.
>This repository is a fork from [Prx001](https://github.com/Prx001/)'s [QSwitchControl](https://github.com/Prx001/QSwitchControl) project but the code has been modified to work with PyQt6.

## How to use?
### Installation
The package is available on [PyPi](https://pypi.org/project/PyQt6_SwitchControl) so as always use pip for installation:
```
pip install PyQt6_SwitchControl
```

### Usage in your Python application
First of all, as expected, you need to import the package.
Import 'SwitchControl' class from the package:
```python
from PyQt6_SwitchControl import SwitchControl
```
Now the class is ready to use!
SwitchControl is an alternative widget for QCheckBox from Qt framework, same methods, same usage and that's how it works.
There are things you can define for your SwitchControl, like the circle color, background color, active color, animation easing curve, animation duration and some other things, but you can use default values. The package contains a '__main__' script, so you can test the widget easily:
```
python -m PyQt6_SwitchControl
```
Bellow is the '__main__' script:
```python
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout

from PyQt6_SwitchControl import SwitchControl


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(400, 400)
        self.setWindowTitle("SwitchControl test")
        self.setStyleSheet("""
		background-color: #222222;
		""")
        switch_control = SwitchControl()
        h_box = QHBoxLayout()
        h_box.addWidget(switch_control, Qt.AlignmentFlag.AlignCenter, Qt.AlignmentFlag.AlignCenter)
        self.setLayout(h_box)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec()
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
Qt Designer is a very extensible tool, even can support your custom widgets!
It means you can interact with your custom widget just as you do with Qt 
widgets, like QPushButton, QCheckBox, you can drag and drop them on your 
form, change their sizes, set properties and so on. Qt Designer can load 
plugins, and you can load your custom widgets through plugins, then your 
custom widget is available in Qt Designer Widget Box. In C++, using Qt 
Creator IDE you can create your custom widgets and compile them to .dll file, 
then you put the dll file (your plugin) into Qt Designer's relative path for 
plugins, and that's it you can use your widget in Designer. But, here in python 
the story is a little different. PyQt supports this plugin development and 
integrate *Python based* Qt custom widgets in Qt Designer. [Learn more about integrating PyQt custom widgets in Qt Designer](https://wiki.python.org/moin/PyQt/Using_Python_Custom_Widgets_in_Qt_Designer) 
There is the Qt Designer 
plugin for PyQt6_SwitchControl in package, [PyQt6_SwitchControl_plugin.py](https://github.com/M1GW/PyQt6_SwitchControl/blob/main/PyQt6_SwitchControl/PyQt6_SwitchControl_plugin.py).
You can load it to your Qt Designer.
