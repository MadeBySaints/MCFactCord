@echo off
title MCFactCord
color 0A

echo ==============================================================
echo                              MCFC                     
echo ==============================================================
echo                Listening for keywords in chat...             
echo ==============================================================

:: Delay for a second to make the UI look nice
timeout /t 1 >nul

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b
)

:: Start the bot
echo Starting bot...
echo ==============================================================
python mcfc.py

:: Error handling
if %errorlevel% neq 0 (
    echo.
    echo ==============================================================
    echo                    Bot encountered an error                  
    echo ==============================================================
    echo Check your configuration or code and try again.
    echo ==============================================================
    pause
    exit /b
)

echo Bot stopped running. Press any key to exit...
pause >nul
