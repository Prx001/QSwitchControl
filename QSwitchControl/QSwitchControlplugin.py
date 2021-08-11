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
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin
from PyQt5.QtGui import QIcon, QPixmap

from QSwitchControl import SwitchControl


class SwitchControlPlugin(QPyDesignerCustomWidgetPlugin):
	def __init__(self, parent=None):
		super(SwitchControlPlugin, self).__init__(parent)
		self.initialized = False

	def initialize(self, core):
		if self.initialized:
			return
		self.initialized = True

	def isInitialized(self):
		return self.initialized

	def createWidget(self, parent):
		return SwitchControl(parent=parent)

	def name(self):
		return "SwitchControl"

	def group(self):
		return "Buttons"

	def icon(self):
		return QIcon(_logo_pixmap)

	def toolTip(self):
		return "A customized and modern toggle-switch"

	def whatsThis(self):
		return ""

	def isContainer(self):
		return False

	def domXml(self):
		return (
			'<widget class="SwitchControl" name=\"switchControl\">\n'
			"</widget>\n"
		)

	def includeFile(self):
		return "QSwitchControl"


_logo_16x16_xpm = []
_logo_pixmap = QPixmap(_logo_16x16_xpm)
