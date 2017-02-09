<p align="center">
  <img src="https://raw.githubusercontent.com/black3037/MotorLabGUI/master/Resources/new_motorlab_gui.PNG" alt="motorlab"/>
</p>

A multi-platform (Windows, OSX, Linux) graphical interface for designing and experimenting with controls.

## HOW TO DEPLOY A STAND-ALONE APPLICATION ON YOUR OPERATING SYSTEM

### WHAT YOU NEED BEFORE GETTING STARTED
Stand-Alone applications for Windows, Linux, and OSX already exist in the folder 'Stand-Alone-Applications'.
If you are needing to recompile these files (i.e. you made edits to the GUI or the files don't perform the way you wish them to be)
you will need a few python modules to continue.

In addition to the .py files included in this package you will need:

#####Matplotlib
#####sys, os
#####scipy
#####numpy
#####PyQt4
#####PySerial

Python 2.7 was used in this development.

#### WINDOWS

Step 1: Download the full MotorLabGUI.zip file from GitHub.

Step 2: Extract all files into a new folder (Can be called anything).

Step 3: Navigate to the folder 'Compilers'. Run the file 'CompileMotorLabWindows.bat'.

Step 4: Once the compiler is finished, navigate towards the pyinstaller-develop folder.

Step 5: There should be a newly created folder 'dist'. The .exe is located there.

Possible Errors:

If you are receiving errors when running the 'CompileMotorLabWindows.bat' file, it is possible that the file hierarchy was changed.
It is important that you keep the same folder/file hierarchy that was downloaded in the .zip file. The .bat and compiler reference
certain files and folders in that directory. If all else fails, edit the .bat file to make sure it is locating the pyinstaller-develop
folder. If that fails, you will need to edit the MotorLab.spec file and change the locations of the files it references.

#### OSX

Step 1: Download the full MotorLabGUI.zip file from GitHub.

Step 2: Extract all files into a new folder (Can be called anything).

Step 3: Navigate to folder 'Compilers'. Run the file 'CompileMotorLabOSX.sh'.

Step 4: Once the compiler is finished, navigate towards the pyinstaller-develop folder.

Step 5: There should be a newly created folder 'dist'. The .app is located there.

#### LINUX

Still in development. However still do-able on your own. You will need to change the file hierarchy. Drag all files and folders and
put them in the 'pyinstaller-develop' folder. In command line, type 'pyinstaller MotorLab.spec'. This should compile the stand-alone
application. If this fails you will need to reference the pyinstaller documentation. More than likely the MotorLab.spec file is not
functioning as intended and you will need to generate your own. Once the .spec file is generated you will have to edit the directory
locations to the images provided (if desired).
