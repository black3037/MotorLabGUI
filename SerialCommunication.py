from serial.tools import list_ports

import serial


class SerialTools(serial.Serial):
    
    def __init__(self):
        
        self.serial_tools = serial.tools
    
    def getPorts(self):
        
        # There exists list_ports_operating_system for serial tools
        # Might needs to do error handling for different OSs if the
        # general list_ports doesn't function as expected
        port_list = list_ports.comports()
        ports = []
        
        for port in port_list:
            ports.append(str(port[0]))
            
        return ports
        
class SerialOptions(SerialTools):
    
    def __init__(self):
        
        # Call base class's init function
        super(SerialOptions,self).__init__()
    
        # Set up instance of serial
        self.serial_port = serial.Serial()
    
    def connectMotorLab(self,port_name):
                
        port_open = False
        
        if self.serial_port.is_open == False:
            
            port_open = True
            self.serial_port.port = port_name
            self.serial_port.open()

        return port_open
        
        
    def disconnectMotorlab(self,port_name):

        port_open = self.connectMotorLab(port_name)    
        
        if port_open == True:

            self.serial_port.close()
            
        else:
            
            pass
            
        
    def getData(self):
        
        # Needs implementation        
        
        return
        
    def sendData(self):
        
        # Needs implementation
        
        return
        
    def _txReceived(self):
        
        # Needs implementation
        
        return
        
    def _rxReceived(self):
        
        # Needs implementation
        
        return
