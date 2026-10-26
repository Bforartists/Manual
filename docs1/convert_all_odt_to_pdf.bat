@echo off
cd /d "%~dp0"

:: Run this in the manual folder where the ODT files are

set "LIBREOFFICE=C:\Program Files\LibreOffice\program\soffice.exe"

echo Checking if LibreOffice is installed...
if not exist "%LIBREOFFICE%" (
    echo ERROR: LibreOffice not found at "%LIBREOFFICE%"
    echo Please check your LibreOffice installation path.
    pause
    exit /b 1
)

echo Killing any running LibreOffice instances...
taskkill /f /im soffice.bin >nul 2>&1
taskkill /f /im soffice.exe >nul 2>&1

echo.
echo Counting ODT files...
set count=0
for %%f in (*.odt) do set /a count+=1

echo Found %count% ODT files to convert.
echo.

if %count% equ 0 (
    echo No ODT files found to convert.
    pause
    exit /b 1
)

echo Starting batch conversion...
echo.

setlocal enabledelayedexpansion
set current=0
for %%f in (*.odt) do (
    set /a current+=1
    set /a "percent=(current*100)/count"
    
    echo [!current!/%count% - !percent!%%] Converting "%%f"...
    
    "%LIBREOFFICE%" --headless --convert-to pdf "%%f"
    
    if errorlevel 1 (
        echo ERROR: Failed to convert "%%f"
    ) else (
        echo [OK] Successfully converted "%%f"
    )
    
    rem Simple progress bar using ASCII characters
    set /a blocks=percent/5
    set "bar="
    for /l %%i in (1,1,20) do (
        if %%i leq !blocks! (
            set "bar=!bar!#"
        ) else (
            set "bar=!bar!-"
        )
    )
    echo [!bar!] !percent!%% Complete
    echo.
)
endlocal

echo.
echo [####################] 100%% Done!
echo Conversion finished successfully.
echo.
pause
