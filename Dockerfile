FROM python:3.11-slim

# Définit le dossier de travail
WORKDIR /app

# Copie le fichier requirements.txt
COPY requirements.txt .

# Installe les dépendances 
RUN pip install --no-cache-dir -r requirements.txt

# Copie le fichier main.py et le dossier static dans l'image Docker
COPY main.py .
COPY static/ ./static/

# Indique que le conteneur va utiliser le port 8000
EXPOSE 8000

# Démarre FastAPI avec uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
