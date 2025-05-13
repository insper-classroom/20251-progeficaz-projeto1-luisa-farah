import json
import os 

def load_data(notes):
    
    path = os.path.join("static", "data", notes)
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data

def load_template(arquivo):
    path = os.path.join("static", "templates", arquivo)
    with open(path, encoding="utf-8") as f:
        return f.read()
    
def save_note(nota):
    path = os.path.join("static", "data", "notes.json")
    with open(path, encoding="utf-8") as f:
        notas = json.load(f)

    notas.append(nota)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(notas, f, ensure_ascii=False, indent=2)    