#IMPORTANTE.....activar todo este codigo con el comando......          .\buildfronted.ps1



# Activar el entorno virtual
.venv\Scripts\Activate.ps1

# Actualizar pip
pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt

# Actualizar Reflex a la última versión
pip install reflex --upgrade

# Eliminar carpeta "public" si existe
if (Test-Path public) {
    Remove-Item public -Recurse -Force
}

# Inicializar Reflex
reflex init

# Exportar solo frontend
reflex export --frontend-only

# Descomprimir frontend.zip en carpeta public
Expand-Archive -Path frontend.zip -DestinationPath public -Force

# Borrar el archivo zip generado
Remove-Item frontend.zip -Force

# Desactivar el entorno virtual
deactivate

# Subir cambios a GitHub
git add .
git commit -m "Añadiendo mejoras y componentes"
git push origin main
