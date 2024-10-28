# CopaRenault-Admin
Una aplicacion dedicada a la administracion de la copa renault 2024, exclusiva para los trabajadores

 
## Instalacion
Clona el repositorio.
```bash
git clone https://github.com/ParisNicolas/CopaRenault.git
cd CopaRenault
```

### Ejecuta *setup* o sigue las siguientes instrucciones:

#### 1) Usando script setup:
Windows:
```bash
./setup.bat
```
MAC:
```bash
bash setup.sh
```

#### 2) Manualmente:
***Crea el entorno virtual y activalo (opcional).***
```bash
python -m venv .venv
.venv/Scripts/activate
```
> En mac seria ```source .venv/Scripts/activate```

***Instala las dependencias:***
```bash
pip install -r requirements.txt
```

***Crea el archivo .env:***
```
SECRET_KEY=...
SQLALCHEMY_DATABASE_URI=...
```


## Corre el codigo
### Con script run:
> Es necesario en el cole por los entornos virtuales
> Las computadoras tienen desactivado los scripts y el CMD

Sino usas entorno ejecuta ```flask run --debug```

##### Windows
```bash
./run.bat
```
manualmente:
```bash
.venv/Scripts/activate
flask run --debug
```


##### MAC
```bash
source .venv/Scripts/activate
flask run --debug
```


## Proyecto

### Dependencias
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Login
- Flask-WTF
- mysql-connector-python
- python-dotenv

### Variables de entorno
- **SECRET_KEY:** Clave secreta que se usara para cifrar las sessiones y tokens
- **DATABASE_URL:** Url completa de la base de datos (CleverCloud u otra)


### Anotaciones:

- admin (sistema de envio de notificaciones, resetear base de datos, cambiar FG -> Llaves)
- 
