@echo off
title Assault Cube Health Changer
:main
cls
echo.
echo Simple Assault Cube adress manipulator.
echo.
echo Github: www.github.com/DraxFM
echo Discord: Drax#5934
echo.
echo Options:
echo [A] Health Changer
echo [B] Godmode
echo [C] Help
echo [D] Join my Discord server!
echo.
set /p press=Command: 
if /i %press%==A goto hc
if /i %press%==B goto gm
if /i %press%==C goto help
if /i %press%==D goto invite
echo.
echo %press% is not an available command!
echo Press anything to continue...
pause > nul
goto main
exit

:hc
cls
python health.py
pause > nul
exit

:gm
cls
python godmode.py
pause > nul
exit

:help
cls
echo.
echo This page is pretty empty as of right now but if you have problems with the health manipulator, be sure to play in an active match. The manipulator does not work in the lobby!
echo.
echo Press any key to continue...
pause > nul
goto main

:invite
cls
echo.
echo Redirecting to Discord server...
start https://discord.gg/sEXECdC3Et
