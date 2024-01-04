class Batiment():
    
    def __init__(self, name, etage, adresse):
        self.name = name
        self.etage = etage
        self.adresse = adresse
        print("Un nouveau bâtiment a été créé ! Nom :", self.name,"/étages:", self.etage,"/adresse:", self.adresse)
        
        
class Supermarket(Batiment):
    
    def __init__(self, name, etage, adresse, nbrerayon):
        super().__init__(name, etage, adresse)
        self.nbrerayon = nbrerayon
        
    def get_nbrerayon(self):
        return self.nbrerayon
        
supermarche1 = Supermarket("Intermarche", 3, "92 rue des Roches", 95)

print(supermarche1.get_nbrerayon())