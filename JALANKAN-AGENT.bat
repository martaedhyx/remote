@echo off
title Edhy Remote Agent
cd /d "%~dp0"
py -3.8 -m pip install -r requirements.txt
if errorlevel 1 (
  echo.
  echo Installation failed. Install Python 3.8 first, then run this file again.
  pause
  exit /b 1
)
py -3.8 remote_agent.py
pause
