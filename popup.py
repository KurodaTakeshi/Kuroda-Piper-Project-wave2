import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QTimer

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Information')
    label = QLabel('Sendding csv data to GCP...', window)
    window.move(5,970)
    window.resize(400,50)
    
    window.show()
    QTimer.singleShot(3000, window.close)
    sys.exit(app.exec_())