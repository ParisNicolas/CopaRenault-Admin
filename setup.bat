@echo off

REM Crea un entorno virtual en la carpeta 'venv'
python -m venv .venv

REM Activa el entorno virtual
call .venv/Scripts/activate.bat

REM Instala los paquetes requeridos desde requirements.txt
pip install -r requirements.txt

REM Crea el archivo .env
if not exist .env (
    type nul > .env
)