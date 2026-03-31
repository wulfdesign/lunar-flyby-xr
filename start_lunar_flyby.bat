@echo off
setlocal
cd /d "%~dp0"

echo 🧊 Starting Lunar Flyby XR on Port 3550...

:: Check if npx is available
where npx >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Node.js/npm/npx not found. Please install from https://nodejs.org/
    pause
    exit /b
)

:: Open the browser first (serve might block the window)
start http://localhost:3550/index.html

:: Start the server
echo [INFO] Serving on http://localhost:3550
echo [INFO] Press Ctrl+C in this window to stop the server.

npx serve -l 3550
