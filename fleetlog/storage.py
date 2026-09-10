import json
import os

class JSONStorage:
    def __init__(self, filepath: str = "flotte.json"):
        self.filepath = filepath

    def sauvegarder(self, donnees: dict):
        with open(self.filepath, "w", encoding= "utf-8") as f:
            json.dump(donnees, f, indent=4)

    def charger(self) -> dict:
        if not os.path.exists(self.filepath):
            return {"vehicules" : []}
        else:
            try:
                with open(self.filepath, "r", encoding= "utf-8") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return{"vehicules" : []}
