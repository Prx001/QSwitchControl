import pathlib

from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
setup(
	name="PyQt6_SwitchControl",
	version="1.0.4.post1",
	description="An easy-to-use and modern toggle switch for Qt Python binding PyQt",
	long_description=README,
	long_description_content_type="text/markdown",
	url="https://github.com/M1GW/PyQt6_SwitchControl",
	author="Parsa.py",
	author_email="munichbayern2005@gmail.com",
	maintaine="M1GW",
	license="MIT",
	classifiers=[
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",
		"Programming Language :: Python :: 3.11",
		"Programming Language :: Python :: 3.12",
		"Programming Language :: Python :: Implementation :: CPython"
	],
	# py_modules=["__init__", "__main__", "QSwitchControl", "QSwitchControlplugin"],
	packages=["PyQt6_SwitchControl"],
	entry_points={
		'qt_designer_widgets': [
			'switch_control = designer_plugin:registerCustomWidgets',
		],
	},
	include_package_data=True,
	install_requires=["PyQt6"]
)
