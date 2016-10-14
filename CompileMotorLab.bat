REM Place CompileMotorLab.bat and MotorLab.py and all associated files of
REM Motorlab in the same top directory of the pyinstaller-develop folder
REM Then you can run this script to compile to an .exe
ECHO Compiling MotorLab.exe
ECHO This will take some time, please be patient
ECHO Pyinstaller will throw some warnings to you, but it should still work
python pyinstaller.py MotorLab.py --onefile --windowed
pause