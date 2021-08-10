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
