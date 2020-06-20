from distutils.core import setup, Extension

#python.exe setup.py sdist
#python.exe setup.py install
cMod = Extension('Spam', sources=['Spammodule.cpp'])
setup(name='FindFor',
      version=1.0,
      ext_package='pkg',
      py_modules=['DataBase' 'FrameWork', 'Gmail', 'Gmap', 'GraphData', 'Telegram', 'xmlControl', 'Setup'],
      ext_modules=[cMod],
      package_data=['구글지도.png', '텔레그램.png', 'G메일.png']
      )