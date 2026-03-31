@echo off
setlocal
echo 🚀 Launching Artemis: Lunar Flyby XR...
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  Python not found! Please install Python to run the local server.
    echo.
    echo Attempting to open index.html directly...
    start index.html
    pause
    exit /b
)

:: Start the server in a new window and minimized
echo Starting local web server on port 8000...
start /min "Lunar Flyby Server" python server.py

echo.
echo ✅ Server started! Your browser should open automatically.
echo If it doesn't, navigate to: http://localhost:8000
echo.
echo (Close the other terminal window to stop the server)
pause
