@echo off

REM Activa el entorno
call .venv/Scripts/activate.bat

REM Corre la aplicacions
flask run --debug