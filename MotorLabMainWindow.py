#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% IMPORTS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from PyQt4 import QtGui

from PyQt4.QtGui import QMainWindow, QFileDialog

from MotorLab_Ui import Ui_Motorlab

from SerialCommunication import SerialOptions

from plot_tools import plot_tools

import sys
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

class MotorLabMainWindow(QMainWindow, Ui_Motorlab):
    def __init__(self):
        
        # Set up the MotorLab Ui
        super(MotorLabMainWindow,self).__init__()
        #QMainWindow.__init__(self)
        self.setupUi(self)
        
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #%%%%%%%%%%%%%%%%%%%%%%% SIGNALS & SLOTS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        self.JogUpButton.clicked.connect(self.jogup)
        
        self.JogDownButton.clicked.connect(self.jogdown)
        
        self.StepModelButton.clicked.connect(self.get_step)
        
        self.BodeModelButton.clicked.connect(self.get_bode)
        
        self.OpenDirectoryButton.clicked.connect(self.open_directory)
        
        self.StartButton.toggled.connect(self.start)
        
        self.GenerateFileButton.clicked.connect(self.create_xlsx_file)
        
        self.OpenPython.clicked.connect(self.open_python_interpreter)
        
        self.SampleCount.returnPressed.connect(self.update_data_params)
        
        self.SampleRate.returnPressed.connect(self.update_data_params)
        
        self.Duration.returnPressed.connect(self.update_data_params)
        
        self.PlotDataButton.clicked.connect(self.get_data_plot)
        
        self.OpenFlashDir.clicked.connect(self.open_flash_directory)
        
        self.RefreshComButton.clicked.connect(self.update_ports)
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                
    def change_directory(self,current_directory):
        
        text,ok = QtGui.QInputDialog.getText(self,'Change Working Directory','Enter the full path to working directory:')
        output_text_to_dataexplorer = 'Directory Changed To: \n' + text        
        self.DataExplorer.setText(output_text_to_dataexplorer)

    def create_xlsx_file(self):
        
        import xlsxwriter
        
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
        
        self.DataExplorer.clear()
        output_string = str(self.FileName.text()) + '.xlsx'        
        
        workbook = xlsxwriter.Workbook(output_string)
        worksheet = workbook.add_worksheet()
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

        
    def get_bode(self):
   
        num,den = self.transferfunction()
        self.get_graph = plot_tools()
        
        if self.PlotAutoFormatCheckBox.isChecked(): 
            
            self.get_graph.bode2(num,den)
        
        else: 
            
            self.get_graph.bode(num,den)
        
    def get_current_working_directory(self): 
        
        import os
        
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
            
    def get_directory_to_flash(self):
        
            return self.FlashMotorLabDir.text()
            
    def get_step(self):
        
        
        self.get_graph = plot_tools()
        num,den = self.transferfunction()
        
        if self.PlotAutoFormatCheckBox.isChecked(): 
            
            self.get_graph.stepmodel2(num,den)
            
        else: 
            
            self.get_graph.stepmodel(num,den)
        
    def jogdown(self):
        
        step = float(self.StepSize.text())
        command = float(self.Command.text())
        
        increment_down = str(command - step)
        self.Command.setText(increment_down)
        
    def jogup(self):
        
        step = float(self.StepSize.text())
        command = float(self.Command.text())
        
        increment_up = str(command + step)
        self.Command.setText(increment_up)
        
    def open_directory(self):
        
        current_working_directory = self.get_current_working_directory()
        
        if sys.platform == 'win32': 
            
            import os
            
            os.startfile(current_working_directory)
            
        elif sys.platform =='darwin':
            
            import subprocess 
            
            subprocess.Popen(['open',current_working_directory])
            
        else: 
            
            try:
                
                import subprocess 
                
                subprocess.Popen(['open',current_working_directory])
                
            except:
                
                message = QtGui.QMessageBox()
                message.setText('OS currently not supported')
                message.setWindowTitle('Warning')
            
    def open_flash_directory(self):
        
        current_directory = self.get_current_working_directory()
        path = str(QFileDialog.getOpenFileName(self,"Select .bin file",directory = current_directory))
        self.FlashMotorLabDir.setText(path)

    def open_python_interpreter(self):
    
        import subprocess
        
        if sys.platform == 'win32':
            
            try:
                
                subprocess.check_call('start python',shell=True)

            except:
                
                warning = QtGui.QMessageBox()
                warning.setText("Please check that Python is installed." \
                " It is required for some functionality of this application")
                warning.setWindowTitle('Warning')
                warning.exec_()
            
        elif sys.platform == 'darwin':
            
            # OSX has native python support, no error checking needed            
            subprocess.Popen(['open','-a','Terminal','-n'])
            subprocess.call(['python'])
            
        elif sys.platform == 'linux2':
            
            warning = QtGui.QMessageBox()
            warning_message = 'Sorry! Still needs implementation on' + str(sys.platform)
            warning.setText(warning_message)
            warning.setWindowTitle('Warning')
            warning.exec_()
            
        else:
            
            warning = QtGui.QMessageBox()
            warning_message = 'Sorry! Still needs implementation on' + str(sys.platform)
            warning.setText(warning_message)
            warning.setWindowTitle('Warning')
            warning.exec_()
            
    def set_text_callback(self,output_string):

        self.DataExplorer(output_string)
    
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
        
    def update_ports(self):
                
        self.DataExplorer.setText('Refreshing Communication Ports...')
        
        get_ports = SerialOptions()
        ports = get_ports.getPorts()
        
        self.COMPortComboBox.clear()
        self.COMPortComboBox.addItems(ports)
        
        self.DataExplorer.append('Found ports at:')
        self.DataExplorer.append(str(ports))
        self.DataExplorer.append('Select appropriate port from menu and connect')
        
        
        
            