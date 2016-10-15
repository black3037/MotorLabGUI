"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

$$\      $$\  $$$$$$\ $$$$$$$$\  $$$$$$\  $$$$$$$\  $$\        $$$$$$\  $$$$$$$\  
$$$\    $$$ |$$  __$$\\__$$  __|$$  __$$\ $$  __$$\ $$ |      $$  __$$\ $$  __$$\ 
$$$$\  $$$$ |$$ /  $$ |  $$ |   $$ /  $$ |$$ |  $$ |$$ |      $$ /  $$ |$$ |  $$ |
$$\$$\$$ $$ |$$ |  $$ |  $$ |   $$ |  $$ |$$$$$$$  |$$ |      $$$$$$$$ |$$$$$$$\ |
$$ \$$$  $$ |$$ |  $$ |  $$ |   $$ |  $$ |$$  __$$< $$ |      $$  __$$ |$$  __$$\ 
$$ |\$  /$$ |$$ |  $$ |  $$ |   $$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |
$$ | \_/ $$ | $$$$$$  |  $$ |    $$$$$$  |$$ |  $$ |$$$$$$$$\ $$ |  $$ |$$$$$$$  |
\__|     \__| \______/   \__|    \______/ \__|  \__|\________|\__|  \__|\_______/ 
                                                                                                                                
MotorLab (c)
Kansas State University
Developers: Derek Black, Shane Smith, Dale Schinstock
MIT Open License
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
List of files needed to be linked:

Start File  MotorLab.py

Linked      MotorLab_Ui.py
            MotorLabmainWindow.py
            plot_tools.py
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   
"""
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% IMPORTS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from PyQt4 import QtGui

from PyQt4.QtCore import *

from PyQt4.QtGui import *

from MotorLabMainWindow import MotorLabMainWindow

import sys, time
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
""" 


Start up the GUI                                                               
       
                                                                           
"""
if __name__ == "__main__":

    # Create and display the splash screen
    splashme = QApplication(sys.argv)
    splash_pix = QPixmap('splash_loading.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    splashme.processEvents()
    time.sleep(3)
    
    app = QtGui.QApplication(sys.argv)
    
    # Give GUI a theme
    # Some look better than others on different operating systems
    # That is why I choose not to use a single style
    if sys.platform == 'win32':
        
        app.setStyle('cleanlooks')
        
    elif sys.platform == 'darwin':
        
        app.setStyle('mac')
        
    elif sys.platform == 'linux2':
        
        app.setStyle('cleanlooks')
    
    else: 
        
        app.setStyle('cleanlooks')
        
        
        
    window = MotorLabMainWindow() # Create instance of Motor Main Window Class
    window.show()                 # Show the GUI to the end user
    splash.finish(window)         # Terminate splash after GUI is loaded
    sys.exit(app.exec_())         # Exit