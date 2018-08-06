"""
__title__ = '将confession项目转换为exe文件'
__author__ = 'dt'
"""
from PyInstaller.__main__ import run

if __name__ == '__main__':
    opts = ['confession.py', '-w', '--onefile']
    #opts = ['confession.py', '-F']
    #opts = ['confession.py', '-F', '-w']
    #opts = ['confession.py', '-F', '-w', '--icon=TargetOpinionMain.ico','--upx-dir','upx391w']
    run(opts)

# pyinstaller --paths C:/Users/Administrator/AppData/Local/Programs/Python/Python35/Lib/site-packages/PyQt5/Qt/bin -F -w confession.py
