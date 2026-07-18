@echo off
title Git Commit y Push

echo ===============================
echo   Git Commit Automatico
echo ===============================
echo.

REM Comprobar estado
git status

echo.
set /p mensaje=Introduce el mensaje del commit: 

git add .

git commit -m "%mensaje%"

git push 

echo.
echo ===============================
echo      Proceso finalizado
echo ===============================
pause