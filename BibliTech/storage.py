import json
import os
#pourquoi ici on ne met pas from

class Jsontorage:
    def __init__(self, filepath: str = "mediatheque.json"):
        self.filepath = filepath

    def sauvegarder(self, donnees: dict):# donnee = data dans to_dict??? Alors pourquoi ne pas mettre to dict directement
        with open(self.filepath, "w", encoding= "utf-8") as f:
            json.dump(donnees, f, indent= 4)
    def charger(self) -> dict:
        if not os.path.exists(self.filepath):
            return {"Document" : []}
        else:
            try:
                with open(self.filepath, "r", encoding= "utf-8") as f:
                    json.load(f)
            except json.JSONDecodeError:
                return{"Document" : []}


            

