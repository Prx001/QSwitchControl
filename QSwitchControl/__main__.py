"""MIT License

Copyright (c) 2021 Parsa.py

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QColorDialog
from Form import Ui_Form
from Classic.QSwitchControl import SwitchControl as ClassicSwitchControl
from Modern.QSwitchControl import SwitchControl as ModernSwitchControl
class Form(QWidget, Ui_Form):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.classic_switch_control = ClassicSwitchControl()
		self.modern_switch_control = ModernSwitchControl()
		self.init_ui()
	def init_ui(self):
		self.classic_switch_control.setToolTip("SwitchControl with Classic style")
		self.modern_switch_control.setToolTip("SwitchControl with Modern style")
		classic_circle_color = QPushButton("Set circle color")
		classic_circle_color.setFixedSize(classic_circle_color.sizeHint())
		classic_circle_color.clicked.connect(self.open_color_dialog)
		classic_active_color = QPushButton("Set active color")
		classic_active_color.setFixedSize(classic_active_color.sizeHint())
		classic_active_color.clicked.connect(self.open_color_dialog)
		classic_bg_color = QPushButton("Set background color")
		classic_bg_color.setFixedSize(classic_bg_color.sizeHint())
		classic_bg_color.clicked.connect(self.open_color_dialog)
		h_box1 = QHBoxLayout()
		h_box1.addWidget(classic_circle_color)
		h_box1.addWidget(classic_active_color)
		h_box1.addWidget(classic_bg_color)
		# verticalLayout_4 = classic_group_box
		self.verticalLayout_4.addWidget(self.classic_switch_control, Qt.AlignCenter, Qt.AlignCenter)
		self.verticalLayout_4.addLayout(h_box1)


		modern_circle_color = QPushButton("Set circle color")
		modern_circle_color.setFixedSize(modern_circle_color.sizeHint())
		modern_circle_color.clicked.connect(self.open_color_dialog)
		modern_active_color = QPushButton("Set active color")
		modern_active_color.setFixedSize(modern_active_color.sizeHint())
		modern_active_color.clicked.connect(self.open_color_dialog)
		modern_bg_color = QPushButton("Set background color")
		modern_bg_color.setFixedSize(modern_bg_color.sizeHint())
		modern_bg_color.clicked.connect(self.open_color_dialog)
		h_box2 = QHBoxLayout()
		h_box2.addWidget(modern_circle_color)
		h_box2.addWidget(modern_active_color)
		h_box2.addWidget(modern_bg_color)
		# verticalLayout_5 = modern_group_box
		self.verticalLayout_5.addWidget(self.modern_switch_control, Qt.AlignCenter, Qt.AlignCenter)
		self.verticalLayout_5.addLayout(h_box2)
		self.show()
	def open_color_dialog(self, target):
		color = QColorDialog.getColor(parent=self.container_widget, title="Choose color", options=QColorDialog.ShowAlphaChannel)
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())