from models import Document, Livre, Dvd
from storage import Jsontorage
from exceptions import DocumentNonTrouveError, ISBNInvalideError


class GestionnaireMediatheque:
    def __init__(self, storage = Jsontorage):
        self.storage = storage
        self.documents: list[Document] = []
        self.charger_mediatheque()

    def ajouter_document(self):
        self.documents.append(Document)
        self.ajouter_document()#pourquoi self???? expliquer bien le role de self

    def sauvegarder_mediatheque(self):
        donnees = {
            "Document": [d.to_dict() for d in self.documents]
        }
        self.storage.sauvegarder(donnees)#la difference entre sauvegarder et savegarder mediatheque

    def charger_mediatheque(self):
        donnees = self.storage.charger()
        for m_dict in donnees.get("Document",[]):#je suppose que m_dict fais reference a mon_dictionnaire mais il n'as jamais ete instancier comment python peut le reconnaitre, c'est pareil dans d in self.doculents on n'a jamais definis l'allias
        # pourquoi "Document" et pas Document
            type_d = m_dict.get("type")
            if type_d == "Livre":
                self.documents.append(Livre.from_dict(m_dict))
            if type_d == "Dvd":
                self.documents.append(Dvd.from_dict(m_dict))

    def supprimer_document(self, isbn):
        for document in self.documents:
            if isbn == document.isbn:
                self.documents.remove(document)
        
        raise DocumentNonTrouveError("Document Introuvable")
        self.sauvegarder_mediatheque()

    def emprumter_document(self, isbn):
        for document in self.documents:
            if isbn == document.isbn:
                if document.disponible:
                    print(f"{self.documents} emprumté avec succès")
                    self.documents.disponnible == False
                else:
                    print(f"{self.documents} indisponible")
            
        raise ISBNInvalideError("Isbn Invalide")
        self.sauvegarder_mediatheque()

    def retourner_document(self, isbn):
        for document in self.documents:
            if isbn == document.isbn:
                if self.emprumter_document(isbn):
                    print(f"{self.documents} retourner avec succès")
                    self.documents.disponnible == True
                else:
                    print(f"{self.documents} indisponible")
        raise DocumentNonTrouveError("Document introuvable")
                