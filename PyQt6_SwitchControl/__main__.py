"""
MIT License

Copyright (c) 2021 Parsa.py
Modified work Copyright (c) 2024 github/M1GW

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
SOFTWARE.
"""
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

