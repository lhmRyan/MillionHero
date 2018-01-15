1. 下载安装ADB驱动，可以去http://adbdriver.com/下载。
2. 下载安装tesseract，我用的是4.0，可以到http://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-4.00.00dev.exe下载。安装的时候记得勾选简体中文。
3. 安装Anaconda，可以到https://www.anaconda.com/download/下载，我用的是Python 2.7版本的Anaconda 2.3。
4. 把这个项目里的adb和chrome driver文件夹添加到系统路径PATH中。
5. 打开手机的USB调试模式。
6. 根据tesseract的安装目录，修改OCR.py的13行和15行。
7. 根据手机分辨率，修改18行，保证题目在box指定的区域中（box前两个值是左上角的坐标，后两个是右下角坐标，保证题目在这两个坐标确定的矩形框内）。
8. 打开cmd，切换到OCR.py所在目录，运行python OCR.py，出现输入提示的时候，输入除q之外的任意内容，识别区域内的题目（直接回车也行），并在百度搜索。