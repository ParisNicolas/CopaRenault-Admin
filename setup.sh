python3 -m venv venv

# Activa el entorno virtual (macOS/Linux usa source para activar)
source venv/bin/activate

# Instala los paquetes requeridos desde requirements.txt
pip install -r requirements.txt

# Crear el archivo .env vacío si no existe
if [ ! -f .env ]; then
    touch .env
    echo "Archivo .env creado."
else
    echo "El archivo .env ya existe."
fi