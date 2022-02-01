import json
import os

def get_data():
  with open("/Users/imac-13/gestion_des_patients-1/data.json", "r") as f:
    if os.path.getsize("/Users/imac-13/gestion_des_patients-1/data.json") == 0:
      return []
    else:
      liste = json.load(f)
      return liste

def recoding():
  donnees = {
    "medicament": "entre.get()",
    "forme": "fort.get()",
    "quantite": "enter.get()",
    "Dosage": "dos.get()",
    "prix": "prixx.get()"
    }

  with open("/Users/imac-13/gestion_des_patients-1/data.json", "w") as f:
    json.dump(donnees, f, indent=4)
