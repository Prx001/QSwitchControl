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
from PyQt5.QtTest import QTest


def take_closest(num, collection):
	return min(collection, key=lambda x: abs(x - num))


class SwitchCircle(QWidget):
	def __init__(self, parent, move_range: list, color, animation_curve, animation_duration, circle_animation_duration):
		super().__init__(parent=parent)
		self.color = color
		self.move_range = move_range
		self.size = 18
		self.circle_anim_duration = circle_animation_duration
		self.animation = QPropertyAnimation(self, b"pos")
		self.animation.setEasingCurve(animation_curve)
		self.animation.setDuration(animation_duration)
		self.circle_animation = QPropertyAnimation(self, b"circle_size")
		self.circle_animation.setDuration(self.circle_anim_duration)

	@pyqtProperty(float)
	def circle_size(self):
		return self.size

	@circle_size.setter
	def circle_size(self, value):
		self.size = value
		self.update()

	def paintEvent(self, event):
		painter = QPainter()
		painter.begin(self)
		painter.setRenderHint(QPainter.HighQualityAntialiasing)
		painter.setPen(Qt.NoPen)
		painter.setBrush(QColor(self.color))
		painter.drawEllipse(0, 0, self.size, self.size)
		painter.end()

	def set_color(self, value):
		self.color = value
		self.update()

	def grow_on_press(self):
		self.move_range[0] = 3
		self.move_range[1] = self.parent().width() - 26
		self.circle_animation.setStartValue(self.size)
		self.circle_animation.setEndValue(22)
		self.circle_animation.start()
		QTest.qWait(self.circle_anim_duration)
		self.parent().update_circle_position(reset_x=True)

	def shrink_on_release(self, reset_x: bool):
		self.move_range[0] = 5
		self.move_range[1] = self.parent().width() - 23
		self.circle_animation.setStartValue(self.size)
		self.circle_animation.setEndValue(18)
		self.circle_animation.start()
		QTest.qWait(self.circle_anim_duration)
		self.parent().update_circle_position(reset_x)

	def mousePressEvent(self, event):
		self.animation.stop()
		self.grow_on_press()
		self.oldX = event.globalX()
		print(self.size)
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
			if self.new_x != self.move_range[0] and self.new_x != self.move_range[1]:
				go_to = take_closest(self.new_x, self.move_range)
				if go_to == self.move_range[0]:
					self.shrink_on_release(reset_x=False)
					self.animation.setStartValue(self.pos())
					self.animation.setEndValue(QPoint(self.move_range[0], self.y()))
					self.animation.start()
					self.parent().setChecked(False)
				elif go_to == self.move_range[1]:
					self.shrink_on_release(reset_x=False)
					self.animation.setStartValue(self.pos())
					self.animation.setEndValue(QPoint(self.move_range[1], self.y()))
					self.animation.start()
					self.parent().setChecked(True)
			else:
				if self.new_x == self.move_range[0]:
					self.parent().setChecked(False)
				elif self.new_x == self.move_range[1]:
					self.parent().setChecked(True)
				self.shrink_on_release(reset_x=True)
			print(self.size)
		except AttributeError:
			pass
		return super().mouseReleaseEvent(event)


class SwitchControl(QCheckBox):
	def __init__(self, parent=None, bg_color="#777777", circle_color="#DDD", active_color="#aa00ff",
				 animation_curve=QEasingCurve.OutBounce, animation_duration=500, circle_animation_duration=50,
				 checked: bool = False,
				 change_cursor=True):
		if parent is None:
			super().__init__()
		else:
			super().__init__(parent=parent)
		self.setFixedSize(60, 28)
		if checked:
			self.setChecked(True)
		if change_cursor:
			self.setCursor(Qt.PointingHandCursor)
		self.bg_color = bg_color
		self.circle_color = circle_color
		self.active_color = active_color
		self.animation_curve = animation_curve
		self.animation_duration = animation_duration
		self.__min_x = 5
		self.__max_x = self.width() - 23
		self.__circle = SwitchCircle(self, [self.__min_x, self.__max_x], self.circle_color,
									 self.animation_curve, self.animation_duration, circle_animation_duration)
		if not self.isChecked():
			self.__circle.move(self.__min_x, self.__min_x)
		elif self.isChecked():
			self.__circle.move(self.__max_x, self.__min_x)
		self.auto = False
		self.pos_on_press = None
		self.animation = QPropertyAnimation(self.__circle, b"pos")
		self.animation.setEasingCurve(animation_curve)
		self.animation.setDuration(animation_duration)

	def update_circle_position(self, reset_x: bool):
		if reset_x:
			if not self.isChecked():
				self.__circle.move(self.__circle.move_range[0], self.__circle.move_range[0])
			elif self.isChecked():
				self.__circle.move(self.__circle.move_range[1], self.__circle.move_range[0])
		elif not reset_x:
			self.__circle.move(self.__circle.x(), self.__circle.move_range[0])

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
			self.animation.setEndValue(QPoint(self.__circle.move_range[1], self.__circle.y()))
			self.setChecked(True)
		if not checked:
			self.animation.setEndValue(QPoint(self.__circle.move_range[0], self.__circle.y()))
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
