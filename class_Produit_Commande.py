from abc import ABC, abstractclassmethod
class Produit :
    _nb_produit = 0
    def __init__(self, reference, designation, prix_achat, prix_vente, stock):
        self.reference = reference
        self.designetion = designation
        self.prix_achat = prix_achat
        self.prix_vente = prix_vente
        self.stock = stock  
        Produit._nb_produit += 1

    @property
    def Getprix_achat(self):
        return self.prix_achat
    
    def Setprix_achat(self, value):
        self.prix_achat = value

    @property
    def Getprix_vente(self):
        return self.prix_vente
    
    def Setprix_achat(self, value):
        self.prix_vente = value
    
    @property
    def Getstock(self):
        return self.stock
    
    def Setstock(self, value):
        self.stock = value

    @property
    def Getnbproduit():
        return Produit._nb_produit
    
    def __str__(self):
        return f"La référence de produit: {self.reference}, La designation de produit: {self.designetion}, Le prix d'achat: {self.prix_achat}, Le prix de vente: {self.prix_vente}, Le nombre de quantité de ce produit dans le stock: {self.stock}"

    def __eq__(self, other):
        if self._reference == other._reference :
            return True
        
class Commande :
    import time
    def __init__(self, date, quantite):
        self.date = date
        self.quantite = quantite
    
    @property
    def Getdate(self):
        return self.date
    
    def Setdate(self, value):
        self.date= value

    @property
    def Getquantite(self):
        return self.quantite
    
    def Setquantite(self, value):
        self.quantite = value

    def __str__(self):
        return f"La date : {self.date}, la quantite : {self.quantite}"
    
    def __eq__(self, other):
        return self.date == other.date and self.quantite == other.quantite
    


#test
P1 = Produit(1, "nothing", 250, 500, 287)
P2 = Produit(2, "nothing", 100, 200, 130)
print(P1)
print(P2)
print(f"nombre de produit :{Produit._nb_produit()}")

if P1 == P2 :
    print("Equal")
else :
    print("Not Equal")

C1 = Commande("13/12/2023", 3)
C2 = Commande("13/12/2023", 1)

print(C1)
print(C2)

if C1 == C2 :
    print("Equal")
else :
    print("Not Equal")
