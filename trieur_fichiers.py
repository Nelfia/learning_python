from pathlib import Path

dirs = {".png": "Images",
        ".jpeg": "Images",
        ".jpg" : "Images",
        ".bmp" : "Images",
        ".gif" : "Videos",
        ".mp4" : "Videos",
        ".avi" : "Videos",
        ".mov" : "Videos",
        ".zip" : "Archives",
        ".txt" : "Documents",
        ".pptx" : "Documents",
        ".odt" : "Documents",
        ".odp" : "Documents",
        ".pages" : "Documents",
        ".pdf" : "Documents",
        ".json" : "Documents",
        ".mp3" : "Musiques",
        ".wav" : "Musiques",
        ".flac" : "Musiques"
        }
# Créer un objet Path qui point vers le dossier à trier
tri_dossier = Path.home() / "Downloads/sources/data"
print(tri_dossier)
# Récupérer tous les fichiers dans le dossier
files = [f for f in tri_dossier.iterdir() if f.is_file()]
# Boucler sur chaque fichier
for f in files:
    # Déterminer le chemin du dossier vers lequel l'envoyer en fonction de son suffixe
    futur_dossier = tri_dossier / dirs.get(f.suffix, "Divers")
    # Créer le dossier s'il n'existe pas
    futur_dossier.mkdir(exist_ok=True)
    # Déplacer le fichier vers le dossier
    f.rename(futur_dossier / f.name)