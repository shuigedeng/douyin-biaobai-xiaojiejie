# douyin-biaobai-xiaojiejie
抖音表白小姐姐Python代码！

需要安装pip install PyInstaller
	   pip install PyQt5

执行main.py中的main方法进行打包成exe文件！


在Ubuntu上打的包在windows上用不了 我这个是在windows10上打的包 运行没问题

pip install pyqt5
pip install pyqt5-tools
在windows上用pip install pyinstaller  打包成exe文件执行不了
在pyinstaller官网上下载pyinstaller的安装包 然后用python setup.py install 安装
然后执行下面的代码就可以了
记住在confession.py中的图片路径只能是绝对路径不能是相对路径 否则打开没有图片

打包方式有2种 第一种是用如下命令打包
pyinstaller --paths C:/Users/Administrator/AppData/Local/Programs/Python/Python35/Lib/site-packages/PyQt5/Qt/bin -F -w confession.py

第二种就是用我这个main.py脚步打包
python main.py
	   
