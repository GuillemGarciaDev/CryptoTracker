"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = ['icon.png']
OPTIONS = {
    'argv_emulation': True,
    'iconfile':'icon.png',
    'packages': ['rumps', 'requests']
}

setup(
    app=APP,
    name='CryptoBar',
    py_modules=['toolbar', 'request'],
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)