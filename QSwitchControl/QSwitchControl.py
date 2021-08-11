"""
MIT License

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
SOFTWARE.
"""
from PyQt5.QtCore import Qt, QPoint, pyqtSlot, pyqtProperty, QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import QWidget, QCheckBox
from PyQt5.QtGui import QPainter, QColor


def take_closest(num, collection):
	return min(collection, key=lambda x: abs(x - num))


class SwitchCircle(QWidget):
	def __init__(self, parent, move_range: tuple, color, animation_curve, animation_duration):
		super().__init__(parent=parent)
		self.color = color
		self.move_range = move_range
		self.animation = QPropertyAnimation(self, b"pos")
		self.animation.setEasingCurve(animation_curve)
		self.animation.setDuration(animation_duration)

	def paintEvent(self, event):
		painter = QPainter()
		painter.begin(self)
		painter.setRenderHint(QPainter.HighQualityAntialiasing)
		painter.setPen(Qt.NoPen)
		painter.setBrush(QColor(self.color))
		painter.drawEllipse(0, 0, 22, 22)
		painter.end()

	def set_color(self, value):
		self.color = value
		self.update()

	def mousePressEvent(self, event):
		self.animation.stop()
		self.oldX = event.globalX()
		return super().mousePressEvent(event)

	def mouseMoveEvent(self, event):
		delta = event.globalX() - self.oldX
		self.new_x = delta + self.x()
		if self.new_x < self.move_range[0]:
			self.new_x += (self.move_range[0] - self.new_x)
		if self.new_x > self.move_range[1]:
			self.new_x -= (self.new_x - self.move_range[1])
		self.move(self.new_x, self.y())
		self.oldX = event.globalX()
		return super().mouseMoveEvent(event)

	def mouseReleaseEvent(self, event):
		try:
			go_to = take_closest(self.new_x, self.move_range)
			if go_to == self.move_range[0]:
				self.animation.setStartValue(self.pos())
				self.animation.setEndValue(QPoint(go_to, self.y()))
				self.animation.start()
				self.parent().setChecked(False)
			elif go_to == self.move_range[1]:
				self.animation.setStartValue(self.pos())
				self.animation.setEndValue(QPoint(go_to, self.y()))
				self.animation.start()
				self.parent().setChecked(True)
		except AttributeError:
			pass
		return super().mouseReleaseEvent(event)


class SwitchControl(QCheckBox):
	def __init__(self, parent=None, bg_color="#777777", circle_color="#DDD", active_color="#aa00ff",
	             animation_curve=QEasingCurve.OutBounce, animation_duration=500, checked: bool = False,
	             change_cursor=True):
		if parent is None:
			super().__init__()
		else:
			super().__init__(parent=parent)
		self.setFixedSize(60, 28)
		if change_cursor:
			self.setCursor(Qt.PointingHandCursor)
		self.bg_color = bg_color
		self.circle_color = circle_color
		self.animation_curve = animation_curve
		self.animation_duration = animation_duration
		self.__circle = SwitchCircle(self, (3, self.width() - 26), self.circle_color, self.animation_curve,
		                             self.animation_duration)
		self.__circle_position = 3
		self.active_color = active_color
		self.auto = False
		self.pos_on_press = None
		if checked:
			self.__circle.move(self.width() - 26, 3)
			self.setChecked(True)
		elif not checked:
			self.__circle.move(3, 3)
			self.setChecked(False)
		self.animation = QPropertyAnimation(self.__circle, b"pos")
		self.animation.setEasingCurve(animation_curve)
		self.animation.setDuration(animation_duration)

	def get_bg_color(self):
		return self.bg_color

	@pyqtSlot(str)
	def set_bg_color(self, value):
		self.bg_color = value
		self.update()

	backgroundColor = pyqtProperty(str, get_bg_color, set_bg_color)

	def get_circle_color(self):
		return self.circle_color

	@pyqtSlot(str)
	def set_circle_color(self, value):
		self.circle_color = value
		self.__circle.set_color(self.circle_color)
		self.update()

	circleBackgroundColor = pyqtProperty(str, get_circle_color, set_circle_color)

	def get_animation_duration(self):
		return self.animation_duration

	@pyqtSlot(int)
	def set_animation_duration(self, value):
		self.animation_duration = value
		self.animation.setDuration(value)

	animationDuration = pyqtProperty(int, get_animation_duration, set_animation_duration)

	def get_active_color(self):
		return self.active_color

	@pyqtSlot(str)
	def set_active_color(self, value):
		self.active_color = value
		self.update()

	activeColor = pyqtProperty(str, get_active_color, set_active_color)

	def start_animation(self, checked):
		self.animation.stop()
		self.animation.setStartValue(self.__circle.pos())
		if checked:
			self.animation.setEndValue(QPoint(self.width() - 26, self.__circle.y()))
			self.setChecked(True)
		if not checked:
			self.animation.setEndValue(QPoint(3, self.__circle.y()))
			self.setChecked(False)
		self.animation.start()

	def paintEvent(self, event):
		painter = QPainter()
		painter.begin(self)
		painter.setRenderHint(QPainter.HighQualityAntialiasing)
		painter.setPen(Qt.NoPen)
		if not self.isChecked():
			painter.setBrush(QColor(self.bg_color))
			painter.drawRoundedRect(0, 0, self.width(), self.height(), self.height() / 2, self.height() / 2)
		elif self.isChecked():
			painter.setBrush(QColor(self.active_color))
			painter.drawRoundedRect(0, 0, self.width(), self.height(), self.height() / 2, self.height() / 2)

	def hitButton(self, pos):
		return self.contentsRect().contains(pos)

	def mousePressEvent(self, event):
		self.auto = True
		self.pos_on_press = event.globalPos()
		return super().mousePressEvent(event)

	def mouseMoveEvent(self, event):
		if event.globalPos() != self.pos_on_press:
			self.auto = False
		return super().mouseMoveEvent(event)

	def mouseReleaseEvent(self, event):
		if self.auto:
			self.auto = False
			self.start_animation(not self.isChecked())
