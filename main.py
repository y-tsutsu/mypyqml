import sys
from os.path import dirname, join

from PyQt5.QtCore import Q_ARG, QMetaObject, QTimer, QUrl, QVariant
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView

counter = 0


def onTimeout(obj):
    global counter
    value = {'message': f'{counter}: Hello!!!!!!!'}
    QMetaObject.invokeMethod(obj, 'append', Q_ARG(QVariant, value))
    counter += 1


def main():
    app = QGuiApplication(sys.argv)
    view = QQuickView()
    url = QUrl(join(dirname(__file__), 'sample.qml'))
    view.setSource(url)
    timer = QTimer()
    timer.timeout.connect(lambda: onTimeout(view.rootObject()))
    timer.start(10)
    view.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
