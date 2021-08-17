import pathlib

from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "QSwitchControl\\README.md").read_text()
setup(
	name="QSwitchControl",
	version="1.0.4",
	description="An easy-to-use and modern toggle switch for Qt Python binding PyQt",
	long_description=README,
	long_description_content_type="text/markdown",
	url="https://github.com/Prx001/QSwitchControl",
	author="Parsa.py",
	author_email="munichbayern2005@gmail.com",
	license="MIT",
	classifiers=[
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: Implementation :: CPython"
	],
	# py_modules=["__init__", "__main__", "QSwitchControl", "QSwitchControlplugin"],
	packages=["QSwitchControl"],
	include_package_data=True,
	install_requires=["PyQt5"]
)
