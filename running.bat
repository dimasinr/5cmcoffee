@echo off
set VENV_DIR=venv

:: Check if virtual environment exists
if not exist %VENV_DIR% (
    echo [INFO] Virtual environment "%VENV_DIR%" not found. Creating one...
    python -m venv %VENV_DIR%
    
    if %ERRORLEVEL% neq 0 (
        echo [ERROR] Failed to create virtual environment. Make sure Python is installed.
        pause
        exit /b %ERRORLEVEL%
    )

    echo [INFO] Activating virtual environment...
    call %VENV_DIR%\Scripts\activate

    echo [INFO] Installing dependencies from requirements.txt...
    if exist requirements.txt (
        pip install -r requirements.txt
    ) else (
        echo [WARNING] requirements.txt not found. Skipping installation.
    )
) else (
    echo [INFO] Virtual environment "%VENV_DIR%" found. Activating...
    call %VENV_DIR%\Scripts\activate
)

:: Run the Django development server
echo [INFO] Starting Django server...
python manage.py runserver

:: Keep window open if server stops
pause
