# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\OneDrive\\moovel\\python-sha-512.py'],
             pathex=['C:\\cygwin\\home\\ALTMAMA\\pyinstaller-develop\\python-sha-512'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             cipher=block_cipher)
pyz = PYZ(a.pure,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='python-sha-512.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
