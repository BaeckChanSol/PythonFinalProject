from distutils.core import setup, Extension

#python.exe setup.py sdist
#python.exe setup.py install
cMod = Extension('Spam', sources=['Spammodule.cpp'])
setup(name='FindFor',
      version=1.0,
      ext_package='pkg',
      py_modules=['DataBase' 'FrameWork', 'Gmail', 'Gmap', 'GraphData', 'Telegram', 'xmlControl', ],
      ext_modules=[cMod]
      )