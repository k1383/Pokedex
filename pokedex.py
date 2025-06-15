import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

fenetre = tk.Tk()
fenetre.geometry("1024x768")
fenetre.title("Pokedex")
# fenetre.configure(bg='#f3eded')

liste_Pokemon = ["Pikachu", "Dracaufeu", "Rondoudou"]

labelChoix = tk.Label(fenetre, text="Veuillez choisir un Pokémon !", bg='#f3eded', font=("Arial", 12))
labelChoix.place(y=250, x=100)

listeCombo = ttk.Combobox(fenetre, values=liste_Pokemon)
listeCombo.place(y=250, x=330)


bouton_1 = tk.Button(fenetre, text="       OK      ", command=lambda: afficher_pokemon())
bouton_1.place(y=300, x=100)

bouton_2 = tk.Button(fenetre, text="Supprimer", command=lambda: supprimer_pokemon())
bouton_2.place(y=300, x=170)

image_Pikachu = ImageTk.PhotoImage(Image.open(r"img\Pikachu.jpeg"))
Pikachu_image = tk.Label(fenetre, image=image_Pikachu)
Pikachu_image.place_forget()

image_Dracaufeu = ImageTk.PhotoImage(Image.open(r"img\Dracaufeu.png"))
Dracaufeu_image = tk.Label(fenetre, image=image_Dracaufeu)
Dracaufeu_image.place_forget()

image_Rondoudou = ImageTk.PhotoImage(Image.open(r"img\Rondoudou.png"))
Rondoudou_image = tk.Label(fenetre, image=image_Rondoudou)
Rondoudou_image.place_forget()


def afficher_pokemon():
    choix = listeCombo.get()
    
    Pikachu_image.place_forget()
    Dracaufeu_image.place_forget()
    Rondoudou_image.place_forget()

    if choix == "Pikachu":
        Pikachu_image.place(y=250, x=700)
    elif choix == "Dracaufeu":
        Dracaufeu_image.place(y=250, x=700)
    elif choix == "Rondoudou":
        Rondoudou_image.place(y=250, x=700)

def supprimer_pokemon():
    choix = listeCombo.get()
    if choix in liste_Pokemon:
        liste_Pokemon.remove(choix)
        listeCombo["values"] = liste_Pokemon

# Ajout d'un Pokémon
Ajout = tk.Label(fenetre, text="Ajouter un nouveau Pokémon", font=("Arial", 12))
Ajout.place(y=470, x=170)

# Nom 
Nom_pokemon = tk.Label(fenetre, text="Nom", bg='#f3eded')
Nom_pokemon.place(y=530, x=150)
Nom_du_pokemon = tk.Entry(fenetre)
Nom_du_pokemon.place(y=560, x=100, width=150)

# Type
Type_pokemon = tk.Label(fenetre, text="Type", bg='#f3eded')
Type_pokemon.place(y=530, x=330)
Type_du_pokemon = tk.Entry(fenetre)
Type_du_pokemon.place(y=560, x=270, width=150)

# Capacité
Capacite_pokemon = tk.Label(fenetre, text="Capacité", bg='#f3eded')
Capacite_pokemon.place(y=610, x=220)
Capacite_du_pokemon = tk.Entry(fenetre)
Capacite_du_pokemon.place(y=640, x=100, width=320)

# Lien de l'image du Pokémon
image_nouveau_pokemon = tk.Label(fenetre, text="Lien de l'image du Pokémon", bg='#f3eded')
image_nouveau_pokemon.place(y=690, x=180)
Pokemon_nouveau_image = tk.Entry(fenetre)
Pokemon_nouveau_image.place(y=720, x=100, width=320)

bouton_3 = tk.Button(fenetre, text="Ajouter", command=lambda: ajouter_pokemon())
bouton_3.place(y=770, x=230)

def ajouter_pokemon():
    nouveau_pokemon = Nom_du_pokemon.get()
    if nouveau_pokemon and nouveau_pokemon not in liste_Pokemon:
        liste_Pokemon.append(nouveau_pokemon)
        listeCombo["values"] = liste_Pokemon
        Nom_du_pokemon.delete(0, tk.END)
        Type_du_pokemon.delete(0, tk.END)
        Capacite_du_pokemon.delete(0, tk.END)
        Pokemon_nouveau_image.delete(0, tk.END)


fenetre.mainloop()

# Dans le terminale  →  python .\pokedex.py