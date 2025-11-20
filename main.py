from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
import pandas as pd
import io

# Création de l'application FastAPI
app = FastAPI()

# Montage du dossier "static" pour servir les fichiers HTML/CSS/JS
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    """Redirige l'utilisateur vers la page index du frontend"""
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/static/index.html")


@app.post("/excel-to-csv")
async def excel_to_csv(file: UploadFile = File(...)):
    """
    Reçoit un fichier Excel, le convertit en CSV, 
    puis renvoie le fichier CSV en téléchargement.
    """
    
    # Lire le fichier envoyé sous forme de bytes
    contents = await file.read()

    # Charger l'Excel en DataFrame pandas à partir de la mémoire
    df = pd.read_excel(io.BytesIO(contents))
    
    # Convertir le DataFrame en CSV dans un buffer mémoire
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)  # Revenir au début du fichier virtuel
    
    # Retourner le CSV en téléchargement
    return StreamingResponse(
        io.BytesIO(csv_buffer.getvalue().encode()),  # conversion string → bytes
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=converted.csv"}
    )


@app.post("/csv-to-excel")
async def csv_to_excel(file: UploadFile = File(...)):
    """
    Reçoit un fichier CSV, le convertit en Excel (.xlsx),
    puis renvoie le fichier Excel en téléchargement.
    """

    # Lecture du CSV en mémoire
    contents = await file.read()

    # Charger le CSV en DataFrame pandas
    df = pd.read_csv(io.BytesIO(contents))
    
    # Convertir le DataFrame en Excel dans un buffer mémoire
    excel_buffer = io.BytesIO()
    df.to_excel(excel_buffer, index=False, engine='openpyxl')
    excel_buffer.seek(0)  # Revenir au début pour permettre le téléchargement
    
    # Retourner l'Excel en téléchargement
    return StreamingResponse(
        excel_buffer,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=converted.xlsx"}
    )


# Lancement du serveur si le script est exécuté directement
if __name__ == "__main__":
    import uvicorn
    # L'application écoutera sur toutes les interfaces réseau, port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
