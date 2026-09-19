@echo off
setlocal
cd /d "%~dp0"

echo =================================================================
echo [*] Launching Artemis: Lunar Flyby XR DEV SANDBOX on Port 3550...
echo =================================================================
echo.
python server.py --dev

pause
