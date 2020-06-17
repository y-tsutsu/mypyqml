import sys
from os.path import dirname, join

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView


def main():
    app = QGuiApplication(sys.argv)
    view = QQuickView()

    view.engine().quit.connect(app.quit)
    view.rootContext().setContextProperty(
        "imageUrl", 'https://pbs.twimg.com/profile_images/712812877439062017/xZNnGcXW.jpg')

    url = QUrl(join(dirname(__file__), 'sample.qml'))
    view.setSource(url)
    view.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
