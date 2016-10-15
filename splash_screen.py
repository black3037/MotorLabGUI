from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from MotorLabMainWindow import MotorLabMainWindow

if __name__ == "__main__":
    import sys, time

    splashme = QApplication(sys.argv)

    # Create and display the splash screen
    splash_pix = QPixmap('splash_loading.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    splashme.processEvents()

    # Simulate something that takes time
    time.sleep(2)
    
    app = QtGui.QApplication(sys.argv)
    app.setStyle('cleanlooks')
    window = MotorLabMainWindow()
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())
	
	