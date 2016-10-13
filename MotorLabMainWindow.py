# ********************************IMPORTS************************************#
# ***************************************************************************#
from PyQt4 import QtGui

from PyQt4.QtGui import QMainWindow, QColor, QFileDialog

from MotorLab_Ui import Ui_Motorlab

from plot_tools import plot_tools

import os
# ***************************************************************************#
# ***************************************************************************#

class MotorLabMainWindow(QMainWindow, Ui_Motorlab):
    def __init__(self):
        
        # Set up the MotorLab Ui
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        # Push Button Signal --> Slot
        self.JogUpButton.clicked.connect(self.jogup)
        self.JogDownButton.clicked.connect(self.jogdown)
        self.StepModelButton.clicked.connect(self.get_step)
        self.BodeModelButton.clicked.connect(self.get_bode)
        self.OpenDirectoryButton.clicked.connect(self.open_directory)
        self.StartButton.toggled.connect(self.start)
        self.GenerateFileButton.clicked.connect(self.create_csv_file)
        self.OpenPython.clicked.connect(self.open_python_interpreter)
        
    def get_step(self):
        
        self.get_graph = plot_tools()
        num,den = self.transferfunction()
        
        if self.PlotAutoFormatCheckBox.isChecked(): self.get_graph.stepmodel2(num,den)
        else: self.get_graph.stepmodel(num,den)
        
    def get_bode(self):
        
        num,den = self.transferfunction()
        self.get_graph = plot_tools()
        
        if self.PlotAutoFormatCheckBox.isChecked(): self.get_graph.bode2(num,den)
        else: self.get_graph.bode(num,den)
            
    def change_directory(self,current_directory):
        
        text,ok = QtGui.QInputDialog.getText(self,'Change Working Directory','Enter the full path to working directory:')
        output_text_to_dataexplorer = 'Directory Changed To: \n' + text        
        self.DataExplorer.setText(output_text_to_dataexplorer)

    def create_csv_file(self):
        
        self.DataExplorer.clear()
        output_string = str(self.FileName.text()) + '.csv'
        self.DataExplorer.setText('Generating  ' + output_string + '\n' + 'Success!')   
        
        fileout = open(output_string,"w")
        fileout.write('Hello World')
        
    def get_current_working_directory(self):
        
        return os.curdir
        
    def jogdown(self):
        
        # Get the current step size and current command
        step = float(self.StepSize.text())
        command = float(self.Command.text())
        
        # Incrememnt command based on stepsize and print to screen
        increment_down = str(command - step)
        self.Command.setText(increment_down)
        
    def jogup(self):
        
        # Get the current step size and current command
        step = float(self.StepSize.text())
        command = float(self.Command.text())
        
        # Incrememnt command based on stepsize and print to screen
        increment_up = str(command + step)
        self.Command.setText(increment_up)
        
    def open_directory(self):
    
        if sys.platform == 'win32':
            current_working_directory = self.get_current_working_directory()
            os.startfile(current_working_directory)
        #TODO: Have this work for Linux and OSX
            
    def open_python_interpreter(self):
        
        if sys.platform == 'win32':
            os.system("start cmd /c python")
    
    def start(self,checked):
        
        if checked: 
            self.StartButton.setText('Stop')
            self.DataExplorer.setText('MotorLab is running...')
        elif not checked: 
            self.StartButton.setText('Start')
            self.DataExplorer.setText('MotorLab stopped')
            
    def transferfunction(self):
    
        numerator = str(self.Numerator.text())
        denominator = str(self.Denominator.text())
        
        num = map(float,numerator.split(","))
        den = map(float,denominator.split(","))
        
        return num,den
            