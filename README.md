<p align="center">
  <img/>![alt tag](https://github.com/black3037/MotorLabGUI/blob/master/Resources/splash_loading.png)
</p>


# MOTORLAB

A multi-platform (Windows, OSX, Linux) graphical interface for designing and experimenting with controls on the 'Motorlab'.

## HOW TO DEPLOY A STAND-ALONE APPLICATION ON YOUR OPERATING SYSTEM

### WINDOWS

Step 1: Download the full MotorLabGUI.zip file from GitHub.

Step 2: Extract all files into a new folder (Can be called anything).

Step 3: Navigate to the folder 'Compilers'. Run the file 'CompileMotorLabWindows.bat'.

Step 4: Done! The compiler will take a couple minutes to create your executable.

Possible Errors:

If you are receiving errors when running the 'CompileMotorLabWindows.bat' file, it is possible that the file hierarchy was changed.
It is important that you keep the same folder/file hierarchy that was downloaded in the .zip file. The .bat and compiler reference
certain files and folders in that directory. If all else fails, edit the .bat file to make sure it is locating the pyinstaller-develop
folder. If that fails, you will need to edit the MotorLab.spec file and change the locations of the files it references.

### OSX

Step 1: Download the full MotorLabGUI.zip file from GitHub.

Step 2: Extract all files into a new folder (Can be called anything).

Step 3: Navigate to folder 'Compilers'. Run the file 'CompileMotorLabOSX.sh'.

Step 4: Done! The compiler will take a couple minutes to create your executable.

### LINUX

Still in development. However still do-able on your own. You will need to change the file hierarchy. Drag all files and folders and
put them in the 'pyinstaller-develop' folder. In command line, type 'pyinstaller MotorLab.spec'. This should compile the stand-alone
application. If this fails you will need to reference the pyinstaller documentation. More than likely the MotorLab.spec file is not
functioning as intended and you will need to generate your own. Once the .spec file is generated you will have to edit the directory
locations to the images provided (if desired).
