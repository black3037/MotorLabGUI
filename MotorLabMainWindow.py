# ********************************IMPORTS************************************#
# ***************************************************************************#
from PyQt4 import QtGui

from PyQt4.QtGui import QMainWindow, QColor, QFileDialog

from MotorLab_Ui import Ui_Motorlab

from plot_tools import plot_tools

import os

import sys

import csv
# ***************************************************************************#
# ***************************************************************************#

class MotorLabMainWindow(QMainWindow, Ui_Motorlab):
    def __init__(self):
        
        # Set up the MotorLab Ui
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #%%%%%%%%%%%%%%%%%%%%%%% SIGNALS & SLOTS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        self.JogUpButton.clicked.connect(self.jogup)
        
        self.JogDownButton.clicked.connect(self.jogdown)
        
        self.StepModelButton.clicked.connect(self.get_step)
        
        self.BodeModelButton.clicked.connect(self.get_bode)
        
        self.OpenDirectoryButton.clicked.connect(self.open_directory)
        
        self.StartButton.toggled.connect(self.start)
        
        self.GenerateFileButton.clicked.connect(self.create_csv_file)
        
        self.OpenPython.clicked.connect(self.open_python_interpreter)
        
        self.SampleCount.returnPressed.connect(self.update_data_params)
        
        self.SampleRate.returnPressed.connect(self.update_data_params)
        
        self.Duration.returnPressed.connect(self.update_data_params)
        
        self.PlotDataButton.clicked.connect(self.get_data_plot)
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        
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
        import xlsxwriter
        self.DataExplorer.clear()
        output_string = str(self.FileName.text()) + '.xlsx'        
        
        workbook = xlsxwriter.Workbook(output_string)
        worksheet = workbook.add_worksheet()
        
        # Placeholder data for now...
        current = [-0.12,-0.10,-0.08,-0.06,-0.03,0,0.03,0.06,0.08,0.10,0.12]
        output_data = [-3080*(2*3.14/60),
                       -2000*(2*3.14/60),
                       -950*(2*3.14/60),
                       0,
                       0,
                       0,
                       0,
                       0,
                       920*(2*3.14/60),
                       2030*(2*3.14/60),
                       3220*(2*3.14/60)
                       ] 
        row,col = 0,0
        
        for i in current:
            worksheet.write(row,col,i)
            row += 1
            if i == current[-1]:
                row = 0
        
        for j in output_data:
            worksheet.write(row,col+1,j)
            row += 1
        
        workbook.close()        
        self.DataExplorer.setText('Generating  ' + output_string + '\n' + 'Success!')   
        
    def get_current_working_directory(self): 
        
        return os.curdir
        
    def get_data_plot(self):
        
        self.get_graph = plot_tools()
        
        current = [-0.12,-0.10,-0.08,-0.06,-0.03,0,0.03,0.06,0.08,0.10,0.12]
        output_data = [-3080*(2*3.14/60),
                       -2000*(2*3.14/60),
                       -950*(2*3.14/60),
                       0,
                       0,
                       0,
                       0,
                       0,
                       920*(2*3.14/60),
                       2030*(2*3.14/60),
                       3220*(2*3.14/60)
                       ] 
        
        if self.FitDataCheckBox.isChecked():
            self.get_graph.fitdata(current,output_data)
        else:
            self.get_graph.plotdata(current,output_data)
        
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
        
        current_working_directory = self.get_current_working_directory()
        
        if sys.platform == 'win32': 
            os.startfile(current_working_directory)
            
        elif sys.platform =='darwin':
            import subprocess 
            subprocess.Popen(['open',current_working_directory])
            
        else: 
            message = QtGui.QMessageBox()
            message.setText('OS currently not supported')
            
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
        
    def update_data_params(self):
        
        sample_rate = float(self.SampleRate.text())
        sample_count = float(self.SampleCount.text())
        duration = sample_count / sample_rate
        self.Duration.setText(str(duration))
            