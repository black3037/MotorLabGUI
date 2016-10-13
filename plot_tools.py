"""

Simple plotting tools for the MotorLab GUI


"""
# ********************************IMPORTS************************************#
# ***************************************************************************#
from PyQt4.QtGui import QMainWindow

from MotorLab import Ui_Motorlab

import matplotlib.pyplot as plt

from scipy import signal
# ***************************************************************************#
# ***************************************************************************#

class plot_tools(QMainWindow, Ui_Motorlab):
    def __init__(self):        
        QMainWindow.__init__(self)
        self.setupUi(self)
        
    def bode(self,num,den):
        
        w, mag, phase = signal.bode((num,den))
        
        constant_line_gain = [0]*w
        
        # Plot Formatting
        plt.ion()
        plt.close(2)
        f, axarr = plt.subplots(2, sharex=True)
        plt.subplot(211)
        plt.semilogx(w,mag,'dodgerblue')
        plt.semilogx(w,constant_line_gain,color='grey',linestyle='-.')
            
        plt.title('Bode Diagram')
        plt.ylabel('Magnitude (dB)')
        plt.subplot(212)
        plt.semilogx(w, phase,'dodgerblue')
        plt.ylabel('Phase (Deg)')
        plt.xlabel('Frequency (rad/s)')
        plt.figure(2)
        
        return plt.show()
    
    def bode2(self,num,den):
        
        w, mag, phase = signal.bode((num,den))
        
        # Plot formatting
        plt.ion()
        plt.close(2)
        plt.rc('font', family='serif')
        plt.rc('xtick', labelsize='x-small')
        plt.rc('ytick', labelsize='x-small')     
        f, axarr = plt.subplots(2, sharex=True)
        plt.subplot(211)
        plt.semilogx(w,mag,'black')
        plt.title('Bode Diagram')
        plt.ylabel('Magnitude (dB)')
        plt.grid(True, which="both")
        plt.subplot(212)
        plt.semilogx(w, phase,'black')  
        plt.ylabel('Phase (Deg)')
        plt.xlabel('Frequency (rad/s)')
        plt.grid(True,which="both")
        plt.figure(2)
        
        return plt.show()
    
    def stepmodel(self,num,den):
                
        t, y = signal.step2((num,den))
        
        #TODO: Note this messes up for unstable or oscillatory systems
        get_last_value = y[-1]
        dcgain = [get_last_value]*len(t)
     
        # Plot Formatting
        plt.ion()
        plt.close(1)
        plt.plot(t,y,'dodgerblue',t,dcgain,'k:')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Amplitude')
        plt.title('Step Response')
        plt.figure(1)
        
        return plt.show()
            
    def stepmodel2(self,num,den):
        
        t, y = signal.step2((num,den))
        
        #TODO: Note this messes up for unstable or oscillatory systems
        get_last_value = y[-1]
        dcgain = [get_last_value]*len(t)
        
        # Plot Formatting
        plt.ion()
        plt.close(1)
        plt.rc('font', family='serif')
        plt.rc('xtick', labelsize='x-small')
        plt.rc('ytick', labelsize='x-small')            
        plt.plot(t,y,'black',label='Model')
        plt.plot(t,dcgain,'k:',label='Command')
        plt.fill_between(t,y,dcgain,color='lightgrey',alpha=0.3)
        plt.xlabel('Time (seconds)')
        plt.ylabel('Amplitude')
        plt.title('Step Response')
        plt.legend(loc='lower right')
        plt.figure(1)
        
        return plt.show()
          