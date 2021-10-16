#!/usr/bin/env python
import os
import re
import sys

from setuptools import setup

INFO_PLIST_TEMPLATE = '''\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleIdentifier</key>
    <string>%(name)s</string>
</dict>
</plist>
'''
try:
    with open(os.path.join(os.path.dirname(sys.executable), 'Info.plist'), 'w') as f:
        f.write(INFO_PLIST_TEMPLATE % {'name': 'rumps'})
except IOError:
    pass

with open('README.rst') as f:
    readme = f.read()
with open('CHANGES.rst') as f:
    changes = f.read()
with open('rumps/__init__.py') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name='rumps',
    version=version,
    description='Ridiculously Uncomplicated MacOS Python Statusbar apps.',
    author='Jared Suttles',
    url='https://github.com/jaredks/rumps',
    packages=['rumps', 'rumps.packages'],
    package_data={'': ['LICENSE']},
    long_description=readme + '\n\n' + changes,
    license='BSD License',
    install_requires=['pyobjc-framework-Cocoa'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: MacOS X',
        'Environment :: MacOS X :: Cocoa',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Objective C',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
